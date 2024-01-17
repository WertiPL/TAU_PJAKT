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
        self.path = []
        self.generate_path()

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

        for obstacle in self.obstacles:
            self.board[obstacle[1]][obstacle[0]] = 'X'

        self.board[y][x] = '*'
        self.path.append((x, y))


    def display_board(self):
        for row in self.board:
            print(' '.join(row))
        print(f"Start: {self.start}")
        print(f"Stop: {self.stop}")
        print(f"Obstacles: {self.obstacles}")
        print(f"Path: {self.path}")


    def save_to_file(self, filename='board.txt'):
        with open(filename, 'w') as file:
            for row in self.board:
                file.write(' '.join(row) + '\n')
            file.write(f"Start: {self.start}\n")
            file.write(f"Stop: {self.stop}\n")
            file.write(f"Obstacles: {self.obstacles}\n")
            file.write(f"Path: {self.path}\n")


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


# Start Game
game = SimpleGame(5, 5)


while True:
    game.display_board()
    direction = input("Podaj kierunek ruchu (left/right/up/down): ")
    if direction.lower() in ['left', 'right', 'up', 'down']:
        game.move(direction.lower())

        # Dodaj nową pozycję do ścieżki i oznacz na planszy
        game.path.append(game.start)
        game.board[game.start[1]][game.start[0]] = '*'

        # Sprawdź, czy osiągnięto cel
        if game.start == game.stop:
            print("Gratulacje! Osiągnięto cel.")
            break
    else:
        print("Nieprawidłowy kierunek. Podaj 'left', 'right', 'up' lub 'down'.")

# Zapis planszy do pliku
game.save_to_file('board.txt')
