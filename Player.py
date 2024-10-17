import random as r

class Player:
    def __init__(self, id, dice):
        self.id = id
        self.dice = [0] * int(dice)
        self.diceTotal = {1:0, 2:0, 3:0, 4:0}

    def __str__(self):
        return f"Player {self.id}: {self.dice} dice left"
    
    def randomiseDice(self):
        for die in range(len(self.dice)):
            self.dice[die] = r.randrange(1,5)

        self.diceTotal = {1:0, 2:0, 3:0, 4:0}

    def removeDice(self):
        self.dice.pop()

    def diceRemaining(self):
        return len(self.dice)

    def showDice(self):
        return self.dice
    
    def countDice(self):
        if self.diceTotal == {1:0, 2:0, 3:0, 4:0}:
            for die in self.dice:
                self.diceTotal[die] += 1
        
        return self.diceTotal