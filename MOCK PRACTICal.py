print("SALARAY PROGRAM")
month=(input("enter the salary month: "))
  
days=float(input("enter days of month: "))
if days>31:
  print("enter valid days: ")
Total=3000

while True:
     trans_d_w = input()
     if trans_d_w =="":
        break
     else: 
       trans_d_w = trans_d_w.split(" ")
       if trans_d_w[1] == "D":
          Total = Total*days + int(trans_d_w[0])
       elif trans_d_w[1] =="W":
            Total = Total*days - int(trans_d_w[0])

            print(Total)

