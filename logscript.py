#!/usr/bin/env python
# -*- coding: utf-8 -*-

###   Script Configuration Section

import logging          # This loads the "logging" module, which handles logging very simply
import os               # This loads the "os" module, useful for dealing with filepaths
import tempfile         # This loads the "tempfile" module, a nice cross-platform way to deal with temp directories
import subprocess
import sys
import platform
import argparse         # This loads the "argparse" module, used for parsing input arguments which allows us to have a verbose mode
from datetime import datetime   # This lades the datetime module, used for getting dates and timestamps

### Gather our code in a main() function
def main():

### Collect input arguments from the user. For now we just use this to run the script in verbose and debug mode
    parser = argparse.ArgumentParser(description="This is a template script for using logging in Python")
    parser.add_argument('-v', '--verbose', action='count', default=0,help="Defines verbose level for standard out (stdout). v = warning, vv = info, vvv = debug")
    parser.add_argument('-d', '--Debug',dest='d',action='store_true',default=False,help="turns on Debug mode, which send all DEBUG level (and below) messages to the log. By default logging is set to INFO level")
    args = parser.parse_args()

##  This turns on the debug mode if requested by user. Set log_level variable used later when instantiating the log
    if args.d:
        log_level=logging.DEBUG
    else:
        log_level=logging.INFO

##  This portion handles the verbosity levels for the standard out, taken from: https://stackoverflow.com/questions/14097061/easier-way-to-enable-verbose-logging
##  Uncomment the appropriate line

    levels = [logging.CRITICAL, logging.ERROR, logging.WARNING, logging.INFO, logging.DEBUG]     #The default verbosity level for stdout is CRITICAL
    #levels = [logging.ERROR, logging.WARNING, logging.INFO, logging.DEBUG]                       #The default verbosity level for stdout is ERROR
    #levels = [ogging.WARNING, logging.INFO, logging.DEBUG]                                       #The default verbosity level for stdout is WARNING
    #levels = [logging.INFO, logging.DEBUG]                                                       #The default verbosity level for stdout is INFO
    #levels = [logging.DEBUG]                                                                     #The default verbosity level for stdout is DEBUG
    verbose_level = levels[min(len(levels)-1,args.verbose)]

###   Log Configuration Section
##    This is where the log directory is set. Uncomment the line you want to use.

    logDir = os.getcwd()               # The log will be created at the working directory
    #logDir = tempfile.gettempdir()      # The log will be created in the OS's temp directory
    #logDir="ENTER_YOUR_OWN_PATH_HERE"  # The log will be created at an arbitrary location

##    This is where the log name is set. Uncomment the line you want to use.

    logName = 'log'                                 # The script will be named log.log
    #logName = os.path.basename(__file__)            # The log will be named after the name of the script
    #logName = datetime.today().strftime('%Y-%m-%d') # The log will be named after the Date (YYYY-MM-DD)
    #logName = 'ENTER_YOUR_OWN_NAME_HERE'             # The log will be named anything you wants

    logPath = logDir + "/" + logName + ".log"         # This creates the full log path based off the selected options

##      This is where the the log output format is set. Uncomment the line you want to use.

    LOG_FORMAT = '%(asctime)s - %(levelname)s: %(message)s' #Timestamp - Loglevel: Message
    #LOG_FORMAT = '%(asctime)s - %(message)s'               #Timestamp - Message
    #LOG_FORMAT = '%(levelname)s: %(message)s'              #Loglevel: Message
    #LOG_FORMAT = '%(message)s'              #Message
    # more format atrributes can be found here: https://docs.python.org/3/library/logging.html#logrecord-attributes

    #Get the root logger
    logger = logging.getLogger()
    logging.basicConfig(filename=logPath, encoding='utf-8', level=log_level, format=LOG_FORMAT)    # Creates the Log

###     This section allows us to output the logging messages to that standard out (stdout)
##      This is where the stdout message format is selected

    #STDOUT_FORMAT = '%(asctime)s - %(levelname)s: %(message)s' #Timestamp - Loglevel: Message
    #STDOUT_FORMAT = '%(asctime)s - %(message)s'               #Timestamp - Message
    #STDOUT_FORMAT = '%(levelname)s: %(message)s'              #Loglevel: Message
    STDOUT_FORMAT = '%(message)s'                             #Message

##      This portion creates the handler that sends logging info to standard out
##      More info about handlers can be found here: https://docs.python.org/3/library/logging.handlers.html
##      This portion taken from here: https://stackoverflow.com/questions/2302315/how-can-info-and-debug-logging-message-be-sent-to-stdout-and-higher-level-messag

    logging_handler_out = logging.StreamHandler(sys.stdout)
    logging_handler_out.setLevel(verbose_level)
    logging_handler_out.setFormatter(logging.Formatter(STDOUT_FORMAT))
    logger.addHandler(logging_handler_out)


    logging.critical('========Starting Script========')


#The following section is a cross-platform way to open the log
    if platform.system() == 'Darwin':       # macOS
        subprocess.call(('open', logPath))
    elif platform.system() == 'Windows':    # Windows
        os.startfile(logPath)
    else:                                   # linux variants
        subprocess.call(('xdg-open', filepath))

###     Now that the log is setup we can send some messages to it!

    logging.debug('This is a debug message')
    logging.info('This is a standard message')
    logging.warning('This is a warning')
    logging.error('This is an error')
    logging.critical('This is a critical message')

###     We can also send messages to the log using Exceptions
##      This is an example of using logger.exception to send an ERROR level message to the log along with a full stack trace. From: https://www.loggly.com/blog/exceptional-logging-of-exceptions-in-python/
##      Try running with a single -v level of verbosity and you will see the traceback error in your standard out!

    try:
        x = 10 * (1/0)
    except Exception:
        logging.exception("Fatal error in main loop")

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
