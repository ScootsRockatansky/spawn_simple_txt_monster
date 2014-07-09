
from random import random, randint
#1out of 5 chance for critical hit
#start with class weapons
#child class sword, less damage, more chance of crit
#child class mace, more damage, less crit
#crit=base*2
strength=75

class sword:
    def swordhit(self):
        attacks = randint(strength/2, strength*2)
        chance= randint(1,6)
        if chance== 3:
            attacks= randint(strength, strength*3)
            print 'CRITICAL HIT!'
        return attacks
        
class mace:
    def macehit(self):
        attackm= randint(strength/2, strength*2)
        chance= randint(1,15)
        if chance==3:
            attackm= randint(strength, strength*4)
            print "CRITICAL HIT!"
        return attackm
        
monster_hp=200
sw = sword()
mc=mace()
cmd= raw_input()
if cmd=="attack":
    monster_hp = monster_hp - sw.swordhit()
    print monster_hp
else:
    print "no"
