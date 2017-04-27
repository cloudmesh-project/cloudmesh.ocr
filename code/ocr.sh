#!/bin/bash

#echo 'Benchmark Bash file opened'
start_time=$SECONDS
echo "[defaults]
host_key_checking = False" >> ~/ocr/code/ansiblescript/ansible.cfg
mkdir ~/ocr/ocr_results
read -p "Enter the image URL: " url1
url_str="image_url: $url1"
echo $url_str >> ~/ocr/code/ansiblescript/roles/run_ocr/vars/main.yml
ansible-playbook -i ~/ocr/code/ansiblescript/inventory.txt ~/ocr/code/ansiblescript/ocr.yml
finish_time=$SECONDS
duration="$((finish_time-start_time)) seconds"
echo $duration
echo "Characters are: "
for file in ~/ocr/ocr_results/*
do
  cat "$file"
done
