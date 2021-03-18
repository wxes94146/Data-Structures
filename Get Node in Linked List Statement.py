# Give you a series of numbers. Build a linked list for them by add method. 
# Then give you an index, return the data of the specified index node. Won’t give you the over-length index. 
# input:1 2 3 2 1
#       3
# output:3
# input:1 1 1 1 1 1 1 1 1 1 1 1
#       3
# output:1
# input:1 2 3 4 5 1 2 1 2 7 3
#       10
# output:7

class Node:
  def __init__(self,data,next=None):
    self.data = data
    self.next = next
class LinkedList:
  def __init__(self,front=None):
    self.front=front
    self.size=0
  def addNode(self,data):
    if self.front == None:
      self.front = Node(data)
      return
    newNode = self.front
    while True:
      if newNode.next == None:
        break
      newNode = newNode.next
    newNode.next = Node(data)
    return newNode
  def get(self,index):
    if index==1:
      return self.front
    p=self.front
    for i in range(index-1):
      if p==None:
        return p.data
      p=p.next
    return p.data

x=LinkedList()
a=[int(i) for i in input().split(' ')]
for i in range(len(a)):
  x.addNode(a[i])
b=int(input())
print(x.get(b))