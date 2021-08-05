from random import randint
count = 0 
attempt = 0
randno = randint(1,9)
while(count == 0):          
    uno = int(input("Enter number : "))
    if uno > randno:
        print(" wrong!! enter smaller no ")
        attempt += 1
    elif uno < randno:
        print("wrong!1 enter greater no ")
        attempt += 1
    else:
        print("Gotcha!! you guesssed it right ")
        attempt += 1
        count = 1
print(f"you required {attempt} no. of attemps")

with open("guessScore.txt","r+") as f:
    pscore = f.read()
    pscore = int(pscore)
    if attempt < pscore:
        f.truncate(0)
        f.seek(0)
        f.write(str(attempt))
    
    


