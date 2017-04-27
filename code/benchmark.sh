#!/bin/bash

#echo 'Benchmark Bash file opened'
echo "[defaults]
host_key_checking = False" >> ~/ocr/code/ansiblescript/ansible.cfg
mkdir ~/ocr/accuracy
ansible-playbook -i ~/ocr/code/ansiblescript/inventory.txt ~/ocr/code/ansiblescript/benchmark.yml
echo "Benchmarking finished"
echo "Accuracy in % = "
for file in ~/ocr/accuracy/*
do
  cat "$file"
done
