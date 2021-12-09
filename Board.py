# Hasami Shogi - Variant 1
# By Josh Harris (jharrisjoshua)

# Description:  The program represents an abstract board game called Hasami Shogi, variant 1. The players start with
#               nine pieces on the first and last rank(row) of a 9x9 board. Black moves first, followed by Red. A
#               player wins by capturing all but one of their opponents pieces. Pieces can move to any empty space on
#               the same rank or file(no jumping). You can capture enemy pieces (one or multiple) by blocking them on
#               opposite sides with two of your pieces( corner pieces must be blocked orthogonally). Win condition is
#               assumed to be all or all but one piece captured.

import pygame
from Sprites import Sprites


class Board:
    """Represents the 9x9 board in a game of Hasami Shogi."""

    def __init__(self):
        """Creates the 9x9 board for a game of Hasami Shogi. Stores the state of each square on the board."""

        # Pygame Sprites Group
        self._sprite_group = pygame.sprite.Group()

        def _make_board(board_size=9):
            """Initialize Hasami Shogi board with pieces on first and last rank(row)."""
            shogi_board = []
            for row in range(board_size):
                shogi_board.append([])
                for col in range(board_size):
                    if row == 0:
                        sprite = Sprites(row, col, "R")
                    elif row == board_size - 1:
                        sprite = Sprites(row, col, "B")
                    else:
                        sprite = Sprites(row, col, ".")
                    self._sprite_group.add(sprite)
                    shogi_board[row].append(sprite)
            return shogi_board

        # Initialize Board and Square Sprites.
        self._shogi_board = _make_board()

    def display_board(self, game_display):
        """Displays the current board in Pygame."""
        self._sprite_group.draw(game_display)

    def get_square(self, mouse_x, mouse_y):
        """Returns the row and column of the square based on mouse coordinates."""
        for row in range(9):
            for col in range(9):
                sprite = self._shogi_board[row][col]
                if sprite.rect.collidepoint(mouse_x, mouse_y):
                    return [row, col]
        return [None, None]

    def get_square_state(self, row, col):
        """Returns current state of a square on the board."""
        return self._shogi_board[row][col].get_state()

    def set_square(self, row, col, state=None):
        """Updates the state of the specified square."""
        self._shogi_board[row][col].set_state(state)

    def clear_green(self):
        """Reset green squares to blank."""
        for row in range(9):
            for col in range(9):
                if self._shogi_board[row][col].get_state() == "G":
                    self._shogi_board[row][col].set_state()
