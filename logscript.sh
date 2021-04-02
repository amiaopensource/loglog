#!/bin/bash

###   Script Configuration Section

IFS=$'\n'                                    #this is necessary to deal with spaces in filepath
source `dirname "$0"`/bash_logging.config    #this sets the path for the config file, which should be nested next to the script

###   Log Configuration Section
##    This is where you select the log directory. Uncomment the one you want. Uncomment the line you want to use. 

logDir=`pwd` # The log will be created at the working directory
#logDir='/tmp' # The log will be created in the temporary directory
#logDir="ENTER YOUR OWN PATH HERE" # The log will be created at an arbitrary location

##    This is where you name the log. Uncomment the line you want to use.

logName='log'  # The script will be named log.log
#logName=`basename "$0"`  #the log will be named after the name of the script
#logName=`date '+%Y-%m-%d'`  #the log will be named after the Date (YYYY-MM-DD)
#logName='ENTER YOUR OWN NAME HERE'  #the log will be named anything you want

logName+='.log'
logPath=$logDir/$logName

###   Log Implementation Section
##    The following commands create and open the log

logCreate $logPath
logOpen

##    The following commands add lines to the log

logNewLine "Text on a new line in the log goes"
logAddLine "......Text added to the last line goes here"
