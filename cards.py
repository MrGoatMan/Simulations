deck = []
suits = ["♠", "♥", "♦", "♣"]

for i in range(4):
    for j in range(1, 14):
        value = str(j)
        if(j == 1):
            value = "A"
        elif(j == 11):
            value = "J"
        elif(j == 12):
            value = "Q"
        elif(j == 13):
            value = "K"
        deck.append(f"{value}{suits[i]}")

print(deck)

#commit to github under siumulation

# shuffle the deck

# print the shuffled deck
#commit a second time to github
# turn in two histories

import random 
  
def randomize (deck, n): 
    # Start from the last element and swap one by one. We don't 
    # need to run for the first element that's why i > 0 
    for i in range(n-1,0,-1): 
        # Pick a random index from 0 to i 
        j = random.randint(0,i+1) 
  
        # Swap arr[i] with the element at random index 
        deck[i],deck[j] = deck[j],deck[i] 
    return deck

# Driver program to test above function. 

n = len(deck)

print(randomize(deck, n)) 
  

