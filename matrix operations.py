m=int(input("enter the number of col"))
n=int(input("enter the number of rows"))

def mat(m,n):
  out=[]
  for i in range(m):
    row=[]
    for j in range(n):
      num=int(input("enter the num"))
      row.append(num)
    out.append(row)
  return out

m1=mat(m,n)
print(m1)      

m2=mat(m,n)
print(m2)                                  
Result = [[0,0,0], [0,0,0], [0,0,0]] 


#addition
for j in range(len(m1[0])):
 for i in range(len(m1)):

    Result[i][j] = m1[i][j] + m2[i][j]

print("addition is  : ")
for r in Result:
   print(r)

#subtraction
for j in range(len(m1[0])):
 for i in range(len(m1)):

    Result[i][j] = m1[i][j] - m2[i][j]

print("subtraction is  : ")
for r in Result:
   print(r)

 #multiplication

for i in range(len(m1)):
   for j in range(len(m2[0])):
     for k in range(len(m2)):

         Result[i][j] += m1[i][k] * m2[k][j]
      

print("multiplication is  : ")
for r in Result:
   print(r)         





