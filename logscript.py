#!/usr/bin/env python
# -*- coding: utf-8 -*-

###   Script Configuration Section

import logging          # This loads the "logging" module, which handles logging very simply
import os               # This loads the "os" module, useful for dealing with filepaths
import tempfile         # This loads the "tempfile" module, a nice cross-platform way to deal with temp directories
import subprocess
import platform
from datetime import datetime   # This lades the datetime module, used for getting dates and timestamps

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

FORMAT = '%(asctime)s - %(levelname)s: %(message)s' #Timestamp - Loglevel: Message
#FORMAT = '%(asctime)s - %(message)s'               #Timestamp - Message
#FORMAT = '%(levelname)s: %(message)s'              #Loglevel: Message
# more format atrributes can be found here: https://docs.python.org/3/library/logging.html#logrecord-attributes

logging.basicConfig(filename=logPath, encoding='utf-8', level=logging.DEBUG, format=FORMAT)    # Creates the Log

#The following section is a cross-platform way to open the log
if platform.system() == 'Darwin':       # macOS
    subprocess.call(('open', logPath))
elif platform.system() == 'Windows':    # Windows
    os.startfile(logPath)
else:                                   # linux variants
    subprocess.call(('xdg-open', filepath))

logging.debug('This is a debug message')
logging.info('This is a standard message')
logging.warning('This is a warning')
logging.error('This is an error')
logging.critical('This is a critical message')
