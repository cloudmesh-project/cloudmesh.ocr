from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
import sys, os




class DeployCommand(PluginCommand):

    @command
    def do_benchmark(self, args, arguments):
        """
        ::

          Usage:
                benchmark
        """
		os.system('~/ocr/code/benchmark_bash')
		