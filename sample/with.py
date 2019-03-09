#! /usr/bin/env python3

print( '#### read with.py' )
with open("with.py", "r") as f:
    print(f.read())

print( '#### read with.py -> write with.py.backup~' )
with open("with.py", "r") as fr:
    with open("with.py.backup~", "w") as fw:
        fw.write(fr.read())


print( '#### class sample' )
class MySampleClass:
 
  def __enter__(self):
      print('START')
      return self
  
  def myfunc(self):
      print('Do something...')
  
  def __exit__(self, exception_type, exception_value, traceback):
    print('END')
 
with MySampleClass() as c:
  c.myfunc()
