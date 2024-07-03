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
    
    return player1Hand, player2Hand



# this will be the code for each round.
def playerTurn(gameOver, round, deck, player1Hand, player2Hand):
    turn = 'player1'
    #while not gameOver:
    cardsLeft = 41
    if (round % 2 != 0) and gameOver == False:
        print('Player 1 its your turn.')
        print(f'Your cards are {player1Hand}')
        if round == 1:
            print('Since its the first round you must draw from the deck to start the game.')
            # selects the Number card
            randomCardPosition = randint(0, cardsLeft)

            #sets it to the card in the deck
            randomCard = deck[randomCardPosition]
            player1Hand.append(randomCard)
            deck.remove(randomCard)
            cardsLeft -= 1
            print(f'You now have these 6 cards {player1Hand}')
            cardToDiscard = input('Enter the card that you want to discard: ')
            print(cardToDiscard)
    else:
        print('its player twos turn')

    return