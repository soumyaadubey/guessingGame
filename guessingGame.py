import random
def guess(x):
    random_number= random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess= int(input(f"Input a number between 1 and {x}: "))
        if guess<random_number:
            print("Too low. Guess again")
        elif guess>random_number:
            print("Too high. Guess again")
    print("Hooray! You are a genius, you have guessed the number correctly")

guess(10)
    