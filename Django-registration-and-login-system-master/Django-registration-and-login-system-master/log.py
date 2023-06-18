import logging
# Configure the logging settings
logging.basicConfig(
    filename='app.log',  # Specify the file name for the log file
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
# Start logging messages
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")