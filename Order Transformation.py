# Give preorder of a tree, show their in- and post-order traversals. 
# – pre:
# – in:
# – post:
# input:17 41 29 6 9 81 40
# output:29 41 6 17 81 9 40
#        29 6 41 81 40 9 17

from collections import deque
class TreeNode:
  data = None
  left = None
  right = None
  def __init__(self,data,left=None,right=None):
    self.data = data
    self.left = left
    self.right = right
class Tree:
  overallRoot = None
  def __init__(self,a):
    if len(a) == 0:
      return
    parent = deque()
    child = deque()
    self.overallRoot = TreeNode(int(a[0]))
    parent.append(self.overallRoot)
    count = 1
    while len(parent)!=0:
      while len(parent)!=0:
        n = parent.popleft()
        if count < len(a):
          n.left = TreeNode(int(a[count]))
          child.append(n.left)
          count = count + 1
        if count < len(a):
          n.right = TreeNode(int(a[count]))
          child.append(n.right)
          count = count + 1
      parent,child = child,parent
  def PrintTree_1(self):
    y=[]
    return self.PrintQueue(self.overallRoot,y)
  def PrintTree_2(self):
    j=[]
    return self.Print_post_order(self.overallRoot,j)
  def PrintQueue(self,root,y):
    if root!=None:
      self.PrintQueue(root.left,y)
      y.append(str(root.data))
      self.PrintQueue(root.right,y)
    return y
  def Print_post_order(self,root,j):
    if root!=None:
      self.Print_post_order(root.left,j)
      self.Print_post_order(root.right,j)
      j.append(str(root.data))
    return j
a=input().split()
v=deque()
c=deque()
f=deque()
f.append(a[0])
n=len(a)//2
for i in range(n):
  v.append(a[i+1])
for k in range(n):
  c.append(a[n+k+1])
for h in range(len(v)-2):
  f.append(v.popleft())
  f.append(c.popleft())
for u in range(len(v)):
  f.append(v.popleft())
for g in range(len(c)):
  f.append(c.popleft())
x=Tree(f)
a=x.PrintTree_1()
b=x.PrintTree_2()
print(" ".join('%s' %id for id in a))
print(" ".join('%s' %id for id in b))