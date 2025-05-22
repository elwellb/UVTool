#utils/_logger.py

import logging
import os
from datetime import datetime

# Create a directory for logs if it doesn't exist
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "..", "..", "logs")
today = datetime.now().strftime("%Y-%m-%d")
DAILY_LOG_DIR = os.path.join(LOG_DIR, today)
os.makedirs(DAILY_LOG_DIR, exist_ok=True)

# Generate a timestamped log file name
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = os.path.join(LOG_DIR, f"log_{timestamp}.log")

# Set up logging
logging.basicConfig(
	level=logging.INFO,
	format="%(asctime)s - %(levelname)s - %(message)s",
	handlers=[
		logging.FileHandler(log_file, mode="a"),
		logging.StreamHandler()
	]
)

logger = logging.getLogger("uv_tool_log")