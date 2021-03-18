# The text is given in a single line. For each word of the text count the number of its occurrences before it. 
# A word is a sequence of non-white space characters. Two consecutive words are separated by one or more spaces. Punctuation marks are a part of a word, by this definition. 
# input:one two one thothree
# output:0 0 1 0 0
# input:you will not solve this test. This @problem@ is unsolvable.
# output:0 0 0 0 0 0 0 0 0 0
# input:aba aba; aba @?“
# output:0 0 1 0

x=input()
s=x.split()
a=dict()
for j in range(len(s)):
  a[s[j]]=0
for i in s:
  if i in a:
    a[i]=a[i]+1
  print(a[i]-1)