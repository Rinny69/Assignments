print("SALARY PROGRAM")

input("Enter the Employee name: ")
print("1.Manager")
print("2.Team Leader")
print("3.Team Member")

a=int(input("designation:"))
if a==1:
  sl=2000
elif a==2:
  sl=1800
elif a==3:
  sl=1500
else:
  print("Enter correct number ")   
present= float(input("Enter days Employee was present: "))
if present>31:
  print("Enter correct value")

basic=float(sl*present)
print("Salary without overtime is: ",basic)

overtime= float(input("How many days of overtime Did you work?: "))
ot= float(overtime*sl)
print("SALARY WITH OVERTIME: ",ot)

ts= float(bs+ot)
print("TOTAL: ",ts)
