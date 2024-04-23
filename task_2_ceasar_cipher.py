'''
Task #2: Caesar Cipher

Caesar's cipher is a simple encryption technique, in which the plaintext character is replaced by a letter some fixed number of positions down the alphabet.

For example, with a right shift of 3, A would be replaced by D, B would become E, and so on.

Task:
Write a Python program to decode the following message: N qtaj uwtlwfrrnsl zxnsl Udymts, given that the key is 5. (Bearbeitet)
'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key = 5
cipher = 'N qtaj uwtlwfrrnsl zxnsl Udymts'

def ceasar_cipher(cipher, key):
    decrypted = ''
    for letter in cipher:
        if letter == ' ':
            decrypted += ' '
        else:
            if letter.isupper():
                index = alphabet.index(letter.lower())
                decrypted += alphabet[(index - key) % 26].upper()
            else:
                index = alphabet.index(letter.lower())
                decrypted += alphabet[(index - key) % 26]
    return decrypted

print(ceasar_cipher(cipher, key))
