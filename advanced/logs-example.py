import logging

# Configure the logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the minimum level of messages to capture
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log',   # Log messages will be written to this file
    filemode='w'          # Overwrite the log file each time the script runs
)

# Create a logger
logger = logging.getLogger('MyAppLogger')

# Log messages of various severity levels
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")