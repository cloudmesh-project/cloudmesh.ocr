#!/bin/bash

#echo 'Cluster Bash file opened'
read -p "Enter number of nodes: " nnode
start_time=$SECONDS
cm cloud activate chameleon
cm default cloud=chameleon
cm cluster define -n cluster_ocr -c $nnode
cm cluster allocate 
cm cluster inventory -o ~/ocr/code/ansiblescript/inventory.txt
finish_time=$SECONDS
duration="$((finish_time-start_time)) seconds"
echo 'Successfully deployed cluster of '$nnode' nodes on Chameleon Cloud in'
echo $duration
