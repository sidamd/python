#!/usr/bin/env python3

import sys
import subprocess

print("Argument list: ", str(sys.argv))

result = subprocess.run(sys.argv[1:], capture_output=True, text=True,  shell=True)
print(result.stdout)
