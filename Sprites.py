# Hasami Shogi - Variant 1
# By Josh Harris (jharrisjoshua)

# Description:  The program represents an abstract board game called Hasami Shogi, variant 1. The players start with
#               nine pieces on the first and last rank(row) of a 9x9 board. Black moves first, followed by Red. A
#               player wins by capturing all but one of their opponents pieces. Pieces can move to any empty space on
#               the same rank or file(no jumping). You can capture enemy pieces (one or multiple) by blocking them on
#               opposite sides with two of your pieces( corner pieces must be blocked orthogonally). Win condition is
#               assumed to be all or all but one piece captured.

import pygame


class Sprites(pygame.sprite.Sprite):
    """Represents the sprites for each square."""
    def __init__(self, row, col, square_state):
        """Initialize sprite to represent each square on the board."""
        pygame.sprite.Sprite.__init__(self)
        self._row = row
        self._col = col
        self._square_state = square_state
        self._black_img = pygame.image.load('images/Black.png')
        self._red_img = pygame.image.load('images/Red.png')
        self._blank_img = pygame.image.load('images/Blank.png')
        self._green_img = pygame.image.load('images/Green.png')

        if square_state == "B":
            self.image = self._black_img
        elif square_state == "R":
            self.image = self._red_img
        else:
            self.image = self._blank_img

        self._size = self.image.get_rect().size
        self.rect = pygame.Rect(col * self._size[0] + 50 + 2 * (col + 1), row * self._size[1] + 50 + 2 * (row + 1),
                                self._size[0], self._size[1])

    def get_state(self):
        """Gets the state of the Square Sprite."""
        return self._square_state

    def set_state(self, new_state=None):
        """Sets the state of the Square Sprite"""
        if new_state is None:
            self._square_state = "."
            self.image = self._blank_img
        elif new_state == "BLACK":
            self._square_state = "B"
            self.image = self._black_img
        elif new_state == "RED":
            self._square_state = "R"
            self.image = self._red_img
        elif new_state == "GREEN":
            self._square_state = "G"
            self.image = self._green_img
