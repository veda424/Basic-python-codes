def arm(n):
    
    for i in range(1,n+1):
        new = i
        ans=0
        while new>0:
            rem = new % 10
            ans = ans + rem**len(str(i))
            new = new//10
        if ans == i:
            print(ans)
    
arm(500)

""" n = int(input("enter no: "))
ans=0
new = n
for i in range(len(str(new))):
    rem = new % 10
    ans = ans + rem**len(str(n)) 
    new=new//10
if ans == n:
    print("amstrong")
else:
    print("not arms") """


    
""" for num in range(10):
  temp=num
  sum=0
  while temp>0:
    digit=temp%10
    sum=sum+digit**len(str(num))
    temp=temp//10

  if sum==num:
    print (num) """