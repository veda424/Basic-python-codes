def fibonacii(n):
   
    f0 = 0
    f1 = 1
    print(f0)
    print(f1) 
    for i in range(n-1):
        ans = f0 + f1
        print(ans)
        f0 = f1
        f1 = ans       
if __name__ == "__main__":
    while True:
        try:
            n = input("Enter Number : ")
            if n == 'q':
                break
            elif n == "0":
                print("0")
            else:
                fibonacii(int(n))
        except:
            print("********Please enter a vaild  integer number *******")
        
