# Given a list of countries and cities of each country. Then given the names of the cities. For each city specify the country in which it is located. 
# input:2
#       USA Boston Pittsburgh Washington Seattle
#       UK London Edinburgh Cardiff Belfast
#       3
#       Cardiff
#       Seattle
#       London
# output:UK
#        USA
#        UK
# input:2
#       Russia Moscow Petersburg Novgorod Kaluga
#       Ukraine Kiev Donetsk Odessa
#       3
#       Odessa
#       Moscow
#       Novgorod
# output:Ukraine
#        Russia
#        Russia

a=int(input())
n=[input().split() for i in range(a)]
w=dict()
for j in range(a):
  for k in range(len(n[j])):
    w[n[j][k]]=n[j][0]
b=int(input())
m=[input().split() for u in range(b)]
for y in range(len(m)):
  print(w[m[y][0]])