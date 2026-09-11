class Hero:
    jumlahHero = 0
    def __init__(self, name, hp, armor, attack):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.attack = attack
        Hero.jumlahHero += 1
    
    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.attack)
    def diserang(self, lawan, attack_lawan):
        print(f'{self.name} diserang {lawan.name}')
        
sniper = Hero('Sniper', 100, 50, 80)
roger = Hero('Roger', 150, 70, 60)

sniper.serang(roger)