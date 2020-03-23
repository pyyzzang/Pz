 #!/bin/sh
SERVER="9091 --auth pi:cndwn5069()"
TORRENTLIST=`transmission-remote $SERVER --list | sed -e '1d;$d;s/^ *//' | cut --only-delimited --delimiter=" " --fields=1`
for TORRENTID in $TORRENTLIST
do
    
done 
 
 