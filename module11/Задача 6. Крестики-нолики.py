class Cell:
    def __init__(self, number):
        self.is_occupied = False
        self.number = number
        self.symbol = " "

    def set_symbol(self, symbol):
        if not self.is_occupied:
            self.symbol = symbol
            self.is_occupied = True
            return True
        else:
            return False


class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def change_cell_state(self, cell_number, symbol):
        if 1 <= cell_number <= 9:
            return self.cells[cell_number - 1].set_symbol(symbol)
        else:
            return False

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]
        for combination in winning_combinations:
            if all(self.cells[i].symbol == self.cells[combination[0]].symbol and
                   self.cells[i].is_occupied for i in combination):
                return True
        return False

    def reset_board(self):
        for cell in self.cells:
            cell.is_occupied = False
            cell.symbol = " "

    def __str__(self):
        board_str = ""
        for i, cell in enumerate(self.cells):
            board_str += f" {cell.symbol} "
            if (i + 1) % 3 != 0:
                board_str += "|"
            elif i != 8:
                board_str += "\n---+---+---\n"
        return board_str


class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0

    def make_move(self):
        while True:
            try:
                cell_number = int(input(f"{self.name}, выберите клетку (1-9): "))
                if 1 <= cell_number <= 9:
                    return cell_number
                else:
                    print("Неверный номер клетки. Пожалуйста, выберите клетку от 1 до 9.")
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите число.")


class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current_player = 0  # Index of current player

    def play_turn(self, player):
        cell_number = player.make_move()
        symbol = "X" if self.current_player == 0 else "O"
        if self.board.change_cell_state(cell_number, symbol):
            print(self.board)
            if self.board.check_winner():
                print(f"{player.name} победил!")
                player.wins += 1
                return True
            else:
                self.current_player = 1 - self.current_player
                return False
        else:
            print("Эта клетка уже занята. Попробуйте другую.")
            return False

    def play_game(self):
        self.board.reset_board()
        print("Начало игры!\n")
        print(self.board)
        while True:
            if self.play_turn(self.players[self.current_player]):
                return True
            if all(cell.is_occupied for cell in self.board.cells):
                print("Ничья!")
                return True

    def start_game(self):
        while True:
            self.play_game()
            print(f"Счёт: {self.players[0].name} - {self.players[0].wins}, {self.players[1].name} - {self.players[1].wins}")
            play_again = input("Играть ещё раз? (да/нет): ").lower()
            if play_again != "да":
                print("Игра окончена.")
                break


player1 = Player("Игрок 1")
player2 = Player("Игрок 2")
game = Game(player1, player2)
game.start_game()