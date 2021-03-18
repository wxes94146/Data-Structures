# Write a python class that acts as a calculator. 
# Only add, subtraction function. 
# You can only have this Class Members: (Hint: Use Recursion)
# def calc(self,x(string)):
# input:1+1
# output:2
# input:1+1-3+4+4-6
# output:1

class Calculator:
  def calc_(self,x):
    def d(x):
      x=str(x)
      if x.isdigit():
        return int(x)
      for i in ("+","-"):
        a,b,c=x.partition(i)
        if b=="+":
          return d(a)+d(c)
        elif b=="-":
          return d(a)-d(c)
    return d(x)
f=Calculator()
n=str(input())
print(f.calc_(n))