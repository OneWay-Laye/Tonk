'''
In the project we will create the Card game tonk.
How the game works.
    1. each player starts with 5 cards 
    2. the first player will draw from the deck
        now that player has 6 cards and must chekc too see if he has a pair and if he doesnt
        he must pick a card of his choosing to drop.

        *Any pair inculdes three of a kind or consecutive numbers.*

    3. After the player drops their card it then ends their turn.
    4. The next player has a choice to Pick up from the deck or the most recent card added to 
        the discard pile.
        this player then will continue on with the rules stated in step 2.
    
    5. When players find a pair, they will only have 2 cards left. the Goal of the game is 
        to have the lowest number (face value) of cards left when the game the player
        "DROPS".
    
    6. A player Can drop at the beginning of the game is they are confident in the hand.
'''

from gameFunctions import dealHands, playerTurn

deck = ['AC', 'AD', 'AH', 'AS',
        '2C', '2D', '2H', '2S',
        '3C', '3D', '3H', '3S',
        '4C', '4D', '4H', '4S',
        '5C', '5D', '5H', '5S',
        '6C', '6D', '6H', '6S',
        '7C', '7D', '7H', '7S',
        '8C', '8D', '8H', '8S',
        '9C', '9D', '9H', '9S',
        '10C', '10D', '10H', '10S',
        'JC', 'JD', 'JH', 'JS',
        'QC', 'QD', 'QH', 'QS',
        'KC', 'KD', 'KH', 'KS']

gameOver = False
round = 1
playerOneHand = []
playerTwoHand = []
discard_pile = []

'''
game order
'''
# First we deal hands
dealHands(deck, playerOneHand, playerTwoHand)

'''
 Second go through turn 1 which is different because the player 
 doesnt have a choice of picking up from discard deck
'''
while not gameOver: 
    round = playerTurn(gameOver, round, deck, playerOneHand, playerTwoHand, discard_pile)
