def armstrong(n):
    rno = n
    strn = str(n)
    l = len(strn)
    ans = 0
    while(n > 0):
        rem= n % 10
        ans =  rem**l + ans
        n = n // 10
    if ans == rno :
        print(f"{rno} is a armstrong number")
    else :
        print(f"{rno} is not a armstrong number")

if __name__ == '__main__' :
    while(True):
        try:
            n = input("Enter Number : ")
            if n == 'q':
                break
            else:
                armstrong(int(n))
        except:
            print("Wrong number entered! Please enter a valid Integer number :")

    


