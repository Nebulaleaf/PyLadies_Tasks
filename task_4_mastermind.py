'''
Write a program that randomly generates a 4 digit number. The user has maximum 10 tries to guess the number.
If any of the digit guessed is wrong, print "A" to indicate wrong guess.
If the digit is guessed correctly but in the wrong position, print "B".
If the digit guessed is both the correct value and position, print "C".
'''

import random
from colorama import Fore, Style
from matplotlib.pylab import f

# Explain the game to the user
print(
    f"{Fore.RED}Welcome Mastermind!\n"
    f"{Style.RESET_ALL}\n"
    f"I've created a four digit number.\n"
    f"\n"
    f"You have {Fore.GREEN}10 tries{Style.RESET_ALL} to guess the number.\n"
    f"Each time you guess, I will give you feedback.\n"
    f"If a digit is {Fore.GREEN}correct and in the right position{Style.RESET_ALL}, I will say {Fore.GREEN}'C'{Style.RESET_ALL}.\n"
    f"If a digit is {Fore.YELLOW}correct but in the wrong position{Style.RESET_ALL}, I will say {Fore.YELLOW}'B'{Style.RESET_ALL}.\n"
    f"If a digit is {Fore.RED}incorrect{Style.RESET_ALL}, I will say {Fore.RED}'A'{Style.RESET_ALL}.\n"
    f"{Fore.GREEN}Good luck!{Style.RESET_ALL}\n"
    )

number = random.randint(1, 9999)
four_digit_number = "{:04d}".format(number)

#print(four_digit_number) # For testing purposes

# User has 10 tries to guess the number
guess_tracker = 10
while guess_tracker <= 10 and guess_tracker > 0:
    user_guess = input("Enter your guess: ")

    # Check if the user input is a 4 digit number
    if len(user_guess) != 4:
        print("Please enter a 4 digit number.")
        continue

    if user_guess == four_digit_number:
        print(
            f"{Fore.GREEN}Awesome, {four_digit_number} is the correct number!{Style.RESET_ALL}"
            )
        break

    elif user_guess != four_digit_number:
        feedback_string = ""
        for i in range(4):
            if user_guess[i] == four_digit_number[i]:
                feedback_string += f"{Fore.GREEN}C{Style.RESET_ALL}"
            elif user_guess[i] in four_digit_number:
                feedback_string += f"{Fore.YELLOW}B{Style.RESET_ALL}"
            else:
                feedback_string += f"{Fore.RED}A{Style.RESET_ALL}"
        print(feedback_string)

        guess_tracker -= 1
        print(f"You have {guess_tracker} guesses left.")