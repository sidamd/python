#!/usr/bin/env python3
#
# Copyright (c) 2023 Advanced Micro Devices, Inc. All Rights Reserved.
#
# Author: Sid Srinivasan (sid.srinivasan@amd.com)
# Check all rocm driver packages installed
# v1.0 Initial Version
import subprocess
import argparse

def run_two_cmds(cmd1, cmd2):
    p1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(cmd2, stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()
    output = p2.communicate()[0]
    return output.decode('utf-8')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Enter two commands')
    parser.add_argument('--cmd1', nargs=1, dest='cmd1', required=True, help='cmd 1')
    parser.add_argument('--cmd2', nargs=1, dest='cmd2', required=True, help='cmd 2')
    args = parser.parse_args()

#    print("--cmd1 = ", args.cmd1[0])
#    print("--cmd2 = ", args.cmd2[0])

    print(run_two_cmds(args.cmd1[0].split(), args.cmd2[0].split()))
