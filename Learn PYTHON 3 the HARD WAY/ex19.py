def cheeseAndCrackers(cheeseCount, boxsOfCrackers):
    print(f"You have {cheeseCount} cheeses!")
    print(f"You have {boxsOfCrackers} boxs of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the funtion munbers directly:")
cheeseAndCrackers(20, 30)

print("OR, we can use variables from our script:")
amountOfCheese = 10
amountOfCrackers = 50

cheeseAndCrackers(amountOfCheese, amountOfCrackers)

print("We can even do math inside too:")
cheeseAndCrackers(10 + 20, 5 + 6)


print("And wo can combine the two, variables and math:")
cheeseAndCrackers(amountOfCheese + 100, amountOfCrackers + 1000)
