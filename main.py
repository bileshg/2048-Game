import itertools
import random
import os

from terminaltables import SingleTable


class GameBoard:

    def __init__(self, size=4):
        self.grid_size = size
        self.grid = [[0 for _ in range(self.grid_size)]
                     for _ in range(self.grid_size)]
        for i, j in itertools.product(range(self.grid_size),
                                      range(self.grid_size)):
            self.grid[i][j] = 0
        self.add_random_cell()
        self.add_random_cell()

    def add_random_cell(self):
        i = random.randint(0, self.grid_size - 1)
        j = random.randint(0, self.grid_size - 1)
        while self.grid[i][j] != 0:
            i = random.randint(0, self.grid_size - 1)
            j = random.randint(0, self.grid_size - 1)
        self.grid[i][j] = 2

    def print_grid(self):
        table = SingleTable(self.grid)
        table.inner_row_border = True
        print("\n" + table.table)

    def move(self, direction):
        if direction == "S":
            self.move_down()
        elif direction == "W":
            self.move_up()
        elif direction == "D":
            self.move_right()
        elif direction == "A":
            self.move_left()
        else:
            print("Invalid Move!!! Try again...")

    def move_left(self):
        for i in range(self.grid_size):
            self.grid[i] = [j for j in self.grid[i] if j != 0]
            for j in range(len(self.grid[i]) - 1):
                if self.grid[i][j] == self.grid[i][j + 1]:
                    self.grid[i][j] *= 2
                    self.grid[i][j + 1] = 0
            self.grid[i] = [j for j in self.grid[i] if j != 0]
            self.grid[i] += [
                0 for _ in range(self.grid_size - len(self.grid[i]))
            ]

    def move_right(self):
        for i in range(self.grid_size):
            self.grid[i] = [j for j in self.grid[i] if j != 0]
            for j in range(len(self.grid[i]) - 1, 0, -1):
                if self.grid[i][j] == self.grid[i][j - 1]:
                    self.grid[i][j] *= 2
                    self.grid[i][j - 1] = 0
            self.grid[i] = [j for j in self.grid[i] if j != 0]
            self.grid[i] = [
                0 for _ in range(self.grid_size - len(self.grid[i]))
            ] + self.grid[i]

    def move_up(self):
        self.grid = list(map(list, zip(*self.grid)))
        self.move_left()
        self.grid = list(map(list, zip(*self.grid)))

    def move_down(self):
        self.grid = list(map(list, zip(*self.grid)))
        self.move_right()
        self.grid = list(map(list, zip(*self.grid)))

    def game_over(self):
        for i, j in itertools.product(range(self.grid_size),
                                      range(self.grid_size - 1)):
            if self.grid[i][j] in [0, self.grid[i][j + 1]]:
                return False
        return all(
            self.grid[i][j] != self.grid[i + 1][j]
            for i, j in itertools.product(range(self.grid_size -
                                                1), range(self.grid_size)))


if __name__ == '__main__':
    print('-' * 40)
    print("""
    ██████   ██████  ██   ██  █████  
         ██ ██  ████ ██   ██ ██   ██ 
     █████  ██ ██ ██ ███████  █████  
    ██      ████  ██      ██ ██   ██ 
    ███████  ██████       ██  █████  
    """)
    print('[CONTROLS]'.center(40, '-'))
    print("""
    W - Up
    S - Down
    D - Right
    A - Left
    X - Quit
    """)
    print('[PRESS ENTER TO START]'.center(40, '-'))

    # ToDo: Logic to choose grid size
    SIZE = 4
    BLENGTH = (SIZE * 4) + 1

    _ = input()
    os.system('cls' if os.name == 'nt' else 'clear')

    gb = GameBoard(SIZE)
    while not gb.game_over():
        gb.print_grid()
        direction = input("\n" + "Your move:".rjust(BLENGTH)).upper()

        if direction == "X":
            print("\n" + " Bye Bye!!! ".center(BLENGTH, "=") + "\n")
            break

        gb.move(direction)
        gb.add_random_cell()
        os.system('cls' if os.name == 'nt' else 'clear')
