# Add a method contains to the Tree class that searches the tree for a given integer, returning true if it is found.
# If an Tree variable tree referred to the tree below, the following calls would have these results:
# tree.contains(87) true
# tree.contains(60) true
# tree.contains(63) false
# tree.contains(42) false
# input:17 41 9 29 6 81 40
#       40
# output:True

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
  def PrintTree(self):
    self.PrintQueue(self.overallRoot)
    print()
  def PrintQueue(self,root):
    if root!=None:
      self.PrintQueue(root.left)
      if root.data == 40:
        print(str(root.data),end="")
      else:
        print(str(root.data),end=" ")
      self.PrintQueue(root.right)
  def contains(self,node,value):
    if node==None:
      return False
    elif node.data==value:
      return True
    else:
      return self.contains(node.left,value) or self.contains(node.right,value)
a=input().split()
b=int(input())
x=Tree(a)
print(x.contains(x.overallRoot,b))