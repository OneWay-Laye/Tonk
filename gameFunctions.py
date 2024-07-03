#Imports for the game
from random import randint

# deal hands function to start game.
def dealHands(deck): 
    #with this deck i need to randomize the cards in which the players get.
    # start with the players hands
    cardsLeft = 51
    player1Hand = []
    player2Hand = []

    while len(player1Hand) < 5:

        # selects the Number card
        randomCardPosition = randint(0, cardsLeft)

        #sets it to the card in the deck
        randomCard = deck[randomCardPosition]
        if randomCard not in deck:
            randomCardPosition = randint(0,51)
        else:
            player1Hand.append(randomCard)
            deck.remove(randomCard)
            cardsLeft -= 1
    
    # Now we deal player twos hand
    while len(player2Hand) < 5:

        # selects the Number card
        randomCardPosition = randint(0, cardsLeft)

        #sets it to the card in the deck
        randomCard = deck[randomCardPosition]
        if randomCard not in deck:
            randomCardPosition = randint(0,51)
        else:
            player2Hand.append(randomCard)
            deck.remove(randomCard)
            cardsLeft -= 1
    print(f' player 1\' hand is {player1Hand}')
    print(f' player 2\' hand is {player2Hand}')
    return player1Hand