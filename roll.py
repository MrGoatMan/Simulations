import random

rollnum = int(input("Hey bro, please enter a number!"))
print(rollnum)
print("Beginning Rolls!:")
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0

#1/6 of 100 is 16.6 repeating.
#By multiplying the 1 by 1.20, you get a 20/100 chance of rolling a 1
#The remaining 80, divided by 5, is a 16/100 chance each.
i = 0
while i < rollnum:
    thisroll = random.randint(1, 100)
    if thisroll <= 20:
        ones += 1
        print("1")
    if thisroll > 20 and thisroll <= 36:
        twos += 2
        print("2")
    if thisroll > 36 and thisroll <= 52:
        threes += 2
        print("3")
    if thisroll > 52 and thisroll <= 68:
        fours += 2
        print("4")
    if thisroll > 68 and thisroll <= 84:
        fives += 2
        print("5")
    if thisroll > 84 and thisroll <= 100:
        sixes += 2
        print("6")
    i += 1

print("Next")
    
        
    
