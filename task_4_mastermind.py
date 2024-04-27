import random
from colorama import Fore, Style

def explain_game():
    '''
    Explain the game to the user.
    '''
    print(
        f"{Fore.RED}Welcome Mastermind!\n"
        f"{Style.RESET_ALL}\n"
        f"I've created a four-digit number.\n"
        f"\n"
        f"You have {Fore.GREEN}10 tries{Style.RESET_ALL} to guess the number.\n"
        f"Each time you guess, I will give you feedback.\n"
        f"If a digit is {Fore.GREEN}correct and in the right position{Style.RESET_ALL}, I will say {Fore.GREEN}'C'{Style.RESET_ALL}.\n"
        f"If a digit is {Fore.YELLOW}correct but in the wrong position{Style.RESET_ALL}, I will say {Fore.YELLOW}'B'{Style.RESET_ALL}.\n"
        f"If a digit is {Fore.RED}incorrect{Style.RESET_ALL}, I will say {Fore.RED}'A'{Style.RESET_ALL}.\n"
        f"{Fore.GREEN}Good luck!{Style.RESET_ALL}\n"
        )

def generate_random_number():
    '''
    Generate a random 4-digit number."
    '''   
    return "{:04d}".format(random.randint(1, 9999))

def get_user_guess():
    '''
    Prompt the user to enter their guess.
    '''
    return input("Enter your guess: ")

def provide_feedback(user_guess, actual_number):
    '''
    Provide feedback on the user's guess.
    '''
    feedback_string = ""
    for i in range(4):
        if user_guess[i] == actual_number[i]:
            feedback_string += f"{Fore.GREEN}C{Style.RESET_ALL}"
        elif user_guess[i] in actual_number:
            feedback_string += f"{Fore.YELLOW}B{Style.RESET_ALL}"
        else:
            feedback_string += f"{Fore.RED}A{Style.RESET_ALL}"
    print(feedback_string)

def play_game():
    '''
    Play the Mastermind game.
    '''
    explain_game()
    actual_number = generate_random_number()
    guess_tracker = 10
    while guess_tracker > 0:
        user_guess = get_user_guess()
        if len(user_guess) != 4 or not user_guess.isdigit():
            print("Please enter a valid 4-digit number.")
            continue
        if user_guess == actual_number:
            print(
                f"{Fore.GREEN}Awesome, {actual_number} is the correct number!{Style.RESET_ALL}"
                )
            break
        else:
            provide_feedback(user_guess, actual_number)
            guess_tracker -= 1
            if guess_tracker == 0:
                print(
                    f"{Fore.RED}Sorry, you're out of guesses. The correct number was {actual_number}.{Style.RESET_ALL}"
                    )
                break
            else:
                print(f"You have {guess_tracker} guesses left.")          

# Start the game
play_game()
