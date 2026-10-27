# asosiasi
class Shop:
    def __init__(self, name):
        self.name = name
        
    def proses_pembelian(self, hero, item):
        if hero.gold >= item.harga:
            hero.gold -= item.harga
            print(f'{hero.name} beli {item.name} {item.harga} gold di {self.name}, sisa gold {hero.gold}')
            return True
        print(f'Gold {hero.name} tidak cukup untuk beli {item.name}')
        return False
    
class Item:     
    def __init__(self, name, harga, bonus_attack=0, bonus_armor=0):
        self.name = name
        self.harga = harga
        self.bonus_attack = bonus_attack
        self.bonus_armor = bonus_armor
        
    def __str__(self):
        return(f'Item: {self.name} | +{self.bonus_attack} attack | +{self.bonus_armor} armor')
        
class Hero:
    jml_hero = 0
    MAKS_SLOT = 4
    
    def __init__(self, name, hp, mana, armor, attack, gold, list_skill):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.armor = armor
        self.attack = attack
        self.gold = gold
        
        self._inventory = [] # agregasi
        self._skills = [Skill(nama, dmg, cost) for nama, dmg, cost in list_skill] # komposisi
        Hero.jml_hero += 1
        
    
    # penggunaan asosiasi
    def beli_item(self, shop, item):
        if len(self._inventory) >= Hero.MAKS_SLOT:
            print(f'Inventory {self.name} sudah penuh')
            return
        if item in self._inventory:
            print(f'{self.name} sudah punya {item.name}')
            return
        if shop.proses_pembelian(self, item):
            self._pasang_item(item)
            
    def cast_skill(self, nomor_skill, lawan):
        if not 1 <= nomor_skill <= len(self._skills):
            print(f'Skill nomor {nomor_skill} tidak ada')
            return
        skill = self._skills[nomor_skill - 1]
        if self.mana < skill.mana_cost:
            print(f'Mana {self.mana} tidak cukup untuk {skill.name}')
            return
        self.mana -= skill.mana_cost
        lawan.hp = max(0, lawan.hp - skill.damage)
        print(f'{self.name} memakai {skill.name} ke {lawan.name}, sisa hp {lawan.name} = {lawan.hp}')        
    
    # agregasi
    def ambil_item(self, item):
        if len(self._inventory) >= Hero.MAKS_SLOT:
            print(f'Inventory {self.name} sudah penuh')
            return
        if item in self._inventory:
            print(f'{self.name} sudah punya {item.name}')
            return
        self._pasang_item(item)
        print(f'+ {self.name} mengambil {item.name}')

    # bonus item langsung menambah status hero
    def _pasang_item(self, item):
        self._inventory.append(item)
        self.attack += item.bonus_attack
        self.armor += item.bonus_armor
            
    
            
class Skill:
    def __init__(self, name, damage, mana_cost):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
    
    def __str__ (self):
        return(f'{self.name} {self.damage} damage, {self.mana_cost} mana')

brody = Hero('Brody', 3000, 1000, 10, 100, 4000, list_skill=[('tembak',100,10), ('loncat', 10, 1)])
estes = Hero('Estes', 3000, 1000, 10, 100, 4000, list_skill=[('tembak',100,10), ('loncat', 10, 1)])
shop = Shop('Belanja item')
bod = Item('Blade of Despair', 3100, bonus_attack=160)
winter = Item('Winter Truncehon', 2140, bonus_attack=15, bonus_armor=45)

brody.beli_item(shop, bod)
brody.ambil_item(winter)
brody.cast_skill(1, estes)

print()

