class Enemy:
    life = 0

    def __init__(self, life):
        self.life = life

    def attack(self):
        if self.life > 0:
            print('Attack!!!')
            self.life -= 1
        else:
            print('Game over!')

    def checkLife(self):
        if self.life <= 0:
            print('Game over!')
        else:
            print('Life:', self.life)