import random


class Game:
    def __init__(self):
        self.NewGame()

    def Check(self, num: int):
        self.attemptsCount += 1
        if num < self.number:
            return 'Больше'
        elif num > self.number:
            return 'Меньше'
        else:
            self.over = True
            return f'УГАДАЛ!\nЧисло попыток: {self.attemptsCount}'
        
    def NewGame(self, userId: int):
        self.userId = userId
        self.number = random.randint(1, 1001)
        self.attemptsCount = 0
        self.over = False