count = 0
l1 = []
l2 =[]
ans = 0
while True:
    items = input("Enter item name: ")
    if items == 'q':
        print("Thanks for shopping! ")
        break
    else:
        l1.append(items)
        count += 1
        num = input("Enter price : ")
        l2.append(num)
        num = int(num)
        ans = num + ans
print(f"Your Bill is of Rs.{ans} ")       
templete =   f''' WELCOME TO VEDANT'S STORE! \n Your total items were {count} \n Items are {l1}
    With prices are {l2} \n total bill is of rs.{ans} \n THANKS FOR SHOPPING WITH US!'''     
        
with open("recipt.txt","w") as f:
    f.write(templete)

    
    
   


