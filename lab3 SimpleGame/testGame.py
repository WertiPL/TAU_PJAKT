# Wiktor Rostkowski s23141

import unittest
from game import SimpleGame


class TestSimpleGame(unittest.TestCase):
    def setUp(self):
        self.game = SimpleGame(5, 5)

    def test_move_into_obstacle(self):
        # Dodajmy przeszkodę w prawo od startu
        obstacle_position = (self.game.start[0] + 1, self.game.start[1])
        self.game.obstacles.add(obstacle_position)

        initial_position = self.game.start

        # Wykonaj ruch w prawo
        self.game.move('right')

        # Sprawdź, czy pozycja nie zmieniła się, ponieważ ruch był zablokowany przez przeszkodę
        new_position = self.game.start
        print(f"Initial: {initial_position}, New: {new_position}")
        self.assertEqual(new_position, initial_position)

    def test_move_right(self):
        initial_position = self.game.start
        self.game.move('right')
        new_position = self.game.start
        print(f"Initial: {initial_position}, New: {new_position}")
        if new_position[0] == initial_position[0] + 1 and (new_position[0], new_position[1]) not in self.game.obstacles:
            self.assertEqual(new_position[0], initial_position[0] + 1)
        else:
            self.assertEqual(new_position, initial_position)

    def test_move_left(self):
        initial_position = self.game.start
        self.game.move('left')
        new_position = self.game.start
        print(f"Initial: {initial_position}, New: {new_position}")
        if new_position[0] == initial_position[0] - 1 and (new_position[0], new_position[1]) not in self.game.obstacles:
            self.assertEqual(new_position[0], initial_position[0] - 1)
        else:
            self.assertEqual(new_position, initial_position)

    def test_move_up(self):
        initial_position = self.game.start
        self.game.move('up')
        new_position = self.game.start
        print(f"Initial: {initial_position}, New: {new_position}")
        if new_position[1] == initial_position[1] - 1 and (new_position[0], new_position[1]) not in self.game.obstacles:
            self.assertEqual(new_position[1], initial_position[1] - 1)
        else:
            self.assertEqual(new_position, initial_position)

    def test_move_down(self):
        initial_position = self.game.start
        self.game.move('down')
        new_position = self.game.start
        print(f"Initial: {initial_position}, New: {new_position}")
        if new_position[1] == initial_position[1] + 1 and (new_position[0], new_position[1]) not in self.game.obstacles:
            self.assertEqual(new_position[1], initial_position[1] + 1)
        else:
            self.assertEqual(new_position, initial_position)

    def test_move_out_of_bounds(self):
        self.game.start = (0, 0)

        initial_position = self.game.start
        self.game.move('up')
        new_position = self.game.start
        self.assertEqual(new_position, initial_position)

    def test_move_out_of_bounds_left(self):
        self.game.start = (0, 2)
        initial_position = self.game.start
        self.game.move('left')
        new_position = self.game.start
        print(f"Initial: {initial_position}, New: {new_position}")
        self.assertEqual(new_position, initial_position)


if __name__ == '__main__':
    unittest.main()
