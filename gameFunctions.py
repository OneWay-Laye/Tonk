#Imports for the game
from random import randint

#Random card In deck fuction
def randomCardFunc(deck, hand, cardsLeft):
    randomCardPosition = randint(0, cardsLeft -1)
    randomCard = deck[randomCardPosition]
    hand.append(randomCard)
    deck.remove(randomCard)
    cardsLeft -= 1

    return cardsLeft

# deal hands function to start game.
def dealHands(deck, player1Hand, player2Hand): 
    #with this deck i need to randomize the cards in which the players get.
    # start with the players hands
    cardsLeft = 52
    for card in range(10):

        # selects the Number card
        if card < 5:
            cardsLeft = randomCardFunc(deck, player1Hand, cardsLeft)
        else:
            cardsLeft = randomCardFunc(deck, player2Hand, cardsLeft)

#PickUp top card in Discard Pile
def pickUpDiscard(player, hand, discard_pile):
    topCard = discard_pile[0]
    hand.append(topCard)
    discard_pile.remove(topCard)
    print(f'You now have these 6 cards {hand}')
    checkPair = input('Do you have a pair? enter yes or no: ').upper()
    if checkPair == 'YES':
        pairData = pair(hand)
        pairMatchBool = pairData[0]
        pairCards = pairData[1]
        if pairMatchBool == True:
            print('You have a pair. lets remove those cards')
            for card in pairCards:
                hand.remove(card)
            print(f'Your new hand is {hand}')
        else:
            print('Those cards were not a match. Continue with your turn.')
    cardToDiscard = input('Enter the card that you want to discard: ')
    hand.remove(cardToDiscard)
    print(f'This is {player}\'s hand = {hand} after discarding {cardToDiscard}')
    discard_pile.insert(0, cardToDiscard)
    return 

#Pickup card from Deck function
def pickFromDeck(deck, player, hand, cardsLeft, discard_pile):
    cardsLeft = randomCardFunc(deck, hand, cardsLeft)
    print(f'{player} You now have these 6 cards {hand}')
    checkPair = input('Do you have a pair? enter yes or no: ').upper()
    if checkPair == 'YES':
        pairData = pair(hand)
        pairMatchBool = pairData[0]
        pairCards = pairData[1]
        if pairMatchBool == True:
            print('You have a pair. lets remove those cards')
            for card in pairCards:
                hand.remove(card)
            print(f'Your new hand is {hand}')
        else:
            print('Those cards were not a match. Continue with your turn.')
    cardToDiscard = input('Enter the card that you want to discard: ')
    hand.remove(cardToDiscard)
    print(f'This is {player}\'s hand = {hand} after discarding {cardToDiscard}')
    discard_pile.insert(0, cardToDiscard)
    return cardsLeft

#Count total cards fucntion
def countTotal(player1hand, player2hand):
    player1Total = 0
    player2Total = 0

    for card in player1hand:
        if (len(card) == 3) or (card[0] == 'K') or (card[0] == 'Q') or (card[0] == 'J'):
            player1Total += 10
        elif (card[0] == 'A'):
            player1Total += 1
        else:
            numOnCard = int(card[0])
            player1Total += numOnCard
    
    for card in player2hand:
        if (len(card) == 3) or (card[0] == 'K') or (card[0] == 'Q') or (card[0] == 'J'):
            player2Total += 10
        elif (card[0] == 'A'):
            player2Total += 1
        else:
            numOnCard = int(card[0])
            player2Total += numOnCard
        
    return [player1Total, player2Total]

# last Turn and playes drop card to see who have the least total face value
def drop(player1Hand, player2Hand):
    playerTotals = countTotal(player1Hand, player2Hand)
    player1Total = playerTotals[0]
    player2Total = playerTotals[1]
    if player1Total < player2Total:
        print(f'Player 1 Won The game with {player1Total} and Player 2 had {player2Total}')
    elif player2Total < player1Total:
        print(f'Player 2 Won The game with {player2Total} and Player 1 had {player1Total}')
    else:
        print(f'Its A TIE, Both players got {player1Total}')
    gameOver = True
    return gameOver

