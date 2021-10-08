str=input("enter word:-")
ch=input("enter caracter:-")
j=0
for i in range(len(str)):
  if ch==str[i]:
    j=j+1
print(j)
