# You are given a dictionary consisting of word pairs. Every word is a synonym the other word in its pair. All the words in the dictionary are different. 
# After the dictionary there's one more word given. Find a synonym for him. 
# is invalid. 
# input:3
#       Hello Hi
#       Bye Goodbye
#       List Array
#       Goodbye
# output:bye
# input:1
#       1234 4321
#       1234
# output:4321

a=int(input())
n=[input().split() for i in range(a)]
w=dict()
for i in range(a):
  w[n[i][0]]=n[i][1]
for j in range(a):
  w[n[j][1]]=n[j][0]
print(w[input()])