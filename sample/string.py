#! /usr/bin/env python3

import re

print( '##### hello' )

print(re.findall(r'\(.+\)', 'abc(def)ghi'))
# ['(def)']

print(re.findall(r'(\(.+\)).*(\(.+\))', 'abc(def)ghi(xyz)....'))
# ['def']
