#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "Usage: run.sh [num_of_bots]"
    exit 1
fi

for i in $(seq $1)
do 
    echo "Launching $i"
    python ayai-bot.py &
    sleep 0.25
done

echo "Kill python in order to stop the bots"
