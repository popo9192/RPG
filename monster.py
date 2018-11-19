from random import randint


class mob():
    level = 1
    is_player = False
    experience = 10

    def get_info(self):
        print(self.name)
        print('Level '+ str(self.level), self.mob_type)
        print('Health: ' + str(self.health))
        print('Armor: ' + str(self.armor))
        print('Strength: ' + str(self.strength))
        print('Dexterity: ' + str(self.dexterity))
        print('Int: ' + str(self.intelligence))

    def attack(self):
        is_crit = False
        att = max(self.strength,self.dexterity,self.intelligence)
        return(att,is_crit)

    def take_dmg(self,damage):
        dodge = randint(0,10)
        dodge = dodge *(1 +(self.dexterity/10))
        dodged = False
        if dodge >=9:
            damage = 0
            dodged = True
        damage = damage - self.armor
        self.health -= damage
        return damage, dodged, self.health

class bear_mob(mob):

    def __init__(self):
        self.name = 'Bear'
        self.mob_type = 'Beast'
        self.health = 12
        self.armor = 0
        self.strength = 5
        self.dexterity = 2
        self.intelligence = 1

    def power_att(self):
        return (round(self.strength * 1.5))

class wolf_mob(mob):

    def __init__(self):
        self.name = 'Wolf'
        self.mob_type = 'Beast'
        self.health = 10
        self.armor = 0
        self.strength = 4
        self.dexterity = 4
        self.intelligence = 1

    def power_att(self):
        return (self.strength + self.dexterity)

class tiger_mob(mob):

    def __init__(self):
        self.name = 'Tiger'
        self.mob_type = 'Beast'
        self.health = 8
        self.armor = 0
        self.strength = 2
        self.dexterity = 5
        self.intelligence = 1

    def power_att(self):
        return (self.dexterity * 2)

def spawn_mob(list):
    index = randint(0,len(list)-1)
    mob = list[index]
    if mob == 'Bear':
        mob1 = bear_mob()
    elif mob == 'Wolf':
        mob1 = wolf_mob()
    elif mob == 'Tiger':
        mob1 = tiger_mob()
    return mob1


# mob1 = spawn_mob(beasts)

# # mob1 = tiger_mob()
# mob1.get_info()
# mob1.attack()
# mob1.power_att()
