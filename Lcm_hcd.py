def hcd(num1 , num2):
    mn = min(num1 , num2)
    for i in range(1 , mn+1):
        if num1%i==0 and num2%i==0:
            ans1 = i
            break
    print(f"hcd is {ans1}")     
    

num1 = int(input("enter number1 : "))
num2 = int(input("Enter number2 : "))
hcd(num1 , num2)

