#!/bin/sh

# https://github.com/jaagr/polybar/wiki/User-contributed-modules

#The command for starting compton
#always keep the -b argument!

if pgrep -x "compton" > /dev/null
then
	killall compton
else
	compton -b --config ~/.config/i3/compton.conf
fi
