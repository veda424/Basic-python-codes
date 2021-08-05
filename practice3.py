with open("currency.txt","r") as f:
    info = f.readlines()
currencydict={}
for line in info:
    l1=line.split()
    currencydict[l1[0]] = l1[2]
while True:
    print("WELCOME TO CURENCY CONVERTER!\n 1.list of currency's \n 2.convert currency \n 3.quit \n")  
    choice= input("Enter ur choice : ")
    if choice =="3":
        break
    elif choice =="1":
        [print(i) for i in currencydict.keys()] 
    elif choice == "2":
        convert=input("Enter in which currency you want to covert : ")
        rs=float(input("Enter amout in rs: "))
        converted = rs * float(currencydict[convert])
        print(f"After Converting : {converted} ")
    else:
        print("INVALID CHOICE \n please enter a valid choice from above")
        
       

