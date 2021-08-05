string = input("enter a word \n")
pal = string[::-1]
if string == pal:
    print("stringis palindrome")
else:
    print("string is not palindrome")