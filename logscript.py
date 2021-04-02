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
##    This is where you select the log directory. Uncomment the one you want. Uncomment the line you want to use.

logDir = os.getcwd()               # The log will be created at the working directory
#logDir = tempfile.gettempdir()      # The log will be created in the OS's temp directory
#logDir="ENTER_YOUR_OWN_PATH_HERE"  # The log will be created at an arbitrary location

##    This is where you name the log. Uncomment the line you want to use.

logName = 'log'                                 # The script will be named log.log
#logName = os.path.basename(__file__)            # The log will be named after the name of the script
#logName = datetime.today().strftime('%Y-%m-%d') # The log will be named after the Date (YYYY-MM-DD)
#logName = 'ENTER_YOUR_OWN_NAME_HERE'             # The log will be named anything you wants

logPath = logDir + "/" + logName + ".log"         # This creates the full log path based off the selected options

# NEED A TEST TO MAKE SURE THE FILE CAN EXIST

logging.basicConfig(filename=logPath, encoding='utf-8', level=logging.DEBUG)    # Creates the Log

#The following section is a cross-platform way to open the log
if platform.system() == 'Darwin':       # macOS
    subprocess.call(('open', logPath))
elif platform.system() == 'Windows':    # Windows
    os.startfile(logPath)
else:                                   # linux variants
    subprocess.call(('xdg-open', filepath))

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
