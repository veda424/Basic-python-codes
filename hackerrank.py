def oddNumbers(l, r):
    oddarr= []
    for num in l:
        if num%2 != 0:
            oddarr.append(num)
    for num in r:
        if num%2 != 0:
            oddarr.append(num)
    return oddarr

ans = oddNumbers([1,2,3,4,5],[6,7,8,9])
print(ans)
