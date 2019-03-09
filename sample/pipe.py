#! /usr/bin/env python3

import subprocess
from subprocess import PIPE

print( '##### echo XXX |sort' )
with subprocess.Popen('sort', shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE,
        universal_newlines=True) as pipe:
    out, err = pipe.communicate('One\nTwo\nThree\nFour')
    for line in out.splitlines():
        print('===', line)

print( '##### ls |sort' )
ls_result = subprocess.run('ls', shell=True, check=True,
        stdout=PIPE, universal_newlines=True)
sort_result = subprocess.run('sort', shell=True, check=True,
        input=ls_result.stdout, stdout=PIPE, universal_newlines=True)
for line in sort_result.stdout.splitlines():
    print('===', line)

print( '##### cat pipe.py |sort' )
with open('pipe.py', encoding='utf-8') as file:
    proc = subprocess.run('sort', shell=True, check=True,
            stdin=file, stdout=subprocess.PIPE, universal_newlines=True)
    for line in proc.stdout.splitlines():
        print('===', line)
