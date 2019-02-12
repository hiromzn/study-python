#! /usr/bin/env python3

import subprocess
import sys

def command(cmd):
    print( '#### command :', cmd )
    res = subprocess.run( cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
    print( '#### stdout' )
    sys.stdout.buffer.write( res.stdout )
    print( '#### stderr' )
    sys.stderr.buffer.write( res.stderr )

#
# MAIN
#
arg = [ 'ls', '/' ]
command( arg )

arg = [ 'ls', '-aF', '/' ]
command( arg )

arg = [ 'ls', '/hoge' ]
command( arg )
