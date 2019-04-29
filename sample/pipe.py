#! /usr/bin/env python3

import subprocess
from subprocess import PIPE

print( '## SAMPLE : echo XXX |sort' )
with subprocess.Popen(
        'sort',
        shell=True,
        universal_newlines=True,
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,
) as pipe:
    out, err = pipe.communicate('One\nTwo\nThree\nFour')
    for line in out.splitlines():
        print('===', line)

print( '## SAMPLE : ls *.py |print' )
cmd = subprocess.Popen(
    "ls *.py",
    shell=True,
    stdout=subprocess.PIPE )
cmdout = cmd.communicate()[0].splitlines()
for file in cmdout:
    print( file )
