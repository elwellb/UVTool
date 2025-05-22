# utils/_file_utils.py

import os
import re
import subprocess

from uv_tool.utils._logger import logger

def open_export_folder(folder_path):
	"""Open the export folder in the file explorer."""
	logger.info(f"Opening export folder: {folder_path}")
	
	if os.path.exists(folder_path):
		os.startfile(folder_path)  # For Windows

def sanitize_name(name):
	"""Sanitize the name to be a valid file name."""
	logger.info(f"Sanitizing name: {name}")

	sanitizedName = re.sub(r'\W+', "_", name)

	if sanitizedName and sanitizedName[0].isdigit():
		sanitizedName = f"_{sanitizedName}"
		
	return sanitizedName