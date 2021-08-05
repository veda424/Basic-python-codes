l1 = []
print("This is Matrix1")
for i in range(1,4):
    for j in range(1,4):
        val1 = int(input(f"Enter a{i}{j} element of matrices : "))
        l1.append(val1)

l2 = []
print("This is Matrix2")
for i in range(1,4):
    for j in range(1,4):
        val2 = int(input(f"Enter a{i}{j} element of matrices : "))
        l2.append(val2)

a11 = l1[0] + l2[0]
a12 = l1[1] + l2[1]
a13 = l1[2] + l2[2]

a21 = l1[3] + l2[3]
a22 = l1[4] + l2[4]
a23 = l1[5] + l2[5]

a31 = l1[6] + l2[6]
a32 = l1[7] + l2[7]
a33 = l1[8] + l2[8]

print("Matrix After Addition :")
print(f''' 
                         
          |  {a11}  {a12} {a13} \t|
          |  {a21}  {a22} {a23} \t|
          |  {a31}  {a32} {a33} \t|
                        
          ''')