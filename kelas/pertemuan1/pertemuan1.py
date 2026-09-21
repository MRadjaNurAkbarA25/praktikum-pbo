class Hero:
    jumlahHero = 0
    def __init__(self, name, hp, armor, attack):
        self.__name = name
        self._hp = hp
        self.armor = armor
        self.attack = attack
    
    @property
    def getName(self):
        return self.__name
    
    
    
sniper = Hero('sniper', 100, 4, 15)

print(sniper.armor)
print(sniper.__dict__)
print(sniper.getName)
# print(sniper.hp)