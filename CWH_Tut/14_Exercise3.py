# no of guesses 9
# print no of guesses left
# No of guesses he took to finish
# game over

n = 18
num_of_guess = 1
while num_of_guess <=5:
    guessed_num = int(input("Guess the number\n"))
    if guessed_num > 18:
        print("You are entering a greater number")
    elif guessed_num < 18:
        print("You are entering a smaller number")
    else:
        print("You Won!")
        print("Guess you took ", num_of_guess)
        break
    print("Guess left ", 5 - num_of_guess)
    num_of_guess += 1

if num_of_guess > 5:
    print("Game Over!")