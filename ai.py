import math as m
from gameLogic import previousBet, player, ai

# How much risk the AI will take
risk = 0.5

def evaluatePreviousBet():
    global previousBet
    global player
    global ai
    global risk

    # How many of my dice match the bet
    matchingDice = 0
    for i in range(len(ai.dice)):
        if ai.dice[i] == previousBet[1]:
            matchingDice += 1
    
    diceDifference = previousBet[0] - matchingDice
    if diceDifference > 0:
        # cal odds of them having the missing dice value
        results = calculateOdds(len(player.dice), diceDifference)
        if results < risk:
            return False
    
    # Bet is valid
    return True

# Binomial distribution formula determining chance of atleast x dice of a value have been rolled
def calculateOdds(unknownDice, successes):
    total = 0
    for target in range(successes, 5):
        print(target)
        total += m.factorial(unknownDice) / (m.factorial(unknownDice - target) * m.factorial(target)) * pow(0.25, target) * pow(0.75, unknownDice - target)

    return total