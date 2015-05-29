'''
s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
'''

def gestr(s1,s2):
  count=0
  mare=0
  s3=''
  
  if s1<s2:
    count=len(s2)
    mare=s1
    
  elif s1>=s2:
    count=len(s1)
    mare=s2
    
  for i in range(count):
    s3 +=s1[i]+s[i]
    
  if not s1==s2:
    s3 +=mare[count:]
    
  return s3
  
