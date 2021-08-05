S = input()


def s(x):
    if x.islower():
        return ord(x)
    elif x.isupper():
        return ord(x)*100000
    elif x in "13579":
        return ord(x)*10000000000
    else:
        return ord(x)*1000000000000000000

print(*sorted(S, key=s), sep='')