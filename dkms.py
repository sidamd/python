#!/usr/bin/env python3

import subprocess

def get_amdgpu_pkg():
    p1 = subprocess.Popen(["dpkg", "-l"], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["grep", "amdgpu"], stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()
    output = p2.communicate()[0]
    return output.decode('utf-8')

if __name__ == "__main__":
    print(get_amdgpu_pkg())
