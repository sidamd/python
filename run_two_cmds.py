#!/usr/bin/env python3
#
# Copyright (c) 2023 Advanced Micro Devices, Inc. All Rights Reserved.
#
# Author: Sid Srinivasan (sid.srinivasan@amd.com)
# Check all rocm driver packages installed
# v1.0 Initial Version
import subprocess

def run_two_cmds(cmd1, cmd2):
    p1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(cmd2, stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()
    output = p2.communicate()[0]
    return output.decode('utf-8')

if __name__ == "__main__":
    cmd1 = ["dpkg", "-l"]
    cmd2 = ["grep", "amdgpu"] 
    print(run_two_cmds(cmd1, cmd2))
