def securepass(passw):
    l1=["s", "and" ,"a" ,"i"]
    for letter in passw:
        if letter in l1:
            passw=passw.replace("s","$")
            passw=passw.replace("and","&")
            passw=passw.replace("a","@")
            passw=passw.replace("i","|")
    print(passw)


print(__name__)
if __name__ == "__main__":
    password = input("enter password \n")
    securepass(password)
