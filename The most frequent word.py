# Given the text: the first line contains the number of lines, then given the lines of words. Print the word in the text that occurs most often. If there are many such words, print the one that is less in the alphabetical order. 
# input:1
#       apple orange banana banana orange
# output:banana
# input:1
#       zcgdwbsvuwszj bqzcytzpsdplq zczwrqe zvnisfcytzpsdplgdwbsvcytzpsdple bqzbqzzczwrqgdwbsvgdwbsv
# output:gdwbsv

a=input()
b=input()
s=b.split()#變list
w=dict()
c=[]
for i in s:
  w[i]=0
for j in s:
  if j in w:
    w[j]=w[j]+1
    c.append(w[j])
k=c.index(max(c))
print(s[k])