# package for logging
import logging
from logging.handlers import SysLogHandler

def main_1_basic() -> None:
    
    # Minimum configuration for the logging.
    logging.basicConfig(level=logging.WARNING)

    # To disable logging
    #logging.disable()
    #logging.disable(level=logging.DEBUG)

    # Five levels of severity for logging. 

    logging.debug("This is a debug message")
    logging.info("This is a inf message")

    # All the statements defined with a severity above the configured level will be logged. 
    # In this case the level configured is WARNING. Hence in this case all these statements will be
    # logged
    logging.warning("This is a warning message")
    logging.error("This is a error message")
    logging.critical("This is a critical message")

def main_2_more_config() -> None:
    
    logging.basicConfig(level=logging.WARNING,
                        format = "%(asctime)s %(levelname)s %(message)s",   # logrecord-attributes on Python website
                        datefmt="%Y-%m-%d %H:%M:%S"
                        )

    logging.debug("This is a debug message")    # Lowest Level
    logging.info("This is a inf message")

    logging.warning("This is a warning message")
    logging.error("This is a error message")
    logging.critical("This is a critical message")  # Highest Level

def main_3_file_config() -> None:
    
    logging.basicConfig(level=logging.WARNING,
                        format = "%(asctime)s %(levelname)s %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S",
                        filename="basic.log",
                        filemode='w'    # w = write, lod file is recreated and previous data is erased. 
                                        # Default mode = a for append
                        )   

    logging.debug("This is a debug message")
    logging.info("This is a inf message")

    logging.warning("This is a warning message")
    logging.error("This is a error message")
    logging.critical("This is a critical message")    

# papertrailapp is a log management service provider
def main_4_papertrail_config() -> None:
    
    PAPERTRAIL_HOST = "logs.papertrailapp.com"
    PAPERTRAIL_PORT = 37554

    # Create a logger object. The name here is helpful in identifying where the log is originating from
    logger = logging.getLogger("logging_to_console")

    # Configure the logger object
    logger.setLevel(logging.DEBUG)

    # Need a handler to send the logs to a logging service like Splunk, Papertrail, etc
    handler = SysLogHandler(address=(PAPERTRAIL_HOST, PAPERTRAIL_PORT))
    
    # Add the handler to the logger. We can add multiple handlers to the logger for sending logs to 
    # multiple destinations. For example, we can add a file handler as well to send the logs to file and
    # papertrail at the same time
    logger.addHandler(handler)

    logger.debug("This is a debug message")
    logger.info("This is a inf message")

    logger.warning("This is a warning message")
    logger.error("This is a error message")
    logger.critical("This is a critical message")        

if __name__ == "__main__":
    #main_1_basic()
    #main_2_more_config()
    #main_3_file_config()
    main_4_papertrail_config()