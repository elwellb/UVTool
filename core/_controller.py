# core/_controller.py

import os
import hou
import time

from uv_tool.utils._logger import logger
from uv_tool.core.nodes import create_remesh_layout, create_uv_layout
from uv_tool.utils import open_export_folder, sanitize_name

class UVToolClass:
	def __init__(self, importPath, exportPath, remeshCheck=False, openFileCheck=False):
		"""
		Initialize the UVToolClass with paths, flags, and setup nodes.
		"""
		self.importPath = importPath  # Path to the input file
		self.exportPath = exportPath  # Path to the output file
		self.remeshCheck = remeshCheck  # Flag to enable/disable remeshing
		self.openFileCheck = openFileCheck  # Flag to open the export folder after processing
		self.assetName = os.path.basename(self.importPath).split(".")[0]  # Extract asset name from the import path

		# Create top-level Houdini nodes
		self.topNode = hou.node("/obj")  # Root object node in Houdini
		self.remeshGeoNode = self.topNode.createNode("geo")  # Node for remeshing
		self.uvGeoNode = self.topNode.createNode("geo")  # Node for UV layout

		self.setupNodes()  # Set up the necessary nodes
		self.cacheAndExport()  # Cache and export the processed data

	def setupNodes(self):
		"""
		Set up the remesh and UV layout nodes.
		"""
		logger.info(f"Setting up nodes for: {self.assetName}")

		# Create remesh layout nodes
		self.geoNull, self.geoFileCache = create_remesh_layout(
			self.remeshGeoNode,
			self.importPath,
			self.assetName,
			self.remeshCheck
		)
		logger.info(f"geoNull: {self.geoNull.path()}")  # Log the path of the remesh null node

		# Create UV layout nodes
		self.uvNull, self.uvFileCache, self.exportNode, self.uvVisualizer = create_uv_layout(
			self.uvGeoNode,
			self.geoNull.path(),
			self.assetName,
			self.exportPath
		)

	def cacheAndExport(self):
		"""
		Cache the remesh and UV layout data, then export the results.
		"""
		logger.info(f"Caching and exporting: {self.assetName}")
		start_time = time.time()  # Start timing the export process

		# Execute the remesh file cache node if it exists
		if self.geoFileCache:
			logger.info("Running remesh file cache")
			# Add logic to execute the remesh file cache if needed

		# Calculate elapsed time for the export process
		self.elapsed_time = time.time() - start_time
		logger.info(f"Export completed in {self.elapsed_time:.2f} seconds")
		logger.info(f"Exported to: {self.exportPath}")

		# Open the export folder if the flag is set
		if self.openFileCheck:
			open_export_folder(self.exportPath)

	def clearNodes(self):
		"""
		Clear all child nodes under the top-level Houdini node.
		"""
		logger.info(f"Clearing nodes")
		for node in self.topNode.children():
			node.destroy()  # Destroy each child node

	def toggleUVShell(self, toggle):
		"""
		Toggle the visibility of the UV shell visualizer.
		"""
		logger.info(f"Toggling UV shell: {toggle}")
		if toggle:
			# Enable UV shell visualization
			self.uvVisualizer.parm("visualize_islands").set(1)  # Show UV shells
			self.uvVisualizer.setDisplayFlag(True)  # Set display flag to True
		else:
			# Disable UV shell visualization
			self.uvVisualizer.parm("visualize_islands").set(0)  # Hide UV shells
			self.uvVisualizer.setDisplayFlag(False)

	