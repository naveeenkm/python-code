from array import *
vals=array('i',[89,96,75,24,45])
print(vals)
print(vals.buffer_info())

newArr=array(vals.typecode, (a for a in  vals))