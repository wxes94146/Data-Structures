# Give you a series of numbers. 
# Build a linked list for them by add method. 
# Remove the node of the specified index. Retuen None if the node doesn’t exist. 
# input:1 2 3 2 1
#       3
# output:1 2 2 1
# input:1 1 1 1 1 1 1 1 1 1 1 1
#       1
# output:1 1 1 1 1 1 1 1 1 1 1
# input:1 2 3 4 5 1 2 1 2 7 3
#       1
# output:2 3 4 5 1 2 1 2 7 3

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
  def list_print(self):
    Node = self.front
    z=[]
    while Node:
      z.append(Node.data)
      Node = Node.next
    return z
  def remove(self,index):
    p=self.front
    if index==1:
      self.front=p.next
      return
    for i in range(index-2):
      if p.next==None:
        return
      p=p.next
    p.next=p.next.next

x=LinkedList()
a=input().split()
b=int(input())
for j in range(len(a)):
  x.addNode(a[j])
x.remove(b)
z=x.list_print()
print(" ".join('%s' %id for id in z))