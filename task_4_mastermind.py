'''
Write a program that randomly generates a 4 digit number. The user has maximum 10 tries to guess the number.
If any of the digit guessed is wrong, print "A" to indicate wrong guess.
If the digit is guessed correctly but in the wrong position, print "B".
If the digit guessed is both the correct value and position, print "C".
'''

import random

# Generate a random 4 digit number
number = random.randint(1, 9999)
four_digit_number = "{:04d}".format(number)
print(four_digit_number) # For testing purposes

# User has 10 tries to guess the number
guess_tracker = 10
while guess_tracker <= 10 and guess_tracker > 0:
    user_guess = input("Enter your guess: ")

    # Check if the user input is a 4 digit number
    if len(user_guess) != 4:
        print("Please enter a 4 digit number.")
        continue

    if user_guess == four_digit_number:
        print("Awesome, that's the correct number!")
        break

    elif user_guess != four_digit_number:
        feedback_string = ""
        for i in range(4):
            if user_guess[i] == four_digit_number[i]:
                feedback_string += "C"
            elif user_guess[i] in four_digit_number:
                feedback_string += "B"
            else:
                feedback_string += "A"
        print(feedback_string)

        guess_tracker -= 1
        print(f"You have {guess_tracker} guesses left.")