import random

EASY = 20
MEDIUM = 35
HARD = 50
class SudokuEngine:
    def __init__(self):
        self.tabuleiro = [
            ['--', '--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--', '--'],
        ]
        self.size = 9

    def definir_tabuleiro(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(numbers)
        self.tabuleiro[0] = numbers

        for line in range(1, self.size):
            attempt_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for col in range(self.size):
                placed = False
                pseudo_numbers = attempt_numbers.copy()
                while not placed and pseudo_numbers:
                    num = random.choice(pseudo_numbers)
                    pseudo_numbers.remove(num)
                    if all(self.tabuleiro[row][col] != num for row in range(self.size)):
                        self.tabuleiro[line][col] = num
                        placed = True
                        attempt_numbers.remove(num)
                if not placed:
                    for c in range(self.size):
                        self.tabuleiro[line][c] = '--'
                    return self.definir_tabuleiro() #Refazer tudo se não houver solução.

    def print(self):
        for x in range(0, self.size):
            print(self.tabuleiro[x])