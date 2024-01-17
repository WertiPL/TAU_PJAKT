# Wiktor Rostkoski s23141
from game import SimpleGame

game = SimpleGame(5, 5)
game.display_board()

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