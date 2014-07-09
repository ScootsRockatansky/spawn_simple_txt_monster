from random import random, randint

import random

class Monster:
    hlth = 100
    atk = 100
class Zombie(Monster):
    atk = randint(0,150)
    hlth = randint(1,200)
    name = 'zombie'
class Skeleton(Monster):
    atk = randint(0,100)
    hlth = randint(1,100)
    name = 'skeleton'
class Hellhound(Monster):
    atk = randint(0,100)
    hlth = randint(1,200)
    name = 'hellhound'
class Vampire(Monster):
    atk = randint(0,200)
    hlth = randint(1,200)
    name = 'vampire'
class Sprite(Monster):
    atk = randint(0,50)
    hlth = randint(1,100)
    name = 'sprite'

cmd = raw_input("Do you want to play? Yes or no?")

while cmd != "no" and "No" and "NO":

    monsters=[Zombie, Skeleton, Hellhound, Vampire, Sprite]
    randmonster = random.choice(monsters)
    instr = raw_input("You come across a %s! It has %s health! What will you do?" % (randmonster.name, randmonster.hlth))

    if instr == 'attack':
        randmonster.hlth = randmonster.hlth - 200

        if randmonster.hlth <= 0:
            print("Monster destroyed!")

    elif instr == 'quit':
                break










    
