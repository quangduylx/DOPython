import random
name=input("Enter your name: ")
print('Hello,',name,'!')
print('''Welcome to my Number Guessing Game!
In this game, a number between 1 and 99 will be randomly generated.
You will win if you guess the number correctly''')
rcheck=input('Are you ready? ')
def game():
    number=random.randint(1,99)
    gtaken=0
    for gtaken in range(99):
        print('A random number has been generated. What do you think it is?')
        guess=int(input())
        if guess<number:
            print('Your guess is too low! Try again!')
        elif guess>number:
            print('Your guess is too high! Try again!')
        else:
            break
    if guess==number:
        gtaken=gtaken+1
        print('Well done,',name,'!')
        print('You guessed the right number in',gtaken,'guesses!')
if rcheck=='yes' or rcheck=='y' or rcheck=='Yes':
    game()
    print('Would you like to play again?')
    again = input()
    while again=='yes'or again=='y' or again=='Yes':
        game()
        print('Would you like to play again?')
        again=input()
    else:
        print('Done')
        print('See ya!')
else:
    print('See ya!')