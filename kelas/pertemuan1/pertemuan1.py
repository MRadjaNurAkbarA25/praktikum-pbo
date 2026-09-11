

class Hero:
    jumlahHero = 0
    def __init__(self, name, hp, armor, attack):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.attack = attack
        print('nama saya')
    def hpUp(self, up):
        self.hp += up

roger = Hero('Roger', 100, 4, 15)
print(roger.__dict__)
roger.hpUp(25)
print(roger.__dict__)
print(roger.name)
sniper = Hero('Sniper', 50, 5, 30)