# Add a method remove to the IntTree class that removes a given integer value from the tree, if present. Assume that the elements of the IntTree constitute a legal binary search tree, and remove the value in such a way as to maintain ordering.
# input:7 (共有多少個node)
#       55
#       29
#       87
#       -3
#       42
#       60
#       91
#       55 (移除)
#       87 (移除)
# output:-3
#        29
#        42
#        60
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
  def getmin(self,root):
    if root.left == None:
      return root.data
    else:
      return self.getmin(root.left)
  def remove(self,root,value):
    if root == None:
      return None
    elif root.data > value:
      root.left = self.remove(root.left,value)
    elif root.data < value:
      root.right = self.remove(root.right,value)
    else:
      if root.right == None:
        return root.left
      if root.left == None:
        return root.right
      root.data = self.getmin(root.right)
      root.right = self.remove(root.right,root.data)
    return root
a = [int(input()) for i in range(int(input()))]
x = Tree(a)
x.remove(x.overallRoot,int(input()))
x.remove(x.overallRoot,int(input()))
x.PrintTree()