# Implement the binary search with recursion. Print the index of 42 and the number of recursive times. 
# input:-4 2 7 10 15 20 22 25 30 36 42 50 56 68 85 92 103
# output:10
#        3

def BinarySearch(a,target,min = None,max = None,b = None) :
  if min == None:
    return BinarySearch(a,target,0,len(a) - 1,b+1)
  elif (min > max):
    return -1
  else:
    mid = int((min + max) / 2)
    if int(a[mid]) < target:
      return BinarySearch(a,target,mid + 1,max,b+1)
    elif int(a[mid]) > target:
      return BinarySearch(a,target,min,mid - 1,b+1)
    else:
      return mid,b
a = input().split()
z=BinarySearch(a,42,0,len(a)-1,1)
print(z[0],z[1],sep="\n")