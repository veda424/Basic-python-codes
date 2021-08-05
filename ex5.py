def getdate():
    import datetime
    return datetime.datetime.now()

date = getdate()

def harry():
    global date
    print("*****Hello Harry ****\n")
    ch = int(input("what u want to do\n 1.log \n 2.retrive "))
    if ch==1:
        print("*****what u want to Add****\n")
        userch = int(input("1.Food logs \n 2.exercise log \n Enter ur choice "))
        if userch == 1:
            foodharry= input("Enter what u eat!: ")
            with open("harry_food_logs.txt","a") as f:
                f.write(f"{date}-{foodharry} \n")
        else:
            exerciseharry= input("Which exercise u did! ")
            with open("harry_exercise_logs.txt","a") as f:
                f.write(f"{date}-{exerciseharry} \n")
    else:
        retrivech = int(input("which logs you want\n 1.food logs \n 2. exercise log "))
        if retrivech == 1:
            with open("harry_food_logs.txt","r") as f:
                h_f_content = f.read()
                print(h_f_content)
        else:
            with open("harry_exercise_logs.txt","r") as f:
                h_e_content = f.read()
                print(h_e_content)

def rohan():
    global date
    print("***** Hello Rohan ****\n")
    ch = int(input("what u want to do\n 1.Log \n 2.Retrive "))
    if ch==1:
        print("*****what u want to Add****\n")
        userch = int(input("1.Food logs \n 2.Exercise log \n Enter ur choice "))
        if userch == 1:
            foodRohan= input("Enter what u eat!: ")
            with open("Rohan_food_logs.txt","a") as f:
                f.write(f"{date}-{foodRohan} \n")
        else:
            exerciseRohan= input("Which exercise u did! ")
            with open("Rohan_exercise_logs.txt","a") as f:
                f.write(f"{date}-{exerciseRohan} \n")
    else:
        retrivech = int(input("which logs you want\n 1.food logs \n 2. exercise log "))
        if retrivech == 1:
            with open("Rohan_food_logs.txt","r") as f:
                r_f_content = f.read()
                print(r_f_content)
        else:
            with open("Rohan_exercise_logs.txt","r") as f:
                r_e_content = f.read()
                print(r_e_content)

   
def hammad():
    global date
    print("***** Hello Hammad ****\n")
    ch = int(input("what u want to do\n 1.Log \n 2.Retrive "))
    if ch==1:
        print("*****what u want to Add****\n")
        userch = int(input("1.Food logs \n 2.Exercise log \n Enter ur choice "))
        if userch == 1:
            foodhammad= input("Enter what u eat!: ")
            with open("hammad_food_logs.txt","a") as f:
                f.write(f"{date}-{foodhammad} \n")
        else:
            exercisehammad= input("Which exercise u did! ")
            with open("hammad_exercise_logs.txt","a") as f:
                f.write(f"{date}-{exercisehammad} \n")
    else:
        print("which logs you want \n")
        retrivech = int(input("1.food logs \n 2. exercise log \n"))
        if retrivech == 1 :
            with open("hammad_food_logs.txt","r") as f:
                ham_f_content = f.read()
                print(ham_f_content)
        else:
            with open("hammad_exercise_logs.txt","r") as f:
                ham_e_content = f.read()
                print(ham_e_content)

    

users = ["harry","rohan","hammad"]
while True:
    user = input("enter ur name: ")
    if user in users:
        if user == "harry":
            harry()
        elif user == "rohan":
            rohan()
        else:
         hammad()
    else:
        print("Sorry ur not in our list ")
