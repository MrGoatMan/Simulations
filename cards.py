import sys 

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

def selectSort(deck):
    for i in range(len(deck)): 
      
        min_idx = i 
        for j in range(i+1, len(deck)): 
            if deck[min_idx] > deck[j]: 
                min_idx = j

        if deck[i] > deck[min_idx]:
            deck[i], deck[min_idx] = deck[min_idx], deck[i] 
  

    print ("Sorted array") 
    for i in range(len(deck)): 
        print(deck[i])


selectSort(deck)

print(deck)
  

