from numpy import *
m=matrix('1,2,8,5,6;4,8,6,9,10')
m1=matrix('1,3,8,5,6;4,8,6,9,10')
print(m+m1)

print(m.shape,m1.shape)
m3=m*m1
print(m3)
print(diagonal(m))