'''
The Hangman is a classic word-guessing game where
players attempt to guess a word letter by letter.
You can define number of attempts by yourself.
Please display how many attempts are left and if
the guess was correct or wrong
'''
import random
from colorama import Fore, Style

hangman = (
        '''
 ________
    |/     
    |  
    |           
    |          
    |      
    |               
    |___
''',
    '''
 ________
    |/   |     
    |  
    |           
    |          
    |      
    |               
    |___
''',
    '''
 ________
    |/   |     
    |   (_)    
    |           
    |     
    |        
    |               
    |___
''',
    '''
 ________
    |/   |     
    |   (_)    
    |    |          
    |    |  
    |      
    |               
    |___
''',
    '''
 ________
    |/   |     
    |   (_)    
    |   /|          
    |    |        
    |          
    |               
    |___
''',
    '''
 ________
    |/   |     
    |   (_)    
    |   /|\\         
    |    |        
    |      
    |               
    |___
''',
    '''
 ________
    |/   |     
    |   (_)    
    |   /|\\           
    |    |        
    |   /        
    |               
    |___
''',
    '''
 ________
    |/   |     
    |   (_)    
    |   /|\\           
    |    |        
    |   / \\       
    |               
    |___
'''
)

print("Heeey you! You have 7 attempts to guess a mystery word. Please, don't let me hanging!")
print(hangman[0])

def choose_word(): #list with words, random word gets chosen
    random_word_list = ["Barbarian", "Wizard", "Sorcerer", "Fighter", "Rogue", "Cleric", "Druid", "Monk", "Paladin", "Ranger", "Bard", "Warlock", "Artificer"]
    random_word = random.choice(random_word_list).lower()
    print("The mystery word is:")
    for i in random_word:
        print("_", end=" ")
    #print(f"\n{random_word}") #TODO: remove this line
    return random_word

def hangman_game():
    word = choose_word()
    word_list = list(word)
    #print(word_list) #TODO: remove this line
    guessed = []
    all_guesses = []
    attempts = 7

    while attempts > 0:
        guess = input("\n\nGuess a letter: ").lower()

        if guess in all_guesses:
            print(f"You already guessed the letter '{guess}'. Try another one.")
            continue
        all_guesses.append(guess)

        if guess in word_list:
            guessed.append(guess)
            print(f"Correct! The letter {Fore.GREEN}'{guess}'{Style.RESET_ALL} is in the word. You have {attempts} attempts left.")
            for i in word_list:
                if i in guessed:
                    print(i, end=" ")            
                else:
                    print("_", end=" ")
            if set(word_list) == set(guessed):
                print(f"\n{Fore.YELLOW}Congratulations! You won! The word was '{word}'.{Style.RESET_ALL}")
                break
        else:
            attempts -= 1
            print(f"Wrong! The letter {Fore.RED}'{guess}'{Style.RESET_ALL} is not in the word. You have {attempts} attempts left.")
            print(hangman[7 - attempts])
    if attempts == 0:
        print(f"\n{Fore.RED}You lost! The word was '{word}'.{Style.RESET_ALL}")

    play_again = input("Do you want to play again? (y/n): ").lower()
    while play_again != "y" and play_again != "n":
        play_again = input("{Fore.RED} Invalid input. Please, try again. Do you want to play again? (y/n): {Style.RESET_ALL}").lower()
    if play_again == "y":
        hangman_game()
    elif play_again == "n":
        print("Goodbye!")

hangman_game()
