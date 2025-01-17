import random
def Validate(guess):
    if type(guess) != str or guess ==" ":
        return False
    else:
        return True

elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon",
            "Nitrogen", "Oxygen", "Fluorine", "Neon"]

randomElement = random.choice(elements)
print("Random element is chosen")
attempts = 3
print("Guess the element")
guess = input()

while (attempts > 1):
    check = Validate(guess)
    if check :
            if guess.lower() == randomElement.lower():
                 print("Correct!")
                 attempts = 0
            else:
                 attempts -= 1
                 print("Wrong!")
                 print("you have " + str(attempts) + " attempts remaining")
                 print(f"Try again ")
                 print("Guess the element")
                 guess = input()
    elif check == False:
        print("please enter a valid input")
        print("Guess the element")
        guess = input()

print(f"correct answer was {randomElement}")
print("Thank you for playing!")


