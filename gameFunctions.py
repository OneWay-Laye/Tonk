#Imports for the game
from random import randint

def randomCardFunc(deck, hand, cardsLeft):
    randomCardPosition = randint(0, cardsLeft)
    randomCard = deck[randomCardPosition]
    hand.append(randomCard)
    deck.remove(randomCard)
    cardsLeft -= 1

    return cardsLeft

# deal hands function to start game.
def dealHands(deck, player1Hand, player2Hand): 
    #with this deck i need to randomize the cards in which the players get.
    # start with the players hands
    cardsLeft = 51
    for card in range(10):

        # selects the Number card
        if card < 5:
            cardsLeft = randomCardFunc(deck, player1Hand, cardsLeft)
        else:
            cardsLeft = randomCardFunc(deck, player2Hand, cardsLeft)


# this will be the code for each round.
def playerTurn(gameOver, round, deck, player1Hand, player2Hand, discard_pile):

    #while not gameOver:
    cardsLeft = 41
    if (round % 2 != 0) and gameOver == False:
        player = "Player 1"
        hand = player1Hand
    else: 
        player = "Player 2"
        hand = player2Hand
       
    print(f'{player} your cards are {hand}')
    if round == 1:
        print('Since its the first round you must draw from the deck to start the game.')
    # selects the Number card
    randomCardPosition = randint(0, cardsLeft)

    #sets it to the card in the deck
    randomCard = deck[randomCardPosition]
    hand.append(randomCard)
    deck.remove(randomCard)
    cardsLeft -= 1
    print(f'You now have these 6 cards {hand}')
    cardToDiscard = input('Enter the card that you want to discard: ')
    hand.remove(cardToDiscard)
    print(f'This is {player}\'s hand = {hand} after discarding {cardToDiscard}')
    discard_pile.insert(0, cardToDiscard)
    print(discard_pile)
    round += 1

    return round