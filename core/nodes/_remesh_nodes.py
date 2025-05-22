# core/nodes/_remesh_nodes.py

# import os
# import hou

from uv_tool.utils._logger import logger
from uv_tool.core.caching._export_ops import createFileCache, createOutputNode

def create_remesh_layout(remeshNode, importFile, assetName, remeshCheck):
	''' Create the remesh layout for the given node and import file. '''
	logger.info(f"Creating remesh layout for: {assetName}")

	importNode = createImportNode(remeshNode, importFile) # Create the import node
	attribDelete = createAttribDeleteNode(remeshNode, importNode) # Create the attribute delete node
	deleteUCX = createDeleteUCXNode(remeshNode, attribDelete) # Create the delete UCX node
	cleanNode = createCleanNode(remeshNode, deleteUCX) # Create the clean node
	polyReduce = createPolyReduceNode(remeshNode, cleanNode) # Create the poly reduce node
	switchNode = createSwitchNode(remeshNode, deleteUCX, polyReduce, remeshCheck) # Create the switch node
	fileCache = createFileCache(remeshNode, switchNode, assetName) # Create the file cache node
	nullNode = createOutputNode(remeshNode, fileCache) # Create the null node

	logger.info(f"Remesh layout created for: {assetName}")
	return nullNode, fileCache # Return the null node

def createImportNode(geoNode, importFile):
	''' Create the import node for the given node and import file. '''

	logger.info(f"Creating import node")

	importNode = geoNode.createNode("file", "importFile") # Create a file node
	importNode.parm("file").set(importFile) # Set the file path to the import file

	return importNode

def createAttribDeleteNode(geoNode, inputNode):
	''' Create the attribute delete node for the given node and import node. '''

	logger.info("Creating attribute delete node")

	attribDelete = geoNode.createNode("attribdelete", "attribDelete") # Create an attribute delete node
	attribDelete.setInput(0, inputNode) # Set the input to the import node

	attribDelete.parm("vtxdel").set("uv uv2") # Delete UVs

	return attribDelete

def createDeleteUCXNode(geoNode, inputNode):
	''' Create the delete UCX node for the given node and attrib node. '''

	logger.info("Creating delete UCX node")

	deleteUCX = geoNode.createNode("blast", "deleteUCX") # Create a delete node
	deleteUCX.setInput(0, inputNode) # Set the input to the attrib delete node

	deleteUCX.parm("group").set("@name=UCX") # Delete UCX collision

	return deleteUCX

def createCleanNode(geoNode, inputNode):
	''' Create the clean node for the given node and delete node. '''

	logger.info("Creating clean node")

	cleanNode = geoNode.createNode("clean", "clean") # Create a clean node
	cleanNode.setInput(0, inputNode) # Set the input to the delete UCX node

	return cleanNode

def createPolyReduceNode(geoNode, inputNode):
	''' Create the poly reduce node for the given node and clean node. '''

	logger.info("Creating poly reduce node")

	polyReduce = geoNode.createNode("polyreduce", "polyReduce") # Create a poly reduce node
	polyReduce.setInput(0, inputNode) # Set the input to the clean node

	polyReduce.parm("target").set(2) # Set target to Output Polygon Count
	polyReduce.parm("finalcount").set(1000) # Set final count to 1000

	return polyReduce

def createSwitchNode(geoNode, optionOne, optionTwo, remeshCheck):
	''' Create the switch node for the given nodes'''

	logger.info("Creating switch node")
	
	switchNode = geoNode.createNode("switch", "switch") # Create a switch node
	switchNode.setInput(0, optionOne) # Set the input to the poly reduce node
	switchNode.setInput(1, optionTwo) # Set the input to the delete UCX node
	switchNode.parm("input").set(0) # Set the input to option one

	if remeshCheck:
		switchNode.parm("input").set(1) # Set the input to option two (poly reduce)

	return switchNode