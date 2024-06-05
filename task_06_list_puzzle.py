'''
Write a Python program to compute the largest product of three integers from a given list of integers.
Sample input:
[-10, -20, 20, 1]
[-1, -1, 4, 2, 1]
[1, 2, 3, 4, 5, 6]

Sample output:
4000
8
120
'''


integers = [int(x) for x in input("Enter at least four (4!) integers separated by commas. Those integers can also be negative: ").split(", ")]
print(f"Your list of integers: {integers}")

if len(integers) < 4:
    print("Common, I wanted 4 integers of you.")
else:
    negative = []
    positive = []
    for i in integers:
        if i < 0:
            negative.append(i)
        else:
            positive.append(i)

three_biggest = []
if len(negative) >= 2:
    negative.sort()
    three_biggest.extend(negative[:2])
    if len(positive) >= 1:
        positive.sort(reverse=True)
        three_biggest.append(positive[0])
else:
    positive.sort(reverse=True)
    three_biggest.extend(positive[:3])

#print(f"Negative integers: {negative}") # just for checking
#print(f"Positive integers: {positive}") # just for checking

print(f"The three biggest integers from the list are: {three_biggest}")
print(f"The largest product of three integers from the list is: {three_biggest[0] * three_biggest[1] * three_biggest[2]}")

