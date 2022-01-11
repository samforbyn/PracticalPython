import random

def main():
    user = input("Welcome - enter your name:\n")

    randNum = random.randint(1,101)

    print(f"{user}, I'm thinking of a number between 1 and 100...\nTry to guess my number!")
    
    has_won = False
    count = 0
    while has_won == False:
        guess = int(input("Your guess:\n"))

        if guess < randNum:
            print("Your guess is too low, try again.")
            count += 1
        elif guess > randNum:
            print("Your guess is too high, try again.")
            count += 1
        else:
            print(f"Nicely done, {user}! You found my number in {count} tries")
            has_won = True

main()