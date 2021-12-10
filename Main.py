# Hasami Shogi - Variant 1
# By Josh Harris (jharrisjoshua)

# Description:  The program represents an abstract board game called Hasami Shogi, variant 1. The players start with
#               nine pieces on the first and last rank(row) of a 9x9 board. Black moves first, followed by Red. A
#               player wins by capturing all but one of their opponents pieces. Pieces can move to any empty space on
#               the same rank or file(no jumping). You can capture enemy pieces (one or multiple) by blocking them on
#               opposite sides with two of your pieces( corner pieces must be blocked orthogonally). Win condition is
#               assumed to be all or all but one piece captured.

import pygame, sys
from pygame.locals import *
from Game import HasamiShogiGame

WINDOW_WIDTH = 770
WINDOW_HEIGHT = 930
SQUARE_WIDTH = 72
SQUARE_HEIGHT = 90
BOARD_SIZE = 9
BORDER = 50
GAP_SIZE = 2
BLACK_COLOR = (0, 0, 0)
GREEN_COLOR = (0, 255, 0)
BACKGROUND_IMAGE = pygame.image.load('images/Background.png')


def main():
    """Hasami Shogi implemented in Pygame."""
    pygame.init()
    game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Hasami Shogi')

    game_display.blit(BACKGROUND_IMAGE, BACKGROUND_IMAGE.get_rect())
    game = HasamiShogiGame()
    game_board = game.get_board()

    select_count = 0
    from_row, from_col, to_row, to_col = None, None, None, None
    mouse_x, mouse_y = 0, 0

    ### Test ###
    test_code = False
    test_case = 0
    if test_code:
        move_list = [(8, 0), (1, 0), (0, 8), (2, 8), (1, 0), (1, 7), (2, 8), (2, 7), (8, 8), (1, 8), (0, 0), (8, 0), (1, 8), (1, 6), (2, 7), (1, 7), (8, 5), (1, 5), (1, 7), (2, 7), (8, 7), (3, 7), (0, 1), (0, 0), (1, 6), (1, 7), (0, 0), (6, 0), (1, 5), (2, 5), (0, 2), (0, 0), (1, 7), (1, 8), (0, 0), (5, 0), (1, 8), (0, 8), (0, 3), (0, 0), (8, 4), (8, 5), (0, 0), (4, 0), (8, 2), (7, 2), (0, 6), (2, 6), (3, 7), (2, 7), (0, 4), (2, 4), (2, 7), (2, 6), (0, 7), (2, 7), (8, 6), (2, 6), (2, 4), (2, 5), (8, 5), (7, 5), (0, 5), (1, 5), (0, 8), (0, 5), (2, 5), (2, 3), (7, 2), (2, 2), (2, 7), (2, 4), (8, 3), (3, 3), (4, 0), (4, 1), (3, 3), (3, 0), (4, 1), (4, 0), (7, 5), (7, 0), (2, 4), (2, 5), (8, 1), (8, 5), (2, 5), (2, 4), (8, 5), (2, 5)]

        for index in range(0, 80, 2):
            game.make_move(move_list[index][0], move_list[index][1], move_list[index + 1][0], move_list[index + 1][1])
        if test_case == 1:
            for index in range(80, 88, 2):
                game.make_move(move_list[index][0], move_list[index][1], move_list[index + 1][0], move_list[index + 1][1])
    ######

    while True:
        if game.get_game_state() != "UNFINISHED":
            break
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
            if event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                # Second Square selected - To Square
                if select_count == 1:
                    to_row, to_col = game_board.get_square(mouse_x, mouse_y)
                    # Clear possible moves
                    game.clear_moves()
                    # Check move is valid and make move
                    game.make_move(from_row, from_col, to_row, to_col)
                    select_count, from_row, from_col, to_row, to_col = None, None, None, None, None
                # First square selected - From Square
                if select_count == 0:
                    from_row, from_col = game_board.get_square(mouse_x, mouse_y)
                    if from_row is not None and from_col is not None:
                        if game.get_active_player()[0] == game_board.get_square_state(from_row, from_col):
                            select_count = 1
                            # Show possible moves
                            game.show_moves(from_row, from_col)
                # No selection
                if select_count is None:
                    select_count = 0
        row, column = game_board.get_square(mouse_x, mouse_y)

        game_display.blit(BACKGROUND_IMAGE, BACKGROUND_IMAGE.get_rect())
        fill_border(game_display)
        if row is not None and column is not None:
            highlight_square(game_display, row, column)
        game_info(game_display, game)
        game_board.display_board(game_display)
        pygame.display.update()

    if game.get_game_state() == "BLACK_WON":
        text = "Black Won. Would you like to play again?"
    else:
        text = "Red Won. Would you like to play again?"
    font = pygame.font.SysFont("Calibri", 20, bold=True)
    text_box = font.render(text, True, GREEN_COLOR, BLACK_COLOR)
    text_rect = text_box.get_rect()
    text_rect.center = (int(WINDOW_WIDTH / 2), int(WINDOW_HEIGHT / 2))
    game_display.blit(text_box, text_rect)

    text_box_yes = font.render("Yes", True, GREEN_COLOR, BLACK_COLOR)
    text_rect_yes = text_box_yes.get_rect()
    text_rect_yes.center = (int(WINDOW_WIDTH / 2) - 60, int(WINDOW_HEIGHT / 2) + 90)

    text_box_no = font.render("No", True, GREEN_COLOR, BLACK_COLOR)
    text_rect_no = text_box_no.get_rect()
    text_rect_no.center = (int(WINDOW_WIDTH / 2) + 60, int(WINDOW_HEIGHT / 2) + 90)

    # Game Display once finished.
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                if text_rect_yes.collidepoint(mouse_x, mouse_y):
                    main()
                elif text_rect_no.collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    sys.exit()

        game_display.blit(BACKGROUND_IMAGE, BACKGROUND_IMAGE.get_rect())
        fill_border(game_display)
        game_info(game_display, game)
        game_board.display_board(game_display)
        game_display.blit(text_box, text_rect)
        game_display.blit(text_box_yes, text_rect_yes)
        game_display.blit(text_box_no, text_rect_no)
        pygame.display.update()


def fill_border(game_display):
    """Fills in the border of the board."""
    pygame.draw.rect(game_display, BLACK_COLOR, (BORDER, BORDER,
                                                 (SQUARE_WIDTH + 2) * 9 + 2, (SQUARE_HEIGHT + 2) * 9 + 2))


def highlight_square(game_display, row, column):
    """Highlights the current square."""
    x, y = get_square_location(row, column)
    pygame.draw.rect(game_display, GREEN_COLOR, (x, y, SQUARE_WIDTH + 4, SQUARE_HEIGHT + 4))


def get_square_location(row, column):
    """Returns the location of square as pixels."""
    x = column * (SQUARE_WIDTH + GAP_SIZE) + BORDER
    y = row * (SQUARE_HEIGHT + GAP_SIZE) + BORDER
    return [x, y]


def game_info(game_display, game):
    """Displays the current game's information."""
    font = pygame.font.SysFont("Calibri", 20, bold=True)
    black_score = game.get_num_captured_pieces("RED")
    red_score = game.get_num_captured_pieces("BLACK")
    active_player = game.get_active_player().capitalize()
    display_info = font.render("Black's Score: %s    Red's Score: %s    %s's Turn" %
                                    (str(black_score), str(red_score), active_player), False, GREEN_COLOR)
    info_rect = display_info.get_rect()
    info_rect.topright = (WINDOW_WIDTH - 50, 10)
    game_display.blit(display_info, info_rect)


if __name__ == '__main__':
    main()
