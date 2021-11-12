def selectionSort(array):
  n = len(array)
  for i in range(n):
    minimum = i

    for j in range(i+1, n):
      if (array[j] < array[minimum]):

        minimum = j
     
    temp = array[i]
    array[i] = array[minimum]
    array[minimum] = temp
    
  return array

def bubble_sort(list1):  
  
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    return list1  



array = [93.5, 45.5, 97.3, 91.6, 57.1, 81.9, 73.11]
print("Input:", array)

print("Bubble Sort:")
print("Output:",bubble_sort(array))
newarr=array[::-1]
print("Top 5 Score:", newarr[0:5])

print("\n\n")

array=[85.11,45.12,77.85,57.25,75.8,65.6,34.5]
print("Input:", array)
print("Selection Sort:")
print("Output",selectionSort(array))
newarr=array[::-1]
print("Top 5 Score:", newarr[0:5])
