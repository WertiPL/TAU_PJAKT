# Wiktor Rostkowski s23141
import random


class SimpleGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
        self.start = self.generate_start()
        self.stop = self.generate_stop()
        self.obstacles = self.generate_obstacles()
        self.path = []
        self.generate_path()

    def generate_start(self):
        side = random.choice(['top', 'bottom', 'left', 'right'])
        if side == 'top':
            return (random.randint(0, self.width - 1), 0)
        elif side == 'bottom':
            return (random.randint(0, self.width - 1), self.height - 1)
        elif side == 'left':
            return (0, random.randint(0, self.height - 1))
        else:  # right
            return (self.width - 1, random.randint(0, self.height - 1))

    def generate_stop(self):
        stop_side = random.choice(['top', 'bottom', 'left', 'right'])
        stop = self.generate_point_on_side(stop_side)
        while stop == self.start:
            stop_side = random.choice(['top', 'bottom', 'left', 'right'])
            stop = self.generate_point_on_side(stop_side)
        return stop

    def generate_point_on_side(self, side):
        if side == 'top':
            return (random.randint(0, self.width - 1), 0)
        elif side == 'bottom':
            return (random.randint(0, self.width - 1), self.height - 1)
        elif side == 'left':
            return (0, random.randint(0, self.height - 1))
        else:  # right
            return (self.width - 1, random.randint(0, self.height - 1))

    def generate_obstacles(self):
        num_obstacles = random.randint(3, min(self.width, self.height) - 1)
        obstacles = set()

        while len(obstacles) < num_obstacles:
            obstacle = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if obstacle != self.start and obstacle != self.stop:
                obstacles.add(obstacle)

        return obstacles

    def generate_path(self):
        x, y = self.start
        self.board[y][x] = 'S'

        for obstacle in self.obstacles:
            self.board[obstacle[1]][obstacle[0]] = 'X'

        # while (x, y) != self.stop:
        #     if x < self.stop[0]:
        #         x += 1
        #     elif x > self.stop[0]:
        #         x -= 1
        #     if y < self.stop[1]:
        #         y += 1
        #     elif y > self.stop[1]:
        #         y -= 1
        #     self.path.append((x, y))
        #     self.board[y][x] = '*'

        x, y = self.stop
        self.board[y][x] = 'F'

    def display_board(self):
        for row in self.board:
            print(' '.join(row))

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
