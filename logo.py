""" def logo(str):
    t = ""
    for i in str:
        if (i in t):
            pass
        else:
            t=t+i
    for i in range(len(t)):
        c = str.count(t[i])
        print(f"{t[i]} = {c}")

logo("choclate") """

str = "vedant"
a = set(str)
print(a)
