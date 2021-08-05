oxford = {
    "asleep" :"in a state of sleep.",
    "philosophy" : "the study of the fundamental nature of knowledge, reality, and existence, especially when considered as an academic discipline.",
    "faith" : "complete trust or confidence in someone or something.",
    "optimism" : "hopefulness and confidence about the future or the success of something.",
    "frightened" : "afraid or anxious."
}
while(True):
    word = input("Enter word to find its meaning or press q to exit  : \n")
    if word == "q":
        break
    elif word in oxford.keys():
        print(oxford[word])
    else:
        print("sorry ,not present in dictonary")

