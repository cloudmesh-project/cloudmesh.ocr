from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
#import subprocess
#import os.path as op
import sys, os




class DeployCommand(PluginCommand):

    @command
    def do_deploy(self, args, arguments):
        """
        ::

          Usage:
                deploy cluster
                deploy stack

          If called with cluster, this command deploys a virtual cluster of
	  3 nodes on Chameleon Cloud.
	  It saves the inventory file in path: ./code/ansiblescript/inventory.txt

	  If called with stack, it runs an Ansible playbook that installs the
	  packages needed for running OCR on the hosts specified in inventory.txt

          Options:
              -f      specify the file
        """
	#dir_path = op.dirname(op.realpath('__file__'))
	if arguments.cluster:
		#print("Cluster Selected")
		#subprocess.call("cd ~/ocr")
		#subprocess.call("pwd")
		os.system('~/ocr/code/deploy_cluster_bash')
		#subprocess.call(['~/ocr/deploy_cluster_bash'])
	elif arguments.stack:
		#print("Stack selected")
		os.system('~/ocr/code/deploy_stack_bash')
		#subprocess.call("./deploy_stack_bash")
	