#! /usr/bin/env python3

filepath = "inputfile"

print( "##### read each line" )
with open(filepath, "r", encoding="utf-8") as f:
    for line in f:
        print(line)

print( "##### read all line" )
with open(filepath, "r", encoding="utf-8") as f:
    lines = f.read()
    print(lines)

print( "##### read all line by list()" )
with open(filepath, "r", encoding="utf-8") as f:
    print(list(f))

print( "##### read all line by readlines()" )
with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)

print( "##### read all line by readlines() without RET" )
with open(filepath, "r", encoding="utf-8") as f:
    lines = f.read().split('\n')
    print(lines)
