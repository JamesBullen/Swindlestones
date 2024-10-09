import random as r

class Player:
    def __init__(self, id, dice):
        self.id = id
        self.dice = [0] * int(dice)

    def __str__(self):
        return f"Player {self.id}: {self.dice} dice left"
    
    def randomiseDice(self):
        for die in range(len(self.dice)):
            self.dice[die] = r.randrange(1,5)

    def removeDice(self):
        self.dice.pop()