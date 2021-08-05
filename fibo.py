def fibo(n):
    l1 = []
    f0 = 0
    f1 =1
    l1.append(f0)
    l1.append(f1)
    for i in range(0,n-1):
        ans = f0 + f1
        l1.append(ans)
        f0 = f1
        f1 = ans
    return l1
if __name__ == '__main__':
    while True:
        num = int(input("enter a num \n"))
        print(fibo(num))
        
