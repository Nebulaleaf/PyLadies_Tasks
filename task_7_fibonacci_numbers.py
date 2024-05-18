'''
Write a program that asks the user how many Fibonacci numbers to
generate and then generates them. Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.

Hint: The Fibonacci sequence is a sequence of numbers where the next number
in the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, 21, 34, …
'''
def fibonacci_numbers(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b

n = int(input("This program generates Fibonacci numbers. How many Fibonacci numbers do you want to generate? "))
fibonacci_numbers(n)

