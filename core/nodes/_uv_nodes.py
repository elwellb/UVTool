# core/nodes/_uv_nodes.py

# import os
# import hou

from uv_tool.utils._logger import logger
from uv_tool.core.caching._export_ops import (
	createFileCache,
	createOutputNode,
	createExportNode
)

def create_uv_layout(geoNode, importFile, assetName, exportPath):
	''' Create the UV layout for the given node and import file. '''
	logger.info(f"Creating UV layout for: {assetName}")

	objMergeNode = createMergeNode(geoNode, importFile) # Create the import node
	measureNode = createMeasureNode(geoNode, objMergeNode) # Create the measure node
	groupNode = createGroupNode(geoNode, measureNode) # Create the group node
	uvFlattenNode = createUVFlattenNode(geoNode, groupNode) # Create the UV flatten node
	uvUnwrapNode = createUnwrapNode(geoNode, uvFlattenNode) # Create the UV unwrap node
	uvLayoutNode = createLayoutNode(geoNode, uvUnwrapNode) # Create the UV layout node
	uvVisualizer = createVisualizerNode(geoNode, uvLayoutNode) # Create the UV visualizer node
	uvFileCache = createFileCache(geoNode, uvVisualizer, assetName) # Create the file cache node
	nullNode = createOutputNode(geoNode, uvFileCache) # Create the null node
	exportNode = createExportNode(geoNode, nullNode, exportPath, assetName) # Create the export node

	logger.info(f"UV layout created for: {assetName}")

	return nullNode, uvFileCache, exportNode, uvVisualizer # Return the null node

def createMergeNode(geoNode, importFile):
	''' Create the import node for the given node and import file. '''
	logger.info(f"Creating UV merge node")

	importNode = geoNode.createNode("object_merge", "importRemesh") # Create a file node
	importNode.parm("objpath1").set(importFile) # Set the file path to the import file

	return importNode

def createMeasureNode(geoNode, inputNode):
	''' Create the measure node for the given node and import node. '''
	logger.info("Creating measure node")

	measureNode = geoNode.createNode("measure", "measure") # Create a measure node
	measureNode.setInput(0, inputNode) # Set the input to the import node

	measureNode.parm("measure").set(4) # Set the measure to curvature
	measureNode.parm("attribname").set("curvature") # Set the attribute name to curvature
	measureNode.parm("grouptype").set(0) # Set group type to points

	return measureNode

def createGroupNode(geoNode, inputNode):
	''' Create the group node for the given node and measure node. '''
	logger.info("Creating group node")

	groupNode = geoNode.createNode("groupcreate", "group") # Create a group node
	groupNode.setInput(0, inputNode) # Set the input to the measure node

	groupNode.parm("groupname").set("sharp_edges") # Set the group name to curvature
	groupNode.parm("grouptype").set(2) # Set group type to edges
	groupNode.parm("groupedges").set(1) # Set group edges to on
	groupNode.parm("dominedgeangle").set(1) # Turn on min edge angle
	groupNode.parm("domaxedgeangle").set(1) # Turn on max edge angle
	groupNode.parm("minedgeangle").set(80) # Set min edge angle to 80
	groupNode.parm("maxedgeangle").set(110) # Set max edge angle to 100
	groupNode.parm("unshared").set(1) # Set unshared to on
	groupNode.parm("groupbase").set(0)

	return groupNode

def createUVFlattenNode(geoNode, inputNode):
	''' Create the UV flatten node for the given node and group node. '''
	logger.info("Creating UV flatten node")

	uvFlattenNode = geoNode.createNode("uvflatten", "uvFlatten") # Create a UV flatten node
	uvFlattenNode.setInput(0, inputNode) # Set the input to the group node

	uvFlattenNode.parm("seamgroup").set("sharp_edges") # Set the seam group to curvature
	uvFlattenNode.parm("uvattrib").set("uv") # Set the UV attribute to uv
	uvFlattenNode.parm("keepexistingseams").set(1) # Set keep seams to on

	return uvFlattenNode

def createUnwrapNode(geoNode, inputNode):
	''' Create the UV unwrap node for the given node and flatten node. '''
	logger.info("Creating UV unwrap node")

	uvUnwrapNode = geoNode.createNode("uvunwrap", "uvUnwrap") # Create a UV unwrap node
	uvUnwrapNode.setInput(0, inputNode) # Set the input to the flatten node

	uvUnwrapNode.parm("uvattrib").set("uv") # Set the UV attribute to uv
	uvUnwrapNode.parm("spacing").set(1) # Set spacing to 1

	return uvUnwrapNode

def createLayoutNode(geoNode, inputNode):
	''' Create the UV layout node for the given node and unwrap node. '''
	logger.info("Creating UV layout node")

	uvLayoutNode = geoNode.createNode("uvlayout", "uvLayout") # Create a UV layout node
	uvLayoutNode.setInput(0, inputNode) # Set the input to the unwrap node

	uvLayoutNode.parm("uvattrib").set("uv") # Set the UV attribute to uv
	uvLayoutNode.parm("packbetween").set(1) # Set pack between to on
	uvLayoutNode.parm("padding").set(5) # Set padding to 5
	uvLayoutNode.parm("paddingboundary").set(1) # Set padding boundary to on
	uvLayoutNode.parm("axisalignislands").set(0) # Set axis align islands to off
	uvLayoutNode.parm("stackislands").set(1) # Set stack islands to on
	uvLayoutNode.parm("invertedoverlays").set(1) # Set inverted overlays to on

	return uvLayoutNode

def createVisualizerNode(geoNode, inputNode):
	''' Create the UV visualizer node for the given node and layout node. '''
	logger.info("Creating UV visualizer node")

	uvVisualizer = geoNode.createNode("visualize_uvs", "uvVisualizer") # Create a UV visualizer node
	uvVisualizer.setInput(0, inputNode) # Set the input to the layout node

	return uvVisualizer