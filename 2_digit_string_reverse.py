def postion(s):
    for i in range(0,len(s),2):
        s[i],s[i+1] = s[i+1],s[i]
    st=''.join(s)
    print(st)

if __name__ == '__main__':
    s1 = input("string1 : ")
    s2 = input("string2 : ")
    s3 = input("string3 : ")
    s4 = input("string4 : ")
    s5 = input("string5 : ")
    postion(list(s1))
    postion(list(s2))
    postion(list(s3))
    postion(list(s4))
    postion(list(s5))
   

    

