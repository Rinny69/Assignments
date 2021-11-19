#linear search================

list1=[]
n = int(input("number of elements="))
for i in range(n):
    x=int(input("enter number="))
    list1.append(x)
y=(int(input("enter number to search= " )))
for i in range(len(list1)):
    if list1[i]==y:
        print(f"{y} is at index {i}")
        
