#!/bin/bash

#echo 'Cluster Bash file opened'
start_time=$SECONDS
cm cloud activate chameleon
cm default cloud chameleon
cm cluster define -n cluster_ocr -c 2
cm cluster allocate 
cm cluster inventory -o ~/ocr/code/ansiblescript/inventory.txt
finish_time=$SECONDS
duration="$((finish_time-start_time)) seconds"
echo 'Successfully deployed cluster of 2 nodes on Chameleon Cloud in'
echo $duration
