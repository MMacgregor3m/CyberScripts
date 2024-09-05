import random

vowels = ["A", "E", "I", "O", "U", "Y"]
cons = ["B", "C","D", "F", "J", "K","L","M","N","O", "P", "S", "T", "U", "V", "X", "Z"]

def builtWord():
    randomNumber = random.randint(2, 4)
    name=""
    for X in range (randomNumber):
        randomVowel = random.choice(vowels)
        randomCons = random.choice(cons)
        name= name + randomVowel+ randomCons
    return name

print(builtWord())