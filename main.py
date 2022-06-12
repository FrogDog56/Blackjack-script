import random as r

#TODO fix more than one ace issue
#TODO add split and double

cardTypes = ("hearts", "clubs", "spades", "diamonds")
cardNames = ("ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king")
cardValues = {
                "ace" : 11, 
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
    ace = 0
    for x in range(0, len(hand)):
        if (hand[x].value == "ace"):
            ace += 1

    for x in range(0, len(hand)):
        total += cardValues.get(hand[x].value)

    if (total > 21):
        total -= 10 * ace

    return total

def dealCard(hand):
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
        return True
    return False

def init():
    #4 is default because most casinos play blackjack with a four deck shoe
    for x in range(0, 4):
        addDeck()

def main():
    run = True

    init()
    chips = 10000

    x = input("Welcome to Blackjack, type s to start\n")

    if (x.lower() != "s"):
        print("Ok quitting")  
        exit(0)
    else:
        pass

    print(f"You have {chips} chips, good luck!")

    while run:

        x = input("Place your bet\n")
        bet = int(x)

        if ((chips - bet) > 0):
            chips -= bet
            print(f"Your bet is {x} chips\n")
        else:
            print("You don't have enough chips to place that bet!\n")

        for x in range(0, 2):
            dealCard(dealerHand)
            dealCard(playerHand)

        if (total(playerHand) != 21):
            print(f"The dealers visible card is {dealerHand[0].value} of {dealerHand[0].type}")
            print(f"You have {total(playerHand)}")

            stand = False

            while stand == False:
                x = input("Would you like to hit(h) or stand(s)\n")

                if (x.lower() == "h"):
                    hit(playerHand)
                    print(f"Your total is now {total(playerHand)}")
                else:
                    stand = True
                    break

        while total(dealerHand) < 17:
            hit(dealerHand)

        if (total(playerHand) == 21 and len(playerHand) == 2):
            print("You have blackjack you win!")
            chips += bet * 2.5
        elif (total(dealerHand) == 21 and len(dealerHand) == 2):
            print("Dealer has blackjack you lose!")
        elif (total(playerHand) > 21):
            print("You have gone bust you lose!")
        elif (total(dealerHand) > 21):
            print("You win, the dealer has gone bust!")
            chips += bet * 2
        else:
            if (total(dealerHand) == total(playerHand)):
                print(f"It is a draw you both have {total(playerHand)}")
                chips += bet
            elif (total(dealerHand) < total(playerHand)):
                print(f"You win you have {total(playerHand)}")
                chips += bet * 2
            else:
                print(f"Dealer wins with {total(dealerHand)}")

        print(f"You now have {chips} chips!")

        dealerHand.clear()
        playerHand.clear()

        print("<--------------------------------->")

if __name__ == "__main__":
    main()