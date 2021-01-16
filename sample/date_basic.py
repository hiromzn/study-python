#! /usr/bin/env python3

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

from datetime import datetime, date, time

print ( ("old date: %s") %  datetime.utcfromtimestamp(1541030400))

ds1 = "2021-10-10"
ds2 = "2021-10-16"
dt1 = datetime.strptime(ds1, "%Y-%m-%d")
dt2 = datetime.strptime(ds2, "%Y-%m-%d")
dt = dt1;
print ( ("date 1: %s") %  dt.date() )
print ( ("  week number: W : %s") %  dt.strftime("%W"))
print ( ("  week as decimal number (0:Sunday..6:Saturday) : w : %s") %  dt.strftime("%w"))
print ( ("  week as decimal number (1:Mon..7:Sun) : u : %s") %  dt.strftime("%u"))
print ( ("  week string: A : %s") %  dt.strftime("%A"))
print ( ("  week string: a : %s") %  dt.strftime("%a"))

dt = dt2
print ( ("date 1: %s") %  dt.date() )
print ( ("  week number: W : %s") %  dt.strftime("%W"))
print ( ("  week as decimal number (0:Sunday..6:Saturday) : w : %s") %  dt.strftime("%w"))
print ( ("  week as decimal number (1:Mon..7:Sun) : u : %s") %  dt.strftime("%u"))
print ( ("  week string: A : %s") %  dt.strftime("%A"))
print ( ("  week string: a : %s") %  dt.strftime("%a"))
