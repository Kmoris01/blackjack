# List of a deck of cards by suite and number
# import random
import random
 
# import shuffle from random
from random import shuffle

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
           

"""Deal the hand first 'down' card"""
hand1(1)=np.random.randint(Deck)
hand2(1)=np.random.randint(Deck)

"""Deal the hand second 'up' card"""
hand1(2)=np.random.randint(Deck)
hand2(2)=np.random.randint(Deck)

"""Show dealer 'up' card and player's cards"""
Print("Dealer has x &", hand1(2))
Print("Player has ", hand2(1),hand2(2))

# Basic function of this project completed

"""Calculate the value of shown cards"""
value_hand1 = hand1(2)
value_hand2 = hand2(1) + hand2(2)

"""Print hand value"""
print(value_hand1)
print(value_hand2)




  