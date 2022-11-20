from random import shuffle  #import the shuffle function from library "random"
from array import *

def add_to_hand(hand_var, sum_var, ace_var, turned_ace):
    
    temp = (total_deck[0]//4) + 1
    
    if(temp > 10):  #because J, Q, K all equal 10
        temp = 10

    hand_var.append(temp)
    
    if(temp == 1):
        ace_var = ace_var + 1

    sum_var = sum_var + temp #add the new card to the sum
    #print("Sum_var: ", sum_var)
    if(sum_var < 21): #if you have an ace, check if it burns you, if it is 11 instead of 1. If not, add 10 to the sum
        if(ace_var > 0 and sum_var + 10 < 21):
            sum_var = sum_var + 10
            turned_ace = True

    if(sum_var > 21):
        if(turned_ace == True):
            sum_var = sum_var - 10
            turned_ace = False
    
    total_deck.pop(0)
    return sum_var

def check_victory(dealer_sum, player_sum, dealer_victory, player_victory):
    if(player_sum == 21):
        print("You win the bet!")
        player_victory = True
    elif(dealer_sum == 21):
        print("You lose the bet...")
        dealer_victory = True

i = 0

deck = []

while(i < 52):
    deck.append(i)  #add "i" at the end of the list, create a base deck
    i = i + 1       #if we take an element of the array div4 + 1, that gives us the value of the card

N = 0

while(N <= 0):       #keep reading the number of decks until a number > 0 is given
    N = int(input("Please give the number of decks that you want to use: "))

i = 0
#j = 0
total_deck = []
while(i < N):    #add the number N of decks to the total_deck variable
    j = 0
    while(j < 52):
        total_deck.append(deck[j])
        j = j + 1
    i = i + 1

shuffle(total_deck) #here we shuffle the deck

#print debug statements
#i = 0
#while(i < len(total_deck)):
#    print(total_deck[i])
#    i = i + 1
#print debug statements

cont = "y"
money = 100

while(cont == "y"):
    if(money == 0): #if money has reached 0, exit and print that you are a brokie
        print("YOU 'RE A BROKIE!")
        break
    if(len(total_deck) <= ((N * 52) * 25/100)): #break if the amount of remaining cards is < 25% of total
        print("You are running low on cards, exiting...")
        break
        
    print("Player Money: ", money, " - Cards Left: ", len(total_deck))
    bet = -1
    while(bet <= 0): #validate that bet > 0
        print("Select your bet in [1 ", money, "]: ")
        bet = int(input())
        
    hit = "y"
    dealer = []
    dealer_sum = 0
    player = []
    player_sum = 0
    counter = 0
    ace_counter_dealer = 0 #if you draw an ace, + 1
    ace_counter_player = 0
    turned_ace_dealer = False
    turned_ace_player = False
    dealer_victory = False
    player_victory = False
    
    while(hit == "y"):
        #print(counter)
        if(counter == 0):
            #dealer draws 2 cards
            dealer_sum = add_to_hand(dealer, dealer_sum, ace_counter_dealer, turned_ace_dealer)
            dealer_sum = add_to_hand(dealer, dealer_sum, ace_counter_dealer, turned_ace_dealer)
            #print("dealer_sum: ", dealer_sum)
            #dealer draws 2 cards

            print("Dealer Cards: ", dealer[0], " ??")
            
            #player draws 2 cards
            player_sum = add_to_hand(player, player_sum, ace_counter_player, turned_ace_player)
            player_sum = add_to_hand(player, player_sum, ace_counter_player, turned_ace_player)
            print("player_sum: ", player_sum)
            #player draws 2 cards

            print("Player Cards: ", player)

            counter = counter + 1

            check_victory(dealer_sum, player_sum, dealer_victory, player_victory)
            
        elif(counter > 0):  #if you choose to hit
            player_sum = add_to_hand(player, player_sum, ace_counter_player, turned_ace_player)
            print("player_sum: ", player_sum)
            print("Player Cards: ", player)

        if(player_sum > 21 or dealer_sum > 21):
            break
        elif(player_victory == True or dealer_victory == True):
            break
            
        hit = str(input("Do you want to hit? [y = yes/n = no] "))
        #print(hit)
        while(hit != "y" and hit != "n"):    #validate input for hit variable
            hit = str(input("Do you want to hit? [y = yes/n = no] "))

    
    print("Dealer Cards: ", dealer)
    print("dealer_sum: ", dealer_sum)
    
    if(player_victory == True): #if player has 21
        money = money + bet
    elif(dealer_victory == True): #if dealer has 21
        money = money - bet
    else:
        if(player_sum > 21):
            print("You lose the bet...")
            money = money - bet
        else:
            while(dealer_sum < 17):  #while the dealer has a sum of less than 17
                dealer_sum = add_to_hand(dealer, dealer_sum, ace_counter_dealer, turned_ace_dealer)
                print("Dealer Cards: ", dealer)
                print("dealer_sum: ", dealer_sum)
                #print(dealer_sum)
            if(dealer_sum > 21):    #if dealer busts and player does not
                if(player_sum < 22):
                    print("You win the bet!")
                    money = money + bet
                else:               #both got burned
                    print("Nobody wins - Tie.")
            elif(dealer_sum > player_sum):  #if the dealer has a bigger sum, you lose
                print("You lose the bet...")
                money = money - bet
            elif(player_sum > dealer_sum):  #if the player has a bigger sum, they win
                print("You win the bet!")
                money = money + bet
    print()
    cont = str(input("Do you want to continue? [y = yes/n = no] "))
    print()
    while(cont != "y" and cont != "n"):   #validate input for stop variable
        cont = str(input("Do you want to continue? [y = yes/n = no] "))
        print()






















