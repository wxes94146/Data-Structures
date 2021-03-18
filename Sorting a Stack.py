# Give you a stack. Use recursion and stack’s methods to sort it. 
# (We will check you code. No sort method can be used, only stack methods (pop, append, len)) (That is, you cannot access the list by something like a[0].)
# input:-3 14 18 -5 30
# output:30 18 14 -3 -5

z=input().split()
a=list()#要輸出的list
b=list()
a.append(z.pop())
while len(z)!=0:
  s=z.pop()
  f=z.pop()
  if int(s)>int(f):
    a.append(s)
    b.append(f)
  else:
    b.append(s)
    a.append(f)
while len(b)!=0:
  q=b.pop()
  w=b.pop()
  if int(q)>int(w):
    a.append(q)
  if len(b)==0:
    a.append(w)
print(a)