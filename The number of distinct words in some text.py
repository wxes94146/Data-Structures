# Given a number n, followed by n lines of text, print the number of distinct words that appear in the text. For this, we define a word to be a sequence of non-white space characters, seperated by one or more white space or newline characters. Punctuation marks are part of a word, in this definition. 
# input:4
#       She sells sea shells on the sea shore;
#       The shells that she sells are sea shells I'm sure.
#       So if she sells sea shells on the sea shore,
#       I'm sure that the shells are sea shore shells.
# output:19
# input:1
#       a b a c a b a d a b a c a b a
# output:4

a=[input().split() for i in range(int(input()))]
n=set(a[0])
for k in range(len(a)-1):
  n=n|set(a[k+1])
print(len(n))