'''
The Hangman is a classic word-guessing game where
players attempt to guess a word letter by letter.
You can define number of attempts by yourself.
Please display how many attempts are left and if
the guess was correct or wrong
'''
import random

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
    |   /|\         
    |    |        
    |      
    |               
    |___
''',
    '''
 ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   /        
    |               
    |___
''',
    '''
 ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___
'''
)

print("Heeey you! You have 7 attempts to guess a mystery word. Please, don't let me hanging!")
print(hangman[0])

def choose_word(): #list with words, random word gets chosen
    random_word_list = ["Barbarian", "Wizard", "Sorcerer", "Fighter", "Rogue", "Cleric", "Druid", "Monk", "Paladin", "Ranger", "Bard", "Warlock", "Artificer"]
    random_word = random.choice(random_word_list).lower()
    for i in random_word:
        print("_", end=" ")
        #print(f"\n{random_word}") #TODO: remote this line
    return random_word

def hangman_game():
    word = choose_word()
    word_list = list(word)
    guessed = []
    attempts = 7
    while attempts > 0:
        guess = input("\nGuess a letter: ").lower()
        if guess in word_list:
            guessed.append(guess)
            print(f"Correct! The letter '{guess}' is in the word.")
            for i in word_list:
                if i in guessed:
                    print(i, end=" ")
                else:
                    print("_", end=" ")
            if len(guessed) == len(set(word_list)):
                print("\nCongratulations! You guessed the word!")
                break
        else:
            attempts -= 1
            print(f"Wrong! The letter '{guess}' is not in the word. You have {attempts} attempts left.")
            print(hangman[7 - attempts])
    if attempts == 0:
        print(f"\nYou lost! The word was '{word}'.")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman_game()
    else:
        print("Goodbye!")

hangman_game()



