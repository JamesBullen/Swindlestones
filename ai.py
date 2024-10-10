import math as m

def calculateOdds(unknownDice, successes):
    total = 0
    for target in range(successes, 5):
        print(target)
        total += m.factorial(unknownDice) / (m.factorial(unknownDice - target) * m.factorial(target)) * pow(0.25, target) * pow(0.75, unknownDice - target)

    return total

print(calculateOdds(4,2))