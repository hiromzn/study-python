#! /usr/bin/env python3

import subprocess
import sys

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

#
# MAIN
#
command('ls /')
command('ls /hoge')
command('ls -aF /')
