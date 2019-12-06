# List of a deck of cards by suite and number
# inport random
import random
 
# import shuffle from random
from random import shuffle

# A Function for creating a Deck
def Deck():
    Deck = []

   for suit in ["Spades","Clubs","Diamonds","Hearts"]
        for rank in['A','2','3','4','5','6','7','8','9','T','J','Q','K']
            Deck.append(suit+rank)
    
   shuffle(Deck)
   return Deck
# A Function for counting the points
def pointCount(myCards):
myCount = 0
aceCount = 0

"""Assign value to Face Cards"""
for i in myCards:
    if(i[1] == 'J' or i[1] == 'Q' or i[1] == 'K' or i[1] == 'T'):
        myCount += 10
    elif(i[1] != 'A'):
        myCount += int(i[1])
    else: aceCount += 1
  
if(aceCount == 1 and myCount >= 10):
    myCount += 11
elif(aceCount != 0):
    myCount += 1
return myCount    

# A Function for creating the player and dealer hand
# Randomly generates two cards for the deck
# Display the hands
def createPlayingHand(Deck):
# Dealer Hand
hand1 = []
# Player Hand
hand2 = []
hand2.append(Deck.pop())
hand1.append(Deck.pop())
hand2.append(Deck.pop())
hand1.append(Deck.pop())

while(pointCount(hand)) <= 16:
    hand1.append(Deck.pop())
return[hand1, hand2]

# Game loop
game = " "
myDeck = Deck()
hands = CreatePlayingHand(myDeck)
dealer = hands[0]
player = hands[1]

while(game != "exit"):
    dealerCount=pointCount(dealer)
    playerCount=pointCount(player)
    print("Dealer has: ")
    print(dealer[0])
    print("Player, you have: ")
    print(player[1])
    if(playerCount == 21):
    print("BlackJack!")
    elif(playerCount > 21):
        print("Player Bust! with" + str(playerCount + " points, Dealer Wins!"))
        break
    elif(dealerCount > 21):
        print("Dealer Busts : with" + str(dealerCount) + " points, Player wins!")
        break
       game = raw_input("What would you like to do? H:Hit me, S:Stand")
       if(game == 'H'):
           player.append(myDeck.pop())
       elif(playerCount > dealerCount):
           print("Player wins with" + str(playerCount) + "points")
           print("Dealer has : " + str(dealer + "or" + str(dealerCount + "points")))
           break
       else:
           print("Dealer Wins! : ")
           


"""Assign values to A,J,Q,K"""
# J = 10
# Q = 10
# K = 10
# A = 1
# A = 11

"""Deal the hand first 'down' card"""
hand1(1)=np.random.randint(Deck)
hand2(1)=np.random.randint(Deck)

"""Deal the hand second 'up' card"""
hand1(2)=np.random.randint(Deck)
hand2(2)=np.random.randint(Deck)

"""Show dealer 'up' card and player's cards"""
Print("Dealer has x &", hand1(2))
Print("Player has ", hand2(1),hand2(2))

"""Create a probability function to determine the dealer's 'down' card"""
# p_hand1(1)=49!/52!
import numpy as np
import matplotlib.pyplot as plt
if 
    Ace = Deckv< 2:
elif:
    Face = Deck > 9:
else: 
    Number
    
plt.hist(Ace,Face,Number)    

# Basic function of this project completed

"""Calculate the value of shown cards"""
value_hand1 = hand1(2)
value_hand2 = hand2(1) + hand2(2)

"""Print hand value"""
print(value_hand1)
print(value_hand2)

"""Create a probability function to determine the next card given the three 'up' cards"""
# p_next=48!/52!

"""Start three groups of probabilities (1/11 Ace Group), (2-9 Numbers Group), (10-K Face Group)"""
if
    Ace=Deck<2:
elif
    Face=Deck>9:
    else=Number
  