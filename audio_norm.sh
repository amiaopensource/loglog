#!/bin/bash

IFS=$'\n'                                   #this is necessary to deal with spaces in filepath. (found a better way to do this so I commented it out to be safe)\
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
newLogLine "Testing for fileype (audio or video)"
logNewLine "Detecting max volume for ${filename}......."
maxVolume=$(ffmpeg -hide_banner -i "${1}" -af "volumedetect" -vn -sn -dn -f null - 2>&1 | grep 'max_volume' | awk '{print $(NF-1)}')
logAddToLine "Complete! Max volume is: ${maxVolume} dB"
volumeBoost="${maxVolume:1}"
audioCodec=$(ffprobe "${1}" 2>&1 >/dev/null |grep Stream.*Audio | sed -e 's/.*Audio: //' -e 's/[, ].*//')

if [[ -z "${format+x}" ]]; then #if the variable $format is unassigned, then run ffmpeg command w/out -c:v copy, otherwise include it
	logLog ffmpeg -hide_banner -loglevel error -i "${1}" -af "volume="${volumeBoost}"dB" -c:a ${audioCodec} -y "${1%.*}_normalized.${extension}"
else
	logLog ffmpeg -hide_banner -loglevel error -i "${1}" -af "volume="${volumeBoost}"dB" -c:v copy -c:a ${audioCodec} -y "${1%.*}_normalized.${extension}"
fi

