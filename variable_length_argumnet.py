def tuple(*a):
    print(a)
    
tuple(2,5,4,7,8,6)
#this *a will take parameters in the form of tuples
def sum(a,   *b):
    c=a
    for i in b:
        c+=i
    print(c)
    
sum(2,8,8,7)   
def sum1(*b):
    c=0
    for i in b:
        c+=i
    print(c)
    
sum1(2,8,8,7)    

        