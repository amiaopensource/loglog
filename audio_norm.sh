#!/bin/bash

source `dirname "$0"`/bash_logging.config    #this sets the path for the config file, which should be nested next to the script
logDir=`pwd` # The log will be created at the working directory
logName='log'  # The script will be named log.log
logName+='.log'
logPath="$logDir/$logName"
logCreate $logPath
logOpen

logNewLine "Starting Audio Normalization Script"

filename=$(basename -- "${1}")
extension="${filename##*.}"
logNewLine "Detecting max volume for ${filename}......."
maxVolume=$(ffmpeg -hide_banner -i "${1}" -af "volumedetect" -vn -sn -dn -f null - 2>&1 | grep 'max_volume' | awk '{print $(NF-1)}')
logAddLine "Complete! Max volume is: ${maxVolume}"
volumeBoost="${maxVolume:1}"
audioCodec=$(ffprobe "${1}" 2>&1 >/dev/null |grep Stream.*Audio | sed -e 's/.*Audio: //' -e 's/[, ].*//')

logLog ffmpeg -hide_banner -loglevel error -i "${1}" -af "volume="${volumeBoost}"dB" -c:v copy -c:a ${audioCodec} -y "${1%.*}_normalized.${extension}"
