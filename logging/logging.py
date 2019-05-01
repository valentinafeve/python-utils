#! /usr/bin/env python3
import logging
#Logging documentation: https://www.python.org/dev/peps/pep-0282/
#https://docs.python.org/3/library/logging.html#logging.Formatter


# LEVEL NAMES= DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FORMAT = "%(levelname)s - %(asctime)s %(funcName)s : %(message)s"
logging.basicConfig(
	filename = "/home/valentina/Documents/alog.log", 
	level= logging.DEBUG,
	format= LOG_FORMAT, 
	)

logger=logging.getLogger()

logger.debug("This is a debug message")
logger.info("Just some useful info")
logger.warning("I'm sorry but I can't do that Vale")
logger.error("Did you just divide by zero?")
logger.critical("The complete world is been taken.")