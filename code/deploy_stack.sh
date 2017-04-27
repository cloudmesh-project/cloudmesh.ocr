#!/bin/bash

#echo 'Stack Bash file opened'
start_time=$SECONDS
echo "[defaults]
host_key_checking = False" >> ~/ocr/code/ansiblescript/ansible.cfg
ansible-playbook -i ~/ocr/code/ansiblescript/inventory.txt ~/ocr/code/ansiblescript/deploy_stack.yml
finish_time=$SECONDS
duration="$((finish_time-start_time)) seconds"
echo "Successfully deployed stack in "
echo $duration
