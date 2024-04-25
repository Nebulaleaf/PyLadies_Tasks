'''
Write a program that randomly generates a 4 digit number. The user has maximum 10 tries to guess the number.
If any of the digit guessed is wrong, print "A" to indicate wrong guess.
If the digit is guessed correctly but in the wrong position, print "B".
If the digit guessed is both the correct value and position, print "C".
'''

import random

number = random.randint(1, 9999)
four_digit_number = "{:04d}".format(number)
print(four_digit_number)



