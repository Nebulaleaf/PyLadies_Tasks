'''
Chicken and Rabbits:
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
Output of the program should tell us how many rabbits and how many chickens we have. 
'''

heads = 35
legs = 94

if legs % 2 != 0 or legs < 2 * heads or legs > 4 * heads:
    print("No solution found with the given number of heads and legs.")
else:
    chicken = []
    rabbits = []
    for i in range(heads + 1):
        j = heads - i
        if 2 * i + 4 * j == legs:
            chicken.append(i)
            rabbits.append(j)

    if chicken and rabbits:
        print(f"Number of chickens: {chicken[0]}")
        print(f"Number of rabbits: {rabbits[0]}")
    else:
        print("No solution found with the given number of heads and legs.")
