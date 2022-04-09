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
    total = 0
    for x in range(0, len(hand)):
        total += cardValues.get(hand[x].value)

    return total

def dealHand(hand):
    randomIndex = r.randint(0, len(cards))
    randomCard = cards[randomIndex]
    del cards[randomIndex]
    hand.append(randomCard)

def hit(hand):
    randomIndex = r.randint(0, len(cards))
    randomCard = cards[randomIndex]
    del cards[randomIndex]
    hand.append(randomCard)
    bustCheck(hand)

def bustCheck(hand):
    if (total(hand) > 21):
        print("You have gone bust, you lose!")
        print("Closing program......")
        exit(0)
    else:
        pass

def init():
    #4 is default because all casinos play blackjack with four decks shuffled together
    for x in range(0, 4):
        addDeck()

def main():
    run = True
    init()

    x = input("Welcome to Blackjack, type s to start\n")

    if (x.lower() != "s"):
        print("Ok quitting")  
        exit(0)
    else:
        pass

    for x in range(0, 2):
        dealHand(dealerHand)
        dealHand(playerHand)

    print(f"The dealers visible card is {dealerHand[0].value} of {dealerHand[0].type}")
    print(f"You have {total(playerHand)}")

    x = input("Would you like to hit(h) or stand(s)\n")

    if (x.lower() == "h"):
        hit(playerHand)
        print(f"Your total is now {total(playerHand)}")

if __name__ == "__main__":
    main()