smatrix=[]
for i in range(len(matrix)):
  for j in range(len(matrix[0])):
    if matrix[i][j] != 0:
      y=[]
      y.append(i)
      y.append(j)
      y.append(matrix[i][j])
      smatrix.append(y)
print("sparse matrix=",smatrix)

A=[[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]]
B=[[0, 6, 0, 0], [0, 0, 8, 0], [0, 5, 0, 0], [0, 3, 0, 0]]
matrix=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for i in range(len(A)):
  for j in range(len(B)):
    matrix[i][j]=A[i][j]+B[i][j]
print("normal matrix=",matrix)

smatrix=[]
for i in range(len(matrix)):
  for j in range(len(matrix[0])):
    if matrix[i][j] != 0:
      y=[]
      y.append(i)
      y.append(j)
      y.append(matrix[i][j])
      smatrix.append(y)
print("sparse matrix=",smatrix)
