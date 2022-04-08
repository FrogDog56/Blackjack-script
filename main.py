import random as r

cardTypes = ("hearts", "clubs", "spades", "diamonds")
cardNames = ("ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king")
cardValues = {
                "ace" : 1, 
                "2" : 2, 
                "3" : 3, 
                "4" : 4,
                "5" : 5,
                "6" : 6,
                "7" : 7,
                "8" : 8,
                "9" : 9,
                "10" : 10,
                "jack" : 10,
                "queen" : 10,
                "king" : 10,
                }

cards = []

dealerHand = []
playerHand = []

class Card(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

def addDeck():
    for x in range(0, len(cardTypes)):
        for y in range(0, len(cardValues)):
            cards.append(Card(cardTypes[x], cardNames[y]))

def total(hand):
    return cardValues.get(hand[0].value) + cardValues.get(hand[1].value)

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

    for x in range(0, 2):
        randomCard = cards[r.randint(0, len(cards))]
        dealerHand.append(randomCard)

    for x in range(0, len(dealerHand)):
        print(f"The dealer has {dealerHand[x].type} {dealerHand[x].value}")
        print(total(dealerHand))

if __name__ == "__main__":
    main()