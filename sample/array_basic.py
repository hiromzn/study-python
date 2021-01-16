#! /usr/bin/env python

##
## list (1D)
##
l = ['apple', 100, 0.123]
print( l )

##
## list (2D)
##
l_2d = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print( l_2d )
# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

##
## index
##
print(l[1])
# 100
print(l_2d[1])
# [3, 4, 5]
print(l_2d[1][1])
# 4
print(l[:2])
# ['apple', 100]

print( "l_num = [0, 10, 20, 30, 40, 50]" )
l_num = [0, 10, 20, 30, 40, 50]

print( "print(min(l_num))" ); print(min(l_num))
# 0
print( "print(max(l_num))" ); print(max(l_num))
# 30
print( "print(sum(l_num))" ); print(sum(l_num))
# 60
print( "print(len(l_num))" ); print(len(l_num))
print( "print(sum(l_num) / len(l_num))" ); print(sum(l_num) / len(l_num))
# 15.0

print( "l_num[0]" ); print(l_num[0])
print( "l_num[1]" ); print(l_num[1])
print( "l_num[5]" ); print(l_num[5])
# ERROR : print( "l_num[6]" ); print(l_num[6])
print( "l_num[1:1]" ); print(l_num[1:1])
print( "l_num[1:2]" ); print(l_num[1:2])
print( "l_num[1:3]" ); print(l_num[1:3])
print( "l_num[0:3]" ); print(l_num[0:3])
print( "l_num[0:4]" ); print(l_num[0:4])
print( "l_num[0:5]" ); print(l_num[0:5])

##
## for loop
##
l_str = ['apple', 'orange', 'banana']

for s in l_str:
    print(s)

##
## Multidimensional array
##
##
import numpy as np

arr = np.array([0, 1, 2])
print(arr)
# [0 1 2]

arr_2d = np.array([[0, 1, 2], [3, 4, 5]])
print(arr_2d)
# [[0 1 2]
#  [3 4 5]]