#Check to see if cards are a pair
def pair(hand):
    playerPair = []
    print('So you think you have a pair?')
    pairInput = input('Enter your 3 cards pair with a space in between: ')
    cardsToCheck = pairInput.split(' ')
    print(cardsToCheck)
    #loop through list
    suitList = []
    numberList = []
    faceList = []
    suitMatch = False
    numbersMatch: False
    match = False

    #first go through cards and add suits to 1 list and numbers to another
    for card in cardsToCheck:
        #check suits
        suitList.append(card[-1])
        if len(card) == 3:
            numberList.append(10)
            faceList.append(10)
        elif (card[0] in {'K', 'Q', 'J'}):
            faceList.append(card[0])
            numberList.append(10)
        elif card[0] == 'A':
            faceList.append(card[0])
            numberList.append(1)
        else:
            numberList.append(int(card[0]))
    print('suit list is',suitList)
    print('number list is', numberList)
    #now lets check match status
    if (suitList[0] == suitList[1] and suitList[0] == suitList[2]):
        print('The Suits Match! Lets check to see if your numbers are consecutive')
        suitMatch = True 
        if (abs(numberList[0] - numberList[1]) <= 2 or abs(numberList[0] - numberList[1]) <= 2) :
            print('The Numbers are consecutive. Looks like you have a pair')
            match = True
    
    # Since we changed the value of Face cards  to equal 10
    # We need to uses the 'cardsToCheck' list from above 
    # to see if numbers match
    elif (faceList[0] == faceList[1] and faceList[0] == faceList[2]):
        print('The Numbers Match! Lets see if you have different suits!')
        if(suitList[0] != suitList[1] and suitList[0] != suitList[2]):
            print('The Suits are Different! Looks like you have a pair')
            match = True

    return [match, cardsToCheck]

# this will be the code for each round.
def playerTurn(gameOver, round, deck, player1Hand, player2Hand, discard_pile, cardsLeft):

    #while not gameOver:
    if (round % 2 != 0):
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
        print(f'{player} You now have these 6 cards {hand}')
        checkPair = input('Do you have a pair? enter yes or no: ').upper()
        if checkPair == 'YES':
            pairData = pair(hand)
            pairMatchBool = pairData[0]
            pairCards = pairData[1]
            if pairMatchBool == True:
                print('You have a pair. lets remove those cards')
                for card in pairCards:
                    hand.remove(card)
                print(f'Your new hand is {hand}')
            else:
                print('Those cards were not a match. Continue with your turn.')
        cardToDiscard = input('Enter the card that you want to discard: ')
        hand.remove(cardToDiscard)
        print(f'This is {player}\'s hand = {hand} after discarding {cardToDiscard}')
        discard_pile.insert(0, cardToDiscard)
        print(discard_pile[0])
    else:
        #give player decision to drop, pull from pile, or pull from the deck
        print(f'{player} its your turn, and here is your hand {hand}')
        print(f"The Top card in the Discard Pile is {discard_pile[0]}")
        print("Enter Deck to pick a card from the Deck")
        print("Enter Pile to pick a card from the Discard Pile")
        print("Enter Drop to drop your cards to see if you win.")
        playerMove = input('Enter Your Choice Here: ')
        playerMoveUpper = playerMove.upper()
        
        if playerMoveUpper == 'PILE':
            pickUpDiscard(player, hand, discard_pile)
        elif playerMoveUpper == 'DECK':
            cardsLeft = pickFromDeck(deck, player, hand, cardsLeft, discard_pile)
            countTotal(player1Hand, player2Hand)
        elif playerMoveUpper == 'DROP':
            gameOver = drop(player1Hand, player2Hand)

    round += 1

    return [round, cardsLeft, gameOver]