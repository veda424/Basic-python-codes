li = []
le = []
lo =[]
for i in range(1,10):
    n1=int(input(f"enter {i} number: "))
    li.append(n1)
for i in li:
    if i%2 ==0:
        le.append(i)
    else:
        lo.append(i)


print(le)
print(lo)
print(f"total numbers of even numbers are {len(le)}")
print(f"total numbers of odd numbers are {len(lo)}")
