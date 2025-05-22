#ui/_qt_ui_controller.py

import os
import hou
from PySide2.QtCore import QFile, QIODevice, QStandardPaths, Qt
from PySide2.QtWidgets import QWidget, QFileDialog, QMessageBox
from PySide2.QtUiTools import QUiLoader

from uv_tool.core import UVToolClass
from uv_tool.utils._logger import logger

class myQtUIClass(QWidget):
	''' This class controls all othe interface between the GUI and Houdini'''
	def __init__(self):
		'''Constructor for your GUI class'''
		super(myQtUIClass, self).__init__(hou.qt.mainWindow())    # Initialize the class as a typical QWidget class                     
		self.setWindowFlags(Qt.Window)
		self.importPath = None
		self.exportPath = None
		self.initUI()
		
	def initUI(self):
		''' Create the GUI and pass off the interface bindings '''
		myFolder = os.path.dirname(__file__)    # Get the path to the current file
		#currentDir = os.path.abspath(os.path.dirname(__file__), "..", "ui")    # Get the unbiased path to your UI file
		uiFile = QFile(os.path.join(myFolder, "_uiForm.ui"))        # A QfILE IS A SPECIAL qTio DEVICE for handling file streams

		if not uiFile.exists():                                # Check to see if the file exists
			raise RuntimeError(f"UI File Not Found: {uiFile.fileName()}")            # If not, raise an error

		if not uiFile.open(QIODevice.ReadOnly):                    # Open the stream as read only
			raise RuntimeError(f"Cannot open file {uiFile.fileName()}")            # If not, raise an error
		loader = QUiLoader()								# A loader is a special device in QtUiTools
		self.ui = loader.load(uiFile, parentWidget=self)   # Convert the UI file from xml to python and send the stream to the Class' UI
		uiFile.close()                                     # Close the File
		
		if self.ui is None:								# If the UI is empty
			raise RuntimeError("Failed to load UI file. Check UI structure")
		
		self.setWindowTitle("Remesh and UV Tool")
		self.bindMyButtons()                               # Perform the rest of the interface configuration


	def bindMyButtons(self):
		''' Bind the buttons to the functions '''
		self.ui.importBrowse.clicked.connect(self.fileBrowseDialogInput)   
		self.ui.exportBrowse.clicked.connect(self.fileBrowseDialogOutput)
		self.ui.exportCheck.stateChanged.connect(self.checkExport)
		self.ui.fixAssetPush.clicked.connect(self.fixAsset)
		self.ui.clearButton.clicked.connect(self.clearEverything)
		self.ui.uvShellCheck.stateChanged.connect(self.toggleUVShell)


	def fileBrowseDialogInput(self):
		''' Open a file dialog and return the selected directory '''
		tempFolder = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
		dialog = QFileDialog(self, "Select an FBX or OBJ File", tempFolder)
		dialog.setFileMode(QFileDialog.ExistingFile)    # Set the dialog to only show files
		dialog.setNameFilter("FBX/OBJ Files (*.fbx *.obj)")

		    
		if dialog.exec_():										# Execute the dialog
			self.ui.importFileLabel.clear()							# Clear the label
			self.filePaths = []
			selectedFile = dialog.selectedFiles()				# Get the selected files
			if selectedFile:  									# If the selected file is not empty
				baseFile = os.path.basename(selectedFile[0]) 	# Get the base file name
				self.ui.importFileLabel.setText(baseFile) 		# Set the label to the base file name
				self.importDir = os.path.dirname(selectedFile[0]) 	# Get the directory of the selected file
				self.importPath = selectedFile[0] 			# Set the import path to the selected file

		if self.ui.importFileLabel.text() == None: 			# If the label is empty
			self.ui.exportBrowse.setEnabled(False)  		# Disable the export browse button
			self.ui.exportCheck.setEnabled(False) 			# Disable the export check box
		else:
			self.ui.exportCheck.setEnabled(True) 
			self.ui.openFileCheck.setEnabled(True)
			self.exportPath = self.importDir
			baseFolder = os.path.basename(self.importDir) 	# Get the base folder name
			self.ui.exportLabel.setText(f"/{baseFolder}") 	# Set the label to the base folder name
			self.ui.fixAssetPush.setEnabled(True)

	def fileBrowseDialogOutput(self):
		''' Open a file dialog and return the selected directory '''
		#print("File Browse Pressed")
		docFolder = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation) # Get the documents folder path
		selectedFolder = QFileDialog.getExistingDirectory(self, "Select Export Location", docFolder, QFileDialog.ShowDirsOnly) # Show only directories
		    
		if selectedFolder:										# Execute the dialog
			self.ui.exportLabel.clear()							# Clear the label
			baseFolder = os.path.basename(selectedFolder)
			self.exportLabel.setText(f"/{baseFolder}")
			self.exportPath = selectedFolder



	def checkExport(self): 
		if self.ui.exportCheck.isChecked():
			self.ui.exportBrowse.setEnabled(False)
			self.ui.exportLabel.setEnabled(False)
			baseFolder = os.path.basename(self.importDir) # Get the base folder name
			self.exportLabel.setText(f"/{baseFolder}") # Set the label to the base folder name
			self.exportPath = self.importDir # Set the export path to the import path
			logger.info(f"Export path set to: {self.exportPath}")
		else:
			self.ui.exportBrowse.setEnabled(True)
			self.ui.exportLabel.setEnabled(True)

	def fixAsset(self):
		''' Call the remeshandUVClass to create the nodes and export the geometry '''
		#print("Fix Asset Pressed")
		if self.importPath is None:
			QMessageBox.critical(None, "Error", "Both an import and export path must be selected.") # If the import path is empty, show an error message

		else:
			self.assetFixer = UVToolClass(self.importPath, self.exportPath, self.ui.remeshCheck.isChecked(), self.ui.openFileCheck.isChecked()) 
			self.ui.clearButton.setEnabled(True)
			self.ui.uvShellCheck.setEnabled(True)
			self.ui.timeLabel.setText(f"Successfully processed in {self.assetFixer.elapsed_time:.2f} seconds") # Set the time label to the elapsed time

	def clearEverything(self): 
		''' Clear all the nodes '''
		if self.assetFixer: 
			self.assetFixer.clearNodes()


	def toggleUVShell(self):
		if self.assetFixer:
			self.assetFixer.toggleUVShell(self.ui.uvShellCheck.isChecked())
