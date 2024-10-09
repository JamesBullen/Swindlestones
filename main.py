from gameLogic import main as Start

def main():
    print("Welcome to Swindlestones: Console Line Edition™")

    startingDice = int(input("How many dice to start with? "))
    Start(startingDice)

main()