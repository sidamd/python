#!/usr/bin/env python3

import sys
import subprocess
import argparse
import shlex

def run_one_command(cmd1):
        p1 = subprocess.run(shlex.split(cmd1), capture_output=True, text=True)
        #p1.communicate()[0]
        return p1.stdout


#result = subprocess.run(sys.argv[1:], capture_output=True, text=True,  shell=True)

if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Enter one Command")
        parser.add_argument('--cmd', nargs=1, dest='cmd', required=True, help='enter a command')

        args = parser.parse_args()

        print(run_one_command(args.cmd[0]))
