def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
   
    else:
        print(a,b,end="  ")
        for i in range(2,n):
            print(a+b,end="  ")
            a,b=b,a+b
            
fib(2)
                
    