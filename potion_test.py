from random import random, randint

potion = 0

cmd = raw_input("please enter a chance to get a potion")

if cmd == "potion":

   potion_drop = randint(0,7)

   if potion_drop == 4:
       potion += 1

print(potion)