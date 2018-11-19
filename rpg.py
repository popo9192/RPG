from random import randint
from items import armor, sword, bow, staff, dagger, wand
from monster import spawn_mob

classes = ['Warrior','Rogue','Mage','Priest']
races = ['Human','Orc','Elf']
combat_opt = ['Attack','Skills',"Backpack","Run"]
beasts = ['Tiger','Bear','Wolf']

class hero:
    level = 1
    experience = 0
    is_player = True
    equip_slots ={
    'Helm' : [],
    'Chest' : [],
    'Gloves' : [],
    'Boots' : [],
    'Weapons' : []}
    skills = []
    backpack = []

    def get_info(self):
        print(self.name)
        print('Level: '+ str(self.level),self.race,self.ch_class)
        print('Health: ' + str(self.health))
        print('Armor: ' + str(self.armor))
        print('Strength: ' + str(self.strength))
        print('Dexterity: ' + str(self.dexterity))
        print('Int: ' + str(self.intelligence))

    def attack(self):
        is_crit = False
        att = max(self.strength,self.dexterity)
        if self.equip_slots['Weapons']:
            for i in self.equip_slots['Weapons']:
                print(i.wep_type)
                att += i.dmg
        crit = randint(0,10)
        crit = crit *(1 +(self.dexterity/10))
        if crit >=8:
            att = att * 2
            is_crit = True
        return(att, is_crit)

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

    def add_equipment(self,item):
        if item.type == 'Armor':
            # print(item.armor_slot)
            slot = item.armor_slot
            if not self.equip_slots[slot]:
                self.equip_slots[slot].append(item)
            else:
                old_item = self.equip_slots[slot].pop()
                self.equip_slots[slot].append(item)

        if item.type == 'Weapon':
            # print(item.wep_type)
            slot = 'Weapons'
            if not self.equip_slots[slot]:
                self.equip_slots[slot].append(item)
            else:
                old_item = self.equip_slots[slot].pop()
                self.equip_slots[slot].append(item)

    def get_equipment(self):
        for slots in self.equip_slots:
            for item in self.equip_slots[slots]:
                item.get_info()

class warrior(hero):

    def __init__(self,name,race):
        self.name = name
        self.ch_class = 'Warrior'
        self.race = race
        self.armor_class = 'Plate'
        self.health = 12
        self.armor = 0
        self.strength = 5
        self.dexterity = 2
        self.intelligence = 1

class rogue(hero):

    def __init__(self,name,race):
        self.name = name
        self.ch_class = 'Rogue'
        self.race = race
        self.armor_class = 'Leather'
        self.health = 10
        self.armor = 0
        self.strength = 1
        self.dexterity = 5
        self.intelligence = 2

class mage(hero):

    def __init__(self,name,race):
        self.name = name
        self.ch_class = 'Mage'
        self.race = race
        self.armor_class = 'Cloth'
        self.health = 8
        self.armor = 0
        self.strength = 1
        self.dexterity = 1
        self.intelligence = 7

class priest(hero):

    def __init__(self,name,race):
        self.name = name
        self.ch_class = 'Priest'
        self.armor_class = 'Cloth'
        self.race = race
        self.health = 8
        self.armor = 0
        self.strength = 1
        self.dexterity = 1
        self.intelligence = 7

def create_new_char():
    print("\nWhat is your name?")
    char_name = input()
    char_class = enter_class()
    char_race = enter_race()
    char = build_char(char_name,char_class,char_race)
    return char


def enter_class():
    valid_class = False
    while not valid_class:
        print("\nSelect your class: "+ (', '.join(classes)))
        char_class = input()
        if char_class in classes:
            valid_class = True
            return(char_class)


def enter_race():
    valid_race = False
    while not valid_race:
        print("\nSelect your class: "+ (', '.join(races)))
        char_race = input()
        if char_race in races:
            valid_race = True
            return(char_race)


def build_char(char_name,char_class,char_race):
    char_class = char_class.lower()
    if char_class == 'warrior':
        char1 = warrior(char_name,char_race)
    elif char_class == 'rogue':
        char1 = rogue(char_name,char_race)
    elif char_class == 'mage':
        char1 = mage(char_name,char_race)
    elif char_class == 'priest':
        char1 = priest(char_name,char_race)
    return char1
    # char1.get_info()
    # char1.get_stats()

# create_new_char()

def generate_armor():
    armor_classes = ['Cloth','Leather','Plate']
    armor_slots = ['Helm','Chest','Boots','Gloves']
    class_index = randint(0,len(armor_classes)-1)
    slot_index = randint(0,len(armor_slots)-1)
    rtg = randint(1,3)
    a = armor(armor_classes[class_index],armor_slots[slot_index],rtg)
    return a


def generate_weapon():
    wep_types = ['Sword','Dagger','Staff','Wand','Bow']
    wep_index = randint(0,len(wep_types)-1)
    wep_type = wep_types[wep_index]
    dmg = randint(1,3)
    if wep_type == 'Sword':
        w = sword(dmg)
    elif wep_type == 'Dagger':
        w = dagger(dmg)
    elif wep_type == 'Staff':
        w = staff(dmg)
    elif wep_type == 'Wand':
        w = wand(dmg)
    elif wep_type == 'Bow':
        w = bow(dmg)
    return w


def new_game():
    print("""
    Greetings Adventurer, Welcome to Dungeon Quest!

    It is up to you to cleanse the beasts and other evils that stalk the neighboring lands.

    Are you ready to get started? (Yes/No)
    """)
    start = input('')
    if start.lower() == 'yes':
        char = create_new_char()
        print('')
        char.get_info()
    else:
        new_game()

    print('\nHere is a gift to help you get started!')
    a = generate_armor()
    char.add_equipment(a)
    w = generate_weapon()
    char.add_equipment(w)
    char.get_equipment()
    pause = input('')

    print("\nLet's start your adventure! Start heading into the Strangethorn Forest.")

    print("\nAs you walk under the towering pines, you hear growls coming out of the shadows... ")
    pause = input('')
    mob1 = spawn_mob(beasts)
    chars = [char,mob1]
    combat(chars)

    char.get_info()
    pause = input('')
    print('\nBloodied, but still standing, you head deeper into the forest. However, you are starting to realize this trek might be harder than expected...')
    pause = input('')
    mob2 = spawn_mob(beasts)
    chars = [char,mob2]
    combat(chars)

def combat(chars):
    enemy_dead = False
    char1 = chars[0]
    char2 = chars[1]
    move_order = sorted(chars, key=lambda x:x.dexterity, reverse=True)
    print("Turn Order:")
    for char in move_order:
        print (char.name, "Dex: " +str(char.dexterity))

    pause = input('')
    while not enemy_dead:
        for char in move_order:
            if char == char1:
                enemy = char2
            else:
                enemy = char1

            if char.is_player:
                print("\n"+char.name + " is up!")
                combat_update(chars)
                enemy_dead = player_combat_options(char,enemy)
                # if enemy_dead:
                #     break
            else:
                print("\nIt's the " +char.name+ "'s turn:")
                combat_update(chars)
                pause = input('')
                enemy_dead = combat_attack(char,enemy)
            if enemy_dead:
                break
                # pause = input('')

def combat_update(chars):
    health_stats = []
    for char in chars:
        health_stats.append(char.name + ": "+str(char.health) + ' Health')
    print(health_stats)

def player_combat_options(char,enemy):
    print("\nWhat do you want to do? "+ (', '.join(combat_opt)))
    combat_move = input('')
    if combat_move.lower() == 'attack':
        enemy_dead = combat_attack(char,enemy)
        return(enemy_dead)
    elif combat_move.lower() == 'skills':
        if char.skills:
            print('\nWhat skill do you want to use?'+ (', '.join(char.backpack)))
        else:
            print("You haven't leaned any skills yet!")
            player_combat_options(char,enemy)
    elif combat_move.lower() == 'backpack':
        if char.backpack:
            print('\nWhat item do you want to use?'+ (', '.join(char.backpack)))
        else:
            print("No items available in your backpack!")
            player_combat_options(char,enemy)
    elif combat_move.lower() == 'run':
        print('\nYou run away from combat!')
    else:
        print('\nPlease select a valid option')
        player_combat_options(char,enemy)

def combat_attack(char,enemy):
    enemy_dead = False
    attack, is_crit = char.attack()
    damage, dodged, health = enemy.take_dmg(attack)
    if dodged:
        if enemy.is_player:
            print('\nYou dodged the attack!')
        else:
            print('\nThe '+enemy.name + ' dodged the attack!')
    else:
        if is_crit:
            print('Critical Strike!')
        print('\n' + char.name + " strikes the " + enemy.name +" for " + str(damage) + ' damage!')
        pause = input('')
    if enemy.health <= 0:
        if enemy.is_player:
            print("\nYou have been killed by the "+ enemy.name +". Better luck next time!")
            pause = input(' ')
            new_game()
        else:
            print("\nYou have slain the " + enemy.name + ". You gain "+ str(enemy.experience)+' experience!')
            char.experience += enemy.experience
            enemy_dead = True
    return(enemy_dead)


# a = generate_armor()
# # a.get_info()
#
# char_name = 'Rex'
# char_race = 'Orc'
#
# char_name2 = 'Pete'
# char_race2 = 'Human'
#
# char1 = warrior(char_name,char_race)
#
# # char1.get_info()
# print('')
# w1 = generate_weapon()
# char1.add_equipment(a)
# char1.add_equipment(w1)
# char1.get_equipment()
# print('')
# char1.attack()
# # char1.equip_slots['Helm'][0].get_info()
# mob1 = spawn_mob(beasts)
# chars = [char1,mob1]
# combat(chars)
new_game()
