import random as r
import Player as p

player = None
ai = None
startingDice = 0
previousBet = [0, 0]

def main():
    global player
    global ai
    global startingDice

    while True:
        startingDice = int(input("How many dice to start with? "))
        player = p.Player(1, startingDice)
        ai = p.Player(2, startingDice)

        while True:
            result = decideFirstPlayer()

            if result != False:
                break
        
        turnHandler(result)

        answer = input("Play another game? y/n ")
        if answer.lower() == "n":
            break

def decideFirstPlayer():
    global player
    global ai

    diceOne = r.randrange(1,5)
    diceTwo = r.randrange(1,5)

    print(f"Player rolled {diceOne}, and AI rolled {diceTwo}")

    if diceOne > diceTwo:
        print("Player goes first")
        return player
    elif diceOne < diceTwo:
        print("AI goes first")
        return ai
    else:
        print("It's a tie")
        return False

def turnHandler(startingPlayer):
    global player
    global ai
    global startingDice

    nextplayer = startingPlayer
    
    # Rolls players dice for the first time
    resetDice()

    while True:
        nextplayer = nextBet(nextplayer)

        result = checkForWin()
        if result == False:
            continue
        else:
            print(f"{result.id} wins")
            break

def nextBet(better):
    global player
    global ai
    global startingDice
    global previousBet

    # Checks if previous bet is the max bet
    # If so, forces a call
    if previousBet == [4, startingDice]:
        return call(better)

    while True:       
        bet = input("Place your bet ")

        if bet == "call":
            return call(better)

        # Is the input valid?
        try:
            formatedBet = list(map(int, bet.split(" ")))

            # Clamps values into valid range
            formatedBet[0] = min(max(1, formatedBet[0]), startingDice)
            formatedBet[1] = min(max(1, formatedBet[1]), 4)
        except:
            print("Invalid formatting")
            continue

        # Is bet bigger than previous?
        if (formatedBet[1] >= previousBet[1] or (formatedBet[0] > previousBet[0] and formatedBet[0] == previousBet[1])) and formatedBet != previousBet:
            previousBet = formatedBet
            break
        else:
            print("Invalid bet")
            continue

    # Tells which player should go next
    if better == player:
        return ai
    else:
        return player

def call(callingPlayer):
    global player
    global ai
    global previousBet

    if previousBet == [0, 0]:
        print("A bet must be placed first before you can call")
        return callingPlayer

    if callingPlayer == player:
        otherPlayer = ai
    else:
        otherPlayer = player

    # Combines dice pools and counts total of each number
    allDice = player.dice + ai.dice
    diceTotals = {1:0, 2:0, 3:0, 4:0}
    for die in allDice:
        diceTotals[die] += 1

    # Resets both players dice, as results have now been stored
    resetDice()

    # Checks if bet is true or not
    if diceTotals[previousBet[1]] >= previousBet[0]:
        otherPlayer.removeDice()
        return otherPlayer
    else:
        callingPlayer.removeDice()
        return callingPlayer
    
def resetDice():
    global player
    global ai

    player.randomiseDice()
    ai.randomiseDice()

    print(f"You've rolled {player.dice}")

def checkForWin():
    global player
    global ai

    if len(player.dice) == 0:
        return ai # Player loses
    
    if  len(ai.dice) == 0:
        return player # AI loses
    
    return False