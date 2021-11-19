#merge sort

 def mergesort(arr):
  if len(arr) > 1:
    arr1=[]
    for i in range(0,len(arr)//2):
      arr1.append(arr[i])
      i=i+1
    arr2=[]
    for i in range((len(arr)//2),len(arr)):
      arr2.append(arr[i])
      i=i+1

    mergesort(arr1)
    mergesort(arr2)

    i = 0
    j = 0
    k = 0
    while i < len(arr1) and j < len(arr2):
      if arr1[i] < arr2[j]:
        arr[k] = arr1[i]
        i += 1
      else:
        arr[k] = arr2[j]
        j += 1
      k += 1

    while i < len(arr1):
      arr[k] = arr1[i]
      i += 1
      k += 1

    while j < len(arr2):
      arr[k] = arr2[j]
      j += 1
      k += 1


arr = []
n=int(input("enter number of elements = "))
for i in range(n):
  x=float(input("enter the number = "))
  arr.append(x)

mergesort(arr)
print(arr)
