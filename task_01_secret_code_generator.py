'''
**Task #1: Secret Code Generator**

Create a Python program that generates a secret code based on user input. The program should prompt the user to enter a word or phrase and then generate a secret code based on the following rules: 
1.    Each letter in the input word should be replaced by a corresponding code.
2.    The code for each letter is determined by its position in the alphabet (1-indexed) multiplied by 2.
3.    If the letter is a vowel (a, e, i, o, u), the code should be doubled.
4.    If the letter is uppercase, the code should be tripled.

Your task is to write a Python program that accomplishes the above requirements. Additionally, your program should handle both uppercase and lowercase letters. 

*Example:*
Enter a word or phrase: dasha 
Secret Code: 8 4 38 16 4
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']
CODE_MULTIPLIER = 2
VOWEL_MULTIPLIER = 2
UPPERCASE_MULTIPLIER = 3

def get_secret_code(word):
    secret_code = []
    for letter in word:
        if letter.lower() in alphabet:
            index = alphabet.index(letter.lower()) + 1
            code = index * CODE_MULTIPLIER
            if letter.lower() in vowels:
                code *= VOWEL_MULTIPLIER
            if letter.isupper():
                code *= UPPERCASE_MULTIPLIER
            secret_code.append(str(code))
    return ' '.join(secret_code)

def main():
    user_input = input("Enter a word or phrase: ")
    secret_code = get_secret_code(user_input)
    print(f"Secret Code: {secret_code}")

main()