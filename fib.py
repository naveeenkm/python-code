
def fib(i):
    if i==0 or i==1:
        return i
    else:
        return fib(i-1)+fib(i-2)
       

n=int(input("enter the number to print the fibonicii series"))
for i in range (n):
    print(fib(i),end="  ")
