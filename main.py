from calendar import c
import random
import string
from traceback import print_last

cardTypes = ("hearts", "clubs", "spades", "diamonds")
cardValues = ("ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king")

cards = []

class Card(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

def addDeck():
    for x in range(0, len(cardTypes)):
        for y in range(0, len(cardValues)):
            cards.append(Card(cardTypes[x], cardValues[y]))

def init(decks):
    for x in range(0, int(decks)):
        addDeck()

def main():
    init(4)

    #for x in range(0, len(cards)):
        #print(f"{x} : {cards[x].type}, {cards[x].value}")

    x = input("Welcome to Blackjack, type s to start\n")

    if (x != "s"):
        print("Ok quitting")  
        exit(0)
    else:
        pass



if __name__ == "__main__":
    main()