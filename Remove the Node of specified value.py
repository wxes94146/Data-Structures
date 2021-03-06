# Give you a series of numbers. Build a linked list for them by add method. 
# Then give you an value, remove the node that have data = value. 
# Print the final LinkedList. 
# input:1 2 3 2 1
#       3
# output:1 2 2 1
# input:1 1 1 1 1 1 1 1 1 1 1 1
#       3
# output:1 1 1 1 1 1 1 1 1 1 1 1
# input:1 2 3 4 5 1 2 1 2 7 3
#       3
# output:1 2 4 5 1 2 1 2 7

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
  def removeElements(self,val):
    p=self.front
    while p.data == val:
      p = p.next
      return
    while p.next != None:
      if p.next.data == val:
        p.next = p.next.next
      else:
        p=p.next
    return

x=LinkedList()
a=input().split()
for j in range(len(a)):
  x.addNode(int(a[j]))
b=int(input())
x.removeElements(b)
c=x.list_print()
print(" ".join('%s' %id for id in c))