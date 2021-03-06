# Give you a series of numbers. Build a linked list for them by add method. 
# Then give you an index, and the value. Insert the node of the value to the specified index. 
# input:1 2 3 2 1
#       3 5
# output:1 2 5 3 2 1
# input:1 1 1 1 1 1 1 1 1 1 1 1
#       3 5
# output:1 1 1 1 5 1 1 1 1 1 1 1 1
# input:1 2 3 4 5 1 2 1 2 7 3
#       10 3
# output:1 2 3 4 5 1 2 1 2 3 7 3

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
  def insert(self,index,data):
    if index==1:
      self.front=Node(data=data,next=self.front)
      return 
    p=self.front
    for i in range(index-2):
      if p.next==None:
        break
      p=p.next
    p.next=Node(data=data,next=p.next)
  def list_print(self):
    Node = self.front
    z=[]
    while Node:
      z.append(Node.data)
      Node = Node.next
    return z

x=LinkedList()
a=input().split()
b=input().split()
for j in range(len(a)):
  x.addNode(a[j])
x.insert(int(b[0]),int(b[1]))
z=x.list_print()
print(" ".join('%s' %id for id in z))