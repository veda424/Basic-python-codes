from pygame import mixer
from datetime import datetime
from time import time

def music(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def file_update(msg):
    with open("Good programmer.txt","a") as f:
        f.write(f"{datetime.now()}-{msg} \n")
init_water = time()
init_eyes = time()
init_exercise= time()
watersec = 40*60
eyessec = 30*60
exercisesec = 60

while True:
    if time() - init_water > watersec:
        print(" Is time to drink water!! type drank if u finished")
        music("water.mp3","drank")
        init_water = time()
        file_update("draked")
    if time() - init_eyes > eyessec:
        print(" Is time to close ur eyes!! type closed if u finished")
        music("eyes.mp3","closed")
        init_eyes = time()
        file_update("closed")
    if time() - init_exercise > exercisesec:
        print(" Is time to do exercise!! type done if u finished")
        music("physical.mp3","done")
        init_exercise = time()
        file_update("done")
        







    
