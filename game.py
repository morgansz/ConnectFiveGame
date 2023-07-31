class Game:
    def __init__(self):
        self.size = 0
        self.board = []
        self.current_player = ""
        self.game_over = False

    def start_game(self, size: int) -> None:
        """
        Start a new game with the specified board size.
        """
        self.size = size
        self.board = [[" " for _ in range(size)] for _ in range(size)]
        self.current_player = "X"
        self.game_over = False

    def make_move(self, column: int) -> bool:
        """
        Make a move by placing the current player's piece in the specified column.
        Returns True if the move is valid and False otherwise.
        """
        if self.game_over:
            return False

        if column < 0 or column >= self.size:
            return False

        for row in range(self.size - 1, -1, -1):
            if self.board[row][column] == " ":
                self.board[row][column] = self.current_player
                if self.is_winner():
                    self.game_over = True
                elif self.is_board_full():
                    self.game_over = True
                else:
                    self.switch_player()
                return True

        return False

    def is_winner(self) -> bool:
        """
        Check if the current player has won the game.
        Returns True if the current player has won and False otherwise.
        """
        # Check rows
        for row in range(self.size):
            for col in range(self.size - 4):
                if (
                    self.board[row][col] == self.current_player
                    and self.board[row][col + 1] == self.current_player
                    and self.board[row][col + 2] == self.current_player
                    and self.board[row][col + 3] == self.current_player
                    and self.board[row][col + 4] == self.current_player
                ):
                    return True

        # Check columns
        for col in range(self.size):
            for row in range(self.size - 4):
                if (
                    self.board[row][col] == self.current_player
                    and self.board[row + 1][col] == self.current_player
                    and self.board[row + 2][col] == self.current_player
                    and self.board[row + 3][col] == self.current_player
                    and self.board[row + 4][col] == self.current_player
                ):
                    return True

        # Check diagonals (top-left to bottom-right)
        for row in range(self.size - 4):
            for col in range(self.size - 4):
                if (
                    self.board[row][col] == self.current_player
                    and self.board[row + 1][col + 1] == self.current_player
                    and self.board[row + 2][col + 2] == self.current_player
                    and self.board[row + 3][col + 3] == self.current_player
                    and self.board[row + 4][col + 4] == self.current_player
                ):
                    return True

        # Check diagonals (top-right to bottom-left)
        for row in range(self.size - 4):
            for col in range(4, self.size):
                if (
                    self.board[row][col] == self.current_player
                    and self.board[row + 1][col - 1] == self.current_player
                    and self.board[row + 2][col - 2] == self.current_player
                    and self.board[row + 3][col - 3] == self.current_player
                    and self.board[row + 4][col - 4] == self.current_player
                ):
                    return True

        return False

    def is_board_full(self) -> bool:
        """
        Check if the game board is full.
        Returns True if the board is full and False otherwise.
        """
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == " ":
                    return False
        return True

    def switch_player(self) -> None:
        """
        Switch the current player to the other player.
        """
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def display_board(self) -> None:
        """
        Display the current state of the game board.
        """
        for row in self.board:
            print(" ".join(row))
