#!/bin/sh
#source https://github.com/x70b1/polybar-scripts
#source https://github.com/polybar/polybar-scripts

if ! updates_arch2=$(checkupdates 2> /dev/null | wc -l ); then
    updates_arch2=0
fi

if ! updates_aur2=$(yay -Qum 2> /dev/null | wc -l); then
    updates_aur2=0
fi

updates2=$(("$updates_arch2" + "$updates_aur2"))

if [ $updates2 -gt 0 ]; then
    echo $updates2
else
    echo "0"
fi
