#letter with highest frequency---------------------------------------------
str=input("enter word:-")
ch=input("enter caracter:-")
j=0
for i in range(len(str)):
  if ch==str[i]:
    j=j+1
print(j)

#longest word in the string----------------------------------------------
list1=[]
str=input("enter string:-")
list1=str.split()
c=[]
for i in range(len(list1)):
  if len(c)<len(list1[i]):
    c=list1[i]

print("word with longest length=",c)

#palindrome-----------------------------------------------------------------
a=input("enter word:")
b=a
x=""
for i in range(len(b)-1,-1,-1):
  x=x+b[i]
if a==x:
  print("palindrome")
else:
  print("not a palindrome")
  
