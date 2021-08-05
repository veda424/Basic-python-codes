def faulty_calculator(expression):
    if expression == "45*3":
        return 555
    elif expression == "56+9":
        return 77
    elif expression =="56/6":
        return 4
    else:
        ans = eval(expression)
        return ans

while(True):
    expression = input("enter question : \n")
    output = faulty_calculator(expression)
    print(f"Your ans is :{output}")



