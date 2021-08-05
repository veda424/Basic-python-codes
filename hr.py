# Enter your code here. Read input from STDIN. Print output
n=input()
a,b = n.split(" ")
arr = []
happiness = 0
a1_arry=[]
b1_arry=[]
for i in range(int(a)):
    ar_ele = int(input())
    arr.append(ar_ele)
    
for j in range(int(b)):
    a_arry = int(input())
    a1_arry.append(a_arry)
    
for k in range(int(b)):
    b_arry = int(input())
    b1_arry.append(b_arry)
for ele in a1_arry:
    if ele in arr:
        happiness += 1
for ele in b1_arry:
    if ele in arr:
        happiness -= 1 
print(happiness)
    
    


