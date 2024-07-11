# Tonk Card Game

## Purpose of the Project
I decided to create the Tonk card game to excercise my Python3 knowledge with something I am familiar with. I knew that it would not be to dificult of a game to program so I jumped right in.

## Rules Of The Game
1. Each player starts off with 5 cards
2. Player One starts their hand by either pulling a card from the deck or pulling a card from the discard pile.
3. Once the player pulls the card, they decide which card they would like to discard, and then Player 2 follows the same path.
4. At anytime each player has the option has to either Spread or Go Out.
    - Spread: A laid down run of three or more cards from the same suit in sequence (e.g. a 7 of Hearts, 8 of Hearts, and 9 of Hearts). A spread is also a book of at least three identically ranked cards from different suits (e.g. three Jacks).
    - Going Out: A player could "Drop" their cards and add up the total of the face value of the cards. Whoever has the lowest total wins.

## Coding Progress
This was a journey of a project. I hit a couple road blocks along the way but was very determined to find the solution.

I started off by working on the main page of the project. I knew that I needed to create A list for deck and add the 52 cards to it. I also knew that I needed to create an empty list for both players hands.

Once I got to this point, I knew that i needed to create a function for the start of the game which is dealing each player their 5 cards. I created another file to house all of my function so that my main file would not be cluttered.

In that gameFunctions file I started and created the deal hands function which housed the randondom card function. The random card function basically takes a random card from the deck and adds it to the players hand. 



## Knowledge Learned
1. randomint() function with 2 parameters (inclusive number, Number above Max) and  gives you a random integer between your parameters.

2. Try and Except in a Loop.