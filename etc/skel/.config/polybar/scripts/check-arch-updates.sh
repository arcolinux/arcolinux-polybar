#!/bin/sh
#source https://github.com/x70b1/polybar-scripts
#source https://github.com/polybar/polybar-scripts

if ! updates_arch1=$(checkupdates 2> /dev/null | wc -l ); then
    updates_arch1=0
fi

if [ $updates_arch1 -gt 0 ]; then
    echo $updates_arch1
else
    echo "0"
fi
