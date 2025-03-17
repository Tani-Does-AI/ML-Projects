import logging
import os
from datetime import datetime

# Create the log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the logs directory path
logs_dir = os.path.join(os.getcwd(), "logs")

# Create the logs directory if it doesn't exist
os.makedirs(logs_dir, exist_ok=True)

# Define the full log file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Corrected: Points to the file, not the directory
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,  # Ensure the logging level is set to INFO
    force=True,  # Override any existing logging configuration
)

if __name__ == "__main__":
    logging.info("Logging has started")