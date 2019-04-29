#! /usr/bin/env python3

import subprocess
import sys

#----------------------------------
#
# run command
#   format : "cmd opt args"
#
def command(cmd):
    print( '#### command :', cmd )
    try:
      res = subprocess.run( cmd, shell=True, check=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            universal_newlines=True)
      for line in res.stdout.splitlines():
        print( line )
      for line in res.stderr.splitlines():
        print( line )
    except subprocess.CalledProcessError:
        print('ERROR: fail subprocess.run [' + cmd + ']', file=sys.stderr)
        # sys.exit(1)

command('ls -d /*a*')
command('ls /hoge')
command('ls -adF /*a*')

#----------------------------------
#
# run command
#   format : "cmd" "arg1" "arg2"
#
def command2(cmd):
    print( '#### command2 :', cmd )
    res = subprocess.run( cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
    print( '#### stdout' )
    sys.stdout.buffer.write( res.stdout )
    print( '#### stderr' )
    sys.stderr.buffer.write( res.stderr )

#command2( [ 'ls', '/*a*' ] )
command2( [ 'ls', '-aF', '/*a*' ] )
command2( [ 'ls', '/hoge' ] )

#----------------------------------
#
# pipe sample:
#

from subprocess import PIPE

print( '##### ls |sort' )
ls_result = subprocess.run(
	'ls',
	shell=True, check=True, universal_newlines=True,
        stdout=PIPE )
sort_result = subprocess.run('sort', shell=True, check=True,
        input=ls_result.stdout, stdout=PIPE, universal_newlines=True)
for line in sort_result.stdout.splitlines():
    print('===', line)

print( '##### cat cmd.py |sort' )
with open('cmd.py', encoding='utf-8') as file:
    proc = subprocess.run(
	'sort', 
	shell=True, check=True, universal_newlines=True,
	stdin=file, stdout=subprocess.PIPE )
    l=0;
    for line in proc.stdout.splitlines():
        print('===', line)
        l += 1
        if l > 10:
            exit

