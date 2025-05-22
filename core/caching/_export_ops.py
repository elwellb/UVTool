# core/caching/_export_ops.py

import os
import tempfile
# import hou

from uv_tool.utils._logger import logger

def createTempDir():
	"""Create a temporary directory for caching."""
	logger.info("Creating temporary directory for caching")
	temp_dir = tempfile.gettempdir()
	cache_dir = os.path.join(temp_dir, "uv_tool_cache")

	if not os.path.exists(cache_dir):
		try:
			os.makedirs(cache_dir)
		except OSError as e:
			logger.error(f"Failed to create cache directory: {e}")
			return None

	logger.info(f"Cache directory created at: {cache_dir}")
	return temp_dir

def createFileCache(geoNode, inputNode, assetName):
	""" Create a file cache node."""
	logger.info(f"Creating file cache for: {assetName}")

	createTempDir() # Create a temporary directory for caching
	# Create a file cache node
	fileCacheNode = geoNode.createNode("filecache", assetName)
	fileCacheNode.setInput(0, inputNode)

	# Set the file cache parameters
	fileCacheNode.parm("basename").set(assetName+"_clean") # Set the base name for the cache
	fileCacheNode.parm("basedir").set("$TEMP/uv_tool_cache") # Set the base directory for the cache
	fileCacheNode.parm("trange").set(0) # Set to single frame
	fileCacheNode.parm("enableversion").set(0) # Disable versioning

	logger.info(f"File cache created: {fileCacheNode.name()}")

	return fileCacheNode

def createOutputNode(geoNode, inputNode):
	""" Create an output node."""
	logger.info("Creating output node")

	# Create an output node
	outputNode = geoNode.createNode("null", "MESH_OUT")
	outputNode.setInput(0, inputNode)
	outputNode.setDisplayFlag(True) # Set display flag to True

	logger.info(f"Output node created: {outputNode.name()}")

	return outputNode

def createExportNode(geoNode, inputNode, exportPath, assetName):
	""" Create an export node."""
	logger.info(f"Creating export node for: {exportPath}")

	# Create an export node
	exportNode = geoNode.createNode("rop_fbx", "outputROP")
	exportNode.setInput(0, inputNode)

	exportFile = os.path.join(exportPath, f"{assetName}_NewUV.fbx")
	exportNode.parm("sopoutput").set(exportFile) # Set the export file path


	logger.info(f"Export node created: {exportNode.name()}")

	return exportNode