import tkinter as tk
from tkinter import messagebox

ROWS = 6
COLS = 7
SQUARE_SIZE = 80
EMPTY = 0
PLAYER1_PIECE = 1
PLAYER2_PIECE = 2


class ConnectFourGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Connect Four")
        self.canvas = tk.Canvas(self.root, width=COLS * SQUARE_SIZE, height=(ROWS + 1) * SQUARE_SIZE)
        self.canvas.pack()
        self.draw_board()
        self.board = [[EMPTY] * COLS for _ in range(ROWS)]
        self.current_player = PLAYER1_PIECE
        self.game_over = False
        self.canvas.bind("<Button-1>", self.drop_piece)
        self.root.mainloop()

    def draw_board(self):
       
        for row in range(ROWS):
            for col in range(COLS):
                x1 = col * SQUARE_SIZE
                y1 = (row + 1) * SQUARE_SIZE
                x2 = x1 + SQUARE_SIZE
                y2 = y1 + SQUARE_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="blue", fill="white")

    def drop_piece(self, event):
       
        if not self.game_over:
            col = event.x // SQUARE_SIZE
            if self.is_valid_location(col):
                row = self.get_next_open_row(col)
                self.drop_piece_on_board(row, col)
                if self.winning_move(PLAYER1_PIECE) or self.winning_move(PLAYER2_PIECE):
                    winner = "Player 1" if self.current_player == PLAYER2_PIECE else "Player 2"
                    messagebox.showinfo("Game Over", f"{winner} wins!")
                    self.game_over = True
                elif self.is_board_full():
                    messagebox.showinfo("Game Over", "It's a draw!")
                    self.game_over = True
                else:
                    self.current_player = PLAYER1_PIECE if self.current_player == PLAYER2_PIECE else PLAYER2_PIECE

    def is_valid_location(self, col):
        """Check if a column is a valid location to place a piece."""
        return self.board[ROWS - 1][col] == EMPTY

    def get_next_open_row(self, col):
        """Get the next available row for a piece in a column."""
        for r in range(ROWS):
            if self.board[r][col] == EMPTY:
                return r

    def drop_piece_on_board(self, row, col):
        """Drop a piece onto the board."""
        self.board[row][col] = self.current_player
        color = "red" if self.current_player == PLAYER1_PIECE else "yellow"
        self.canvas.create_oval(col * SQUARE_SIZE, row * SQUARE_SIZE, (col + 1) * SQUARE_SIZE,
                                (row + 1) * SQUARE_SIZE, fill=color)

    def winning_move(self, piece):
        """Check if the most recent move resulted in a win."""
        # Check horizontal locations
        for c in range(COLS - 3):
            for r in range(ROWS):
                if self.board[r][c] == piece and self.board[r][c + 1] == piece and self.board[r][c + 2] == piece and \
                        self.board[r][c + 3] == piece:
                    return True

        # Check vertical locations
        for c in range(COLS):
            for r in range(ROWS - 3):
                if self.board[r][c] == piece and self.board[r + 1][c] == piece and self.board[r + 2][c] == piece and \
                        self.board[r + 3][c] == piece:
                    return True

        # Check positively sloped diagonals
        for c in range(COLS - 3):
            for r in range(ROWS - 3):
                if self.board[r][c] == piece and self.board[r + 1][c + 1] == piece and self.board[r + 2][
                    c + 2] == piece and self.board[r + 3][c + 3] == piece:
                    return True

        # Check negatively sloped diagonals
        for c in range(COLS - 3):
            for r in range(3, ROWS):
                if self.board[r][c] == piece and self.board[r - 1][c + 1] == piece and self.board[r - 2][
                    c + 2] == piece and self.board[r - 3][c + 3] == piece:
                    return True

        return False

    def is_board_full(self):
        """Check if the board is full."""
        return all(self.board[0][col] != EMPTY for col in range(COLS))


if __name__ == "__main__":
    ConnectFourGUI()
