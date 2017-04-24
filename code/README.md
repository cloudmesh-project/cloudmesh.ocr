README
========
 
This Ansible Galaxy project installs and runs an Optical Character Recognition
session on a portion of a database of 74k images. The session will run on a
cluster of multiple VM's in the Chameleon Cloud.

How to use
================

1- Clone the project in home/user/ocr.
```
$ cd ~
$ mkdir ocr
$ cd ocr
$ git init
$ git clone https://github.com/cloudmesh/cloudmesh.ocr.git

```
2- For running the project using cmd5, add the files deploy.py and benchmark.py
as an extension to your CMD5. These modules implement the commands deploy cluster,
deploy stack, and benchmark.
However, an easier and less error-prone way to run the project is to simply run
the following bash files:

deploy_cluster_bash: Creates a cluster of multiple nodes (the number can be
changed easily in the file) on Chameleon Cloud. E.g.:

```
$ bash ~/ocr/code/deploy_cluster_bash

```
deploy_stack_bash: Installs the necessary packages on the cluster nodes.

benchmark_bash: Runs the OCR on the cluster nodes.

The results will be saved in ocr/results.