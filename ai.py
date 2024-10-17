import math as m
from gameLogic import previousBet, player, ai

# How much risk the AI will take
risk = 0.5

def evaluatePreviousBet():
    global previousBet
    global player
    global ai
    global risk

    # Difference in a dice value present verus betted
    diceDifference = previousBet[0] - ai.countDice()[previousBet[1]]

    if diceDifference > 0:
        # cal odds of them having the missing dice value
        results = calculateOdds(len(player.dice), diceDifference)
        if results < risk:
            return False
    
    # Bet is valid
    return True

def decideBet():
    global player
    global ai
    global previousBet

    bestBet = [0,[0,0]]
    for key, value in ai.countDice():
        # Determines how many dice are needed for a valid bet
        successesNeeded = previousBet[0] - value
        if key <= previousBet[1]:
            successesNeeded += 1

        # Sets the bet odds to 100%
        if successesNeeded <= 0:
            bestBet = [1,[successesNeeded + previousBet[0], key]]
            continue

        betOdds = calculateOdds(player.diceRemaining, successesNeeded)
        if betOdds > bestBet[0]:
            bestBet = [betOdds, [successesNeeded + previousBet[0], key]]
    
    return bestBet[1]

# Binomial distribution formula determining chance of atleast x dice of a value have been rolled
def calculateOdds(unknownDice, successes):
    total = 0
    for target in range(successes, 5):
        print(target)
        total += m.factorial(unknownDice) / (m.factorial(unknownDice - target) * m.factorial(target)) * pow(0.25, target) * pow(0.75, unknownDice - target)

    return total