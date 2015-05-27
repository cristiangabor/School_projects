#interative

def my_log(x,base):
  count -=1
  while x>0:
    x /=base
    count +=1
  if x==0:
    return 1
    

#Recursive

def myLog(x,b):
  if x<b:
    return 0
  return 1 + myLog(x/b,b)
  
  

