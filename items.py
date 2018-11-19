from random import randint

class weapon():

    def get_info(self):
        print('\n'+self.wep_type)
        print(str(self.dmg) +' ' + self.dmg_type + ' damage')
        # print(str(self.handed) + ' Handed')

    def is_two_handed(self):
        if self.handed == 2:
            return True
        else:
            return False

class sword(weapon):

    def __init__(self,dmg):
        self.type = 'Weapon'
        self.wep_type = 'Sword'
        self.dmg_type = 'Slashing'
        self.dmg = dmg
        self.handed = 2

class dagger(weapon):

    def __init__(self,dmg):
        self.type = 'Weapon'
        self.wep_type = 'Dagger'
        self.dmg_type = 'Piercing'
        self.dmg = dmg
        self.handed = 1

class staff(weapon):

    def __init__(self,dmg):
        self.type = 'Weapon'
        self.wep_type = 'Staff'
        self.dmg_type = 'Crushing'
        self.dmg = dmg
        self.handed = 2

class wand(weapon):

    def __init__(self,dmg):
        self.type = 'Weapon'
        self.wep_type = 'Wand'
        self.dmg_type = 'Magic'
        self.dmg = dmg
        self.handed = 1

class bow(weapon):

    def __init__(self,dmg):
        self.type = 'Weapon'
        self.wep_type = 'Bow'
        self.dmg_type = 'Piercing'
        self.dmg = dmg
        self.handed = 2



class armor():

    def __init__(self,armor_class,armor_slot,armor_rtg):
        self.type = 'Armor'
        self.armor_class = armor_class
        self.armor_slot = armor_slot
        self.armor_rtg = armor_rtg

    def get_info(self):
        print('\n'+self.armor_class + ' ' + self.armor_slot)
        print(str(self.armor_rtg) + ' Armor')
