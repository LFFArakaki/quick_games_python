import random
from classes.game import Game
from classes.difficulty import Mode

def hard():
    correct_answer = False
    guesses = 0
    while not correct_answer:
        num = random.randint(0, 100)
        guess = int(input("Pick a number between 0 and 100:\n"))
        guesses += 1
        if win_game(guesses, guess, num):
            correct_answer = True
        else:
            print("Incorrect! Try again!")
            special_messages(guess, num)
            print(f'Number was {num}\n')
def medium():
    correct_answer = False
    guesses = 0
    num = random.randint(0, 100)
    while not correct_answer:
        guess = int(input("Pick a number between 0 and 100:\n"))
        guesses += 1
        if win_game(guesses, guess, num):
            correct_answer = True
        else:
            print("Incorrect! Try again!\n")
def easy():
    correct_answer = False
    guesses = 0
    num = random.randint(0, 100)
    while not correct_answer:
        guess = int(input("Pick a number between 0 and 100:\n"))
        guesses += 1
        if win_game(guesses, guess, num):
            correct_answer = True
        else:
            print("Incorrect! Try again!")
            if guess > num:
                print("The real number is smaller than your guess!\n")
            else:
                print("The real number is bigger than your guess!\n")

def special_messages(guess, real):
    if guess >= real-1 and guess <= real+1:
        print("So close, yet so far T-T")
        if guess == -1:
            print("Maybe if you remebered the lowest is 0 you would've gotten it ._.")
        if guess == 101:
            print("Maybe if you remebered the highest is 100 you would've gotten it ._.")
    elif guess > 100 or guess < 0:
        print("Not even close buddy! Remember it's from 0 to 100 ._.")
    elif guess%10 == real%10 and guess != 100 and guess >= 10 and real >= 10 and real != 100:
        print("Got half way there, just needed the first digit right")
    elif guess-(guess%10) == real-(real%10) and guess != 100 and guess >= 10 and real >= 10 and real != 100:
        print("Got half way there, just needed the second digit right")
def win_game(guesses, guess, real):
    if guess == real:
        print("Congratulations! You won!")
        print(f'Took you {guesses} guesses')
        return True
    return False
    

easy_mode = Mode("Easy", easy)
medium_mode = Mode("Medium", medium)
hard_mode = Mode("Hard", hard)
modes = [easy_mode, medium_mode, hard_mode]
guess = Game("Guessing game", modes)