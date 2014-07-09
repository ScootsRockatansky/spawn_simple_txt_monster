#MONSTERS

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


#PLAYER

class Player:
    hlth = 1000
    atk = randint(0,100)
    name = raw_input("What is your name?")
    stgth = 2000
    mana = 2000


#
