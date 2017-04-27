#!/bin/bash

#echo 'Benchmark Bash file opened'
start_time=$SECONDS
echo "[defaults]
host_key_checking = False" >> ~/ocr/code/ansiblescript/ansible.cfg
mkdir ~/ocr/accuracy
ansible-playbook -i ~/ocr/code/ansiblescript/inventory.txt ~/ocr/code/ansiblescript/benchmark.yml
finish_time=$SECONDS
duration="$((finish_time-start_time)) seconds"
echo "Benchmarking finished in "
echo $duration
echo "Accuracy in % = "
for file in ~/ocr/accuracy/*
do
  cat "$file"
done
