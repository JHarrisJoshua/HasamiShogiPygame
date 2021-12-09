# Hasami Shogi - Variant 1
# By Josh Harris (jharrisjoshua)

# Description:  The program represents an abstract board game called Hasami Shogi, variant 1. The players start with
#               nine pieces on the first and last rank(row) of a 9x9 board. Black moves first, followed by Red. A
#               player wins by capturing all but one of their opponents pieces. Pieces can move to any empty space on
#               the same rank or file(no jumping). You can capture enemy pieces (one or multiple) by blocking them on
#               opposite sides with two of your pieces( corner pieces must be blocked orthogonally). Win condition is
#               assumed to be all or all but one piece captured.

from Board import Board


class HasamiShogiGame:
    """The class represents a game of Hasami Shogi."""
    def __init__(self):
        """Creates a new game of Hasami Shogi."""
        self._board = Board()
        self._current_player = "BLACK"
        self._game_state = "UNFINISHED"
        self._captured_pieces = dict(BLACK=0, RED=0)

    def get_board(self):
        """Returns the game board."""
        return self._board

    def get_game_state(self):
        """Returns the state of the game, unfinished, red won, or black won."""
        return self._game_state

    def get_active_player(self):
        """Returns whose turn it is, red or black."""
        return self._current_player

    def get_num_captured_pieces(self, player_color):
        """Returns the number of pieces of that color that have been captured."""
        if player_color in ("BLACK", "RED"):
            return self._captured_pieces[player_color]

    def get_square_occupant(self, row, col):
        """Returns whether the specified square is occupied by a red piece, black piece, or neither."""
        square_occupant = self._board.get_square_state(row, col)
        if self._check_sqr_valid(row, col):
            return "BLACK" if square_occupant == 'B' else "RED" if square_occupant == 'R' else "NONE"

    def make_move(self, from_row, from_col, to_row, to_col):
        """
        The function makes a move(if valid), removes any captured pieces, and updates the game state and turn. Returns
        True if valid, else returns False.
        """
        if self._game_state != "UNFINISHED":  # Check Game State
            return False
        if not self._check_sqrs_valid(from_row, from_col, to_row, to_col):
            return False
        if not self._check_move(from_row, from_col, to_row, to_col, self._board):
            return False

        self._board.set_square(to_row, to_col, self._current_player)  # Make move
        self._board.set_square(from_row, from_col)  # Remove player at from square
        self._check_for_captures(from_row, from_col, to_row, to_col)  # Check for and capture pieces
        self._update_game_state()  # Update game state

        if self._game_state == "UNFINISHED":   # Update turn
            self._current_player = "RED" if self._current_player == "BLACK" else "BLACK"
        return True

    def _check_sqr_valid(self, row=None, col=None):
        """Return True if the specified Square is valid."""
        if row is None or col is None:
            return False
        return True

    def _check_sqrs_valid(self, from_row=None, from_col=None, to_row=None, to_col=None):
        """Return True if the specified Squares are valid."""
        if from_row is None or from_col is None or to_row is None or to_col is None:
            return False
        return True

    def _check_move(self, from_row, from_col, to_row, to_col, board):
        """Check if move is valid."""
        # Check if from square is not for current player.
        if self._current_player[0] != board.get_square_state(from_row, from_col):
            return False
        # From square and to square are the same, or both row and column changed.
        if (from_row == to_row and from_col == to_col) or (from_row != to_row and from_col != to_col):
            return False
        # Check each square is empty based on a move along row or column
        from_val, to_val, row = (from_col, to_col, True) if from_row == to_row else (from_row, to_row, False)
        move_direction = int((to_val - from_val) / abs(to_val - from_val))
        for val in range(from_val + move_direction, to_val + move_direction, move_direction):
            if board.get_square_state((from_row if row else val), (val if row else from_col)) != ".":
                return False
        return True

    def _check_for_captures(self, from_row, from_col, to_row, to_col):
        """Checks for captures, removes captured pieces, and updates count of captured pieces."""
        captured_pieces = list()

        if (to_row, to_col) in ((1, 0), (0, 1), (7, 0), (8, 1), (0, 7), (1, 8), (7, 8), (8, 7)):
            corner_capture = self._check_corners(to_row, to_col)
            if corner_capture is not None:
                captured_pieces.append(corner_capture)

        # Determine which direction piece moved, relative to black side of board.
        direction = "RIGHT" if to_col>from_col else "UP" if to_row<from_row else "LEFT" if to_col<from_col else "DOWN"
        non_corner_captures = self._check_non_corners(to_row, to_col, direction)  # Check non-corner captures
        if non_corner_captures is not None and len(non_corner_captures) > 0:
            captured_pieces.extend(non_corner_captures)

        # If win condition is set to 10, all of opponent's pieces may be captured (set to 9 for all but one).
        win_condition = 10
        if self._captured_pieces[self._color_captured()] + len(captured_pieces) < win_condition:
            self._remove_pieces(captured_pieces)
            self._captured_pieces[self._color_captured()] += len(captured_pieces)

    def _color_captured(self):
        """Returns the player defending pieces."""
        return "RED" if self._current_player == "BLACK" else "BLACK"

    def _check_corners(self, to_row, to_col):
        """Check corners for captures. To square must be in one of eight positions."""
        defender = self._color_captured()

        if (to_row, to_col) in ((1, 0), (0, 1)):
            if self.get_square_occupant(1, 0) == self.get_square_occupant(0, 1) == self._current_player:
                if self.get_square_occupant(0, 0) == defender:
                    return (0, 0)
        elif (to_row, to_col) in ((7, 0), (8, 1)):
            if self.get_square_occupant(7, 0) == self.get_square_occupant(8, 1) == self._current_player:
                if self.get_square_occupant(8, 0) == defender:
                    return (8, 0)
        elif (to_row, to_col) in ((0, 7), (1, 8)):
            if self.get_square_occupant(0, 7) == self.get_square_occupant(1, 8) == self._current_player:
                if self.get_square_occupant(0, 8) == defender:
                    return (0, 8)
        else:
            if self.get_square_occupant(7, 8) == self.get_square_occupant(8, 7) == self._current_player:
                if self.get_square_occupant(8, 8) == defender:
                    return (8, 8)

    def _check_non_corners(self, to_row, to_col, direction):
        """Check for non-corner captures based on the direction of move. Checks in three directions from to_sqr."""
        defender = self._color_captured()
        captured_pieces = list()

        if direction in ("UP", "LEFT", "RIGHT") and to_row > 0:  # Check up - along column
            captured_pieces.extend(self._check_direction(defender, to_row-1, -1, -1, to_col, False))
        if direction in ("UP", "LEFT", "DOWN") and to_col > 0:  # Check left - along row
            captured_pieces.extend(self._check_direction(defender, to_col-1, -1, -1, to_row, True))
        if direction in ("DOWN", "LEFT", "RIGHT") and to_row < 8:  # Check down - along column
            captured_pieces.extend(self._check_direction(defender, to_row+1, 9, 1, to_col, False))
        if direction in ("UP", "DOWN", "RIGHT") and to_col < 8:  # Check right - along row
            captured_pieces.extend(self._check_direction(defender, to_col+1, 9, 1, to_row, True))
        return captured_pieces

    def _check_direction(self, defender, start, end, inc, to_val, row):
        """Checks the direction for custodian captures and returns captures. Helper to _check_non_corners."""
        valid_capture, pieces_in_play, captured_pieces = True, list(), list()
        for val in range(start, end, inc):
            square_value = self._board.get_square_state(to_val if row else val, val if row else to_val)
            if square_value == '.':
                valid_capture = False
            if square_value == self._current_player[0] and valid_capture:
                captured_pieces.extend(pieces_in_play)
                valid_capture = False
            if square_value == defender[0] and valid_capture:
                pieces_in_play.append((to_val if row else val, val if row else to_val))
        return captured_pieces

    def _remove_pieces(self, captured_squares):
        """Remove captured pieces from the board."""
        for row, col in captured_squares:
            self._board.set_square(row, col)

    def _update_game_state(self):
        """Updates the game state after each move."""
        if self._captured_pieces["BLACK"] >= 8:
            self._game_state = "RED_WON"
        elif self._captured_pieces["RED"] >= 8:
            self._game_state = "BLACK_WON"

    def show_moves(self, from_row, from_col):
        """For the selected square, show the possible moves."""
        # Check each direction for possible moves
        set_green = list()
        if from_row > 0:  # Check up - along column
            set_green.extend(self._check_possible(from_row - 1, -1, -1, from_col, False))
        if from_col > 0:  # Check left - along row
            set_green.extend(self._check_possible(from_col - 1, -1, -1, from_row, True))
        if from_row < 8:  # Check down - along column
            set_green.extend(self._check_possible(from_row + 1, 9, 1, from_col, False))
        if from_col < 8:  # Check right - along row
            set_green.extend(self._check_possible(from_col + 1, 9, 1, from_row, True))
        if len(set_green) > 0:
            for (row, col) in set_green:
                self._board.set_square(row, col, "GREEN")

    def _check_possible(self, start, end, inc, from_val, row):
        """Check direction for possible moves."""
        valid_move, valid_squares = True, list()
        for val in range(start, end, inc):
            sqr_val = self._board.get_square_state(from_val if row else val, val if row else from_val)
            if sqr_val != ".":
                valid_move = False
            if sqr_val == "." and valid_move:
                valid_squares.append((from_val if row else val, val if row else from_val))
        return valid_squares

    def clear_moves(self):
        """Clear the possible moves displayed from the board."""
        self._board.clear_green()
