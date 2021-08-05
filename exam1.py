l1=[]
equ = input("enter equation\n")
lhs,rhs = equ.split("=")
for i in lhs:
    l1.append(i)
    
        
n1 = int(l1[0])
n2 = int(l1[1])
n3 = int(l1[2])

add1 = n1 + n2
stringadd1 = str(add1) + str(n3)

add2 = n2 + n3
stringadd2 = str(n1) + str(add2)

if stringadd1 == rhs:
    print("equation gets corrected and its get matched by suming no.1 and no2 in LHS")
    print(f"{stringadd1} = {rhs}")
elif stringadd2 == rhs:
    print("eqaution gets corrected and its get matched  by suming no2 and no3 in LHS")
    print(f"{stringadd2} = {rhs}")  
else:
    print("-1")  

    

