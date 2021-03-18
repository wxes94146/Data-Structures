# 利用DFS找出tree中是否有指定路徑和之路徑
# input:8
#       0 5 1,2
#       1 4 3
#       2 8 4,5
#       3 11 6,7
#       4 13 -1
#       5 4 8
#       6 7 -1
#       7 2 -1
#       8 1 -1
#       22
# output:True

class node:
  data = None #數值
  visited = False
  adjnodes = [] #相鄰的鄰居
  def __init__(self, data, adjnodes):
    self.data = data
    self.adjnodes = adjnodes
class graph:
  num_nodes = 0
  graph_node = []
  def __init__(self, num_nodes):
    self.num_nodes = num_nodes
  def add_node(self, data, adjnodes):
    self.graph_node.append(node(data, adjnodes))
  def g_print(self):
    for i in range(self.num_nodes):
      print(self.graph_node[i].data)
      v = self.graph_node[i].adjnodes.split(",")
      for j in range(len(v)):
        if v[j] == "-1":
          break
        else:
          print(self.graph_node[int(v[j])].data)
  def DFS_path_sum(self, node, goal, path_sum):
    if goal == node.data + path_sum:
      return True
    node.visited = True
    for index in node.adjnodes:
      if index == -1:
        break
      elif self.graph_node[index].visited == True:
        continue
      elif self.DFS_path_sum(self.graph_node[index], goal, node.data + path_sum) == True:
        return True
    return False

a = int(input())
x = graph(a)
z = [input() for i in range(a+1)]
for k in range(a+1):
  b = z[k].split()
  f = b[2].split(",")
  k = [int(i) for i in f]
  x.add_node(int(b[1]), k)
print(x.DFS_path_sum(x.graph_node[0], int(input()), 0))