# main.py

import hou
import os
import sys

TOOL_DIR = os.path.dirname(__file__)
if TOOL_DIR not in sys.path:
	sys.path.append(TOOL_DIR)

from uv_tool.ui._qt_ui_controller import myQtUIClass

def main():
	ui = myQtUIClass()  # Create an instance of the UI class
	ui.show()
	return ui

if __name__ == "__main__" or hou.isUIAvailable():
	main()