#!/bin/bash

#echo 'Stack Bash file opened'
echo "[defaults]
host_key_checking = False" >> ~/ocr/code/ansiblescript/ansible.cfg
ansible-playbook -i ~/ocr/code/ansiblescript/inventory.txt ~/ocr/code/ansiblescript/deploy_stack.yml
echo "Successfully deployed stack"
