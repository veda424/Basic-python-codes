def factorial(num):
    for i in  range(1,num):
        num = num*i
    print(f"factorial is {num}")
    count=0
    while num>0:
        ans = num%10
        if ans==0:
            count += 1
        num = num / 10    
    print(f" trailling zeros is {count}")
    

   
numb = int(input("enter a number: "))
factorial(numb)

