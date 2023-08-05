

  
def shuffle(l1,l2):
  res=[]
  if len(l1)<len(l2):
    minlen=len(l1)
  else:
    minlen=len(l2)
 
  for i in range(minlen):
    res.append(l1[i])
    res.append(l2[i])
    
  if len(l1)<len(l2):
    l22=l2[minlen:]
    for i in l22:
      res.append(l2[i])
      
    
    
  else:
    l11=l1[minlen:]
    for i in l11:
      res.append(l1[i])
    
    
  return res
print(shuffle([0,2,4],[1]))
    
    
    
    
    
    
    