#!/bin/bash

#echo 'Cluster Bash file opened'
cm cloud activate chameleon
cm default cloud chameleon
cm cluster define -n cluster_ocr -c 2
cm cluster allocate 
cm cluster inventory -o 'ocr/code/ansiblescript/inventory.txt'
echo 'Successfully deployed cluster of 2 nodes on Chameleon Cloud'
