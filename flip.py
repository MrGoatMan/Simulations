import random

numFlips = int(input("How many flips to simulate?"))
runSearch = int(input("What is the side you're looking for?"))


flips = [0] * 6

numHead = 0
numTail = 0
twoHead = 0
oneHead = 0
oneTail = 0
twoTail = 0
i = 0

while (i < numFlips):
    flip = random.randint(0,1)
    flips[flip-1] += 1
    if flip == 0:
        oneHead += 1
        numHead += 1
    if flip == 1:
        oneHead = 0
    if oneHead == 2:
        twoHead +=1
    if flip == 1:
        oneTail += 1
        numTail += 1
    if flip == 0:
        oneTail = 0
    if oneTail == 2:
        twoTail +=1
    i += 1

if runSearch  == 0:
    print("Heads: " + f"{numHead}/{numFlips} = {numHead/numFlips*100}")

if runSearch == 1:
    print("Tails: " + f"{numTail}/{numFlips} = {numTail/numFlips*100}")

runLength = int(input("How long is the run you're looking for?"))
if runSearch == 0:
        print("Heads repeats twice in a row " + f"{numHead}" + " times!")
if runSearch == 1:
        print("Tails repeats twice in a row " + f"{numTail}" + " times!")
