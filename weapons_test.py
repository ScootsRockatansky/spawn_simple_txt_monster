from random import random, randint

monster_hp = 1000

import random

class Weapon:
    dmg = 150
    crithit = randint(0,4)
    if crithit == 2:
        dmg = dmg * 2
    else:
         = dmg

cmd = raw_input("Type attack!")

if cmd == 'attack':
    monster_hp = monster_hp - 
    

    print(monster_hp)

