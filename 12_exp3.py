f1 = True
while f1:
    n = int(input('''enter a number or \n press'q' for exit\n '''))
    if n=='q':
        break
    li = [i*n for i in range(1,11)]
    print(li)
    with open("mul.txt","w") as f:
        f.write(str(li))
    



