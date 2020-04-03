#!/bin/sh
SERVER="9091 --auth pi:cndwn5069()"
TORRENTLIST=`transmission-remote $SERVER --list | sed -e '1d;$d;s/^ *//' | cut --only-delimited --delimiter=" " --fields=1`
LOG_FILE="Bach.log"
for TORRENTID in $TORRENTLIST
do
    DL_COMPLETED=`transmission-remote $SERVER --torrent $TORRENTID --info | grep "Percent Done: 100%"`
    STATE_STOPPED=`transmission-remote $SERVER --torrent $TORRENTID --info | grep "State: Seeding\|Stopped\|Finished\|Idle"`
    if [ "$DL_COMPLETED" ] && [ "$STATE_STOPPED" ]; then

        CompleteMagnet=`transmission-remote $SERVER --torrent $TORRENTID --info | grep -e Magnet:`
        if [ "$CompleteMagnet" ]; then
            cd "/home/pi/Pz/HomePage/HomePage/TransmissionSH"
            SHELL_PATH=`pwd -P`
            python3 "UpdateThumbnail.py" $CompleteMagnet
        fi
        
        transmission-remote $SERVER --torrent $TORRENTID --remove
    fi
done 

