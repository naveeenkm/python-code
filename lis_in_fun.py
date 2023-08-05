def moreThan5char(list):
    print("name that more than 5 charcter")
    for i in list:
        if len(i)>=5:
            print(i,end=" ")
    
list=[]
print("enter the any 10 names")
for i in range(10):
    i=input()
    list.append(i)
    
moreThan5char(list)     