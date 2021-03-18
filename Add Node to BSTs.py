# Add a method add to the SearchTree class that adds a given integer value to the tree.
# Assume that the elements of the SearchTree constitute a legal binary search tree, and add the new value in the appropriate place to maintain ordering.
# input:7 (共有多少個node)
#       55
#       29
#       87
#       -3
#       42
#       60
#       91
#       -5 (加入)
#       30 (加入)
#       49 (加入)
#       10 (加入)
# output:-5
#        -3
#        10
#        29
#        30
#        42
#        49
#        55
#        60
#        87
#        91

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
  def add(self,node,value):
    if node==None:
      node=TreeNode(value)
    elif node.data>value:
      node.left=self.add(node.left,value)
    elif node.data<value:
      node.right=self.add(node.right,value)
    return node
a=[int(input()) for i in range(int(input()))]
x=Tree(a)
for k in range(4):
  x.add(x.overallRoot,int(input()))
x.PrintTree()