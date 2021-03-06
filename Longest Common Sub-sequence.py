# 利用Dynammic Programming解Longest Common Sub-sequence(LCS)問題
# input:1234
#       1224533324
# output:4

def lcs(a, b):
  lengths = [[0 for i in range(len(b) + 1)] for j in range(len(a) + 1)]
  for i, x in enumerate(a):
    for k, y in enumerate(b):
      if x == y:
        lengths[i + 1][k + 1] = lengths[i][k] + 1
      else:
        lengths[i + 1][k + 1] = max(lengths[i + 1][k], lengths[i][k + 1])
  return lengths[len(a)][len(b)]
a = input()
s=[]
for j in a:
  s.append(j)
b = input()
h=[]
for p in b:
  h.append(p)
print(lcs(s, h))