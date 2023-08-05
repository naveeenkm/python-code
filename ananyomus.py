f=lambda a,b:a+b
print(f(5,9))
#uses of lambda
def is_even(n):
    return n%2==0
nums=[4,6,5,8,3,1,7]
evens=list(filter(is_even,nums))
print(evens)
##with uses of lambda function
nums=[4,6,5,8,3,1,7]
evens=list(filter(lambda n:n%2==0,nums))
print(evens)