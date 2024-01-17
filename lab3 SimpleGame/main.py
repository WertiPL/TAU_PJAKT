#Wiktor Rostkowski s23141
import random


class SimpleGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
        self.start = (random.randint(0, width - 1), random.randint(0, height - 1))
        self.stop = self.generate_stop()
        self.obstacles = self.generate_obstacles()
        self.generate_path()

        self.display_board()

    def generate_stop(self):
        stop = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
        while stop == self.start:
            stop = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
        return stop

    def generate_obstacles(self):
        num_obstacles = random.randint(1, min(self.width, self.height) - 1)
        obstacles = set()

        while len(obstacles) < num_obstacles:
            obstacle = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if obstacle != self.start and obstacle != self.stop:
                obstacles.add(obstacle)

        return obstacles

    def generate_path(self):
        x, y = self.start

    def display_board(self):
        for row in self.board:
            print('-'.join(row))

    def move(self, direction):
        x, y = self.start
        if direction == 'left' and x > 0 and (x - 1, y) not in self.obstacles:
            self.start = (x - 1, y)
        elif direction == 'right' and x < self.width - 1 and (x + 1, y) not in self.obstacles:
            self.start = (x + 1, y)
        elif direction == 'up' and y > 0 and (x, y - 1) not in self.obstacles:
            self.start = (x, y - 1)
        elif direction == 'down' and y < self.height - 1 and (x, y + 1) not in self.obstacles:
            self.start = (x, y + 1)


game = SimpleGame(5, 5)

# Test ruchu
game.move('right')
game.display_board()

# Zapis planszy do pliku
with open('board.txt', 'w') as file:
    for row in game.board:
        file.write(' '.join(row) + '\n')
