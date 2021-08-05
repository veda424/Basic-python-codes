try:
    print("its a code to divide")
    a = int(input("enter first number\n"))
    b = int(input("enter seond number\n"))
    ans = a/b
    mans = int(ans)
    print(f"ans is :{mans}")
except ZeroDivisionError as e:
    print("the second number should be greater than 0")
