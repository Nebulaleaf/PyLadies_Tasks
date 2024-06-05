'''
Chicken and Rabbits:
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
Output of the program should tell us how many rabbits and how many chickens we have. 
'''

heads = 35
legs = 94
chicken = []
rabbits = []

for i in range(heads + 1):
    j = heads - i
    if 2 * i + 4 * j == legs:
        chicken.append(i)
        rabbits.append(j)

if chicken and rabbits:  # If the lists are not empty, a solution was found
    print(f"Number of chickens: {chicken[0]}")
    print(f"Number of rabbits: {rabbits[0]}")
else:  # If the lists are empty, no solution was found
    print("No solution found with the given number of heads and legs.")


