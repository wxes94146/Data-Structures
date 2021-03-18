# 用Dynamic Programming實作Binomial Coefficients
# input:10
#       5
# output:252

def binomialCoeff(n, k):
  if k==0 or k ==n:
    return 1
  return binomialCoeff(n-1, k-1) + binomialCoeff(n-1, k)
a = int(input())
b = int(input())
print(binomialCoeff(a, b))