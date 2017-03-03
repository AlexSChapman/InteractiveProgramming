"""
This is a simple tic tac toe game that is meant to be implemented
as a multiplayer game.
I can be modified to play with the computer, however the default is
with another player

@Author: Peter Seger
"""
import pygame
import time


class board():
    """
    This is the game board which contains functions to:
    -Create the board
    -Update the board
    -Print the board
    -Add a play piece
    -Clear the board
    """

    def __init__(self):
        self.board_vals = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

    def print_board(self):
        print('   |   |')
        print(' ' + self.board_vals[1] + ' | ' + self.board_vals[2] + ' | ' + self.board_vals[3])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board_vals[4] + ' | ' + self.board_vals[5] + ' | ' + self.board_vals[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board_vals[7] + ' | ' + self.board_vals[8] + ' | ' + self.board_vals[9])
        print('   |   |')

    def insert_play(self, play, play_piece):
        self.board_vals[play] = play_piece


class Board():
    def __init__(self, height=300, width=300):
        self.height = height
        self.width = width


class TicTacToeModel:
    """ Encodes the game state """
    def __init__(self):
        self.piece = []
        x_pos = [100, 400, 700]
        y_pos = [100, 400, 700]
        for x in x_pos:
            for y in y_pos:
                piece = Piece((0, 15, 0), 20, 20, x, y)
                self.piece.append(piece)


class Piece:
    def __init__(self, color, height, width, x, y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def collision(self, x, y):
        x_range = range(self.x, self.x + 20)
        y_range = range(self.y, self.y + 20)
        if x in x_range and y in y_range:
            return True
        else:
            return False


class PyGameWindowView:
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen

    def draw(self):
        self.screen.fill(pygame.Color(0, 0, 0))
        for pieces in self.model.piece:
            pygame.draw.rect(self.screen, pygame.Color(pieces.color), pygame.Rect(pieces.x, pieces.y, pieces.width, pieces.height))
        pygame.display.update()


# class PyGameMouseController:
#     def __init__(self, model):
#         self.model = model
#
#     def handle_mouse_event(self, event):
#         if event.type == pygame.MOUSEMOTION:
#             self.model.piece.x = event.pos[0] - self.model.piece.width/2.0


if __name__ == '__main__':
    # test = board()
    # test.insert_play(3, "X")
    # test.print_board()

    pygame.init()

    size = (840, 840)
    screen = pygame.display.set_mode(size)

    model = TicTacToeModel()
    view = PyGameWindowView(model, screen)
    # controller = PyGameMouseController(model)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for pieces in model.piece:
                    if pieces.collision(x, y):
                        print("collision at: " + str(pieces.x) + ' ' + str(pieces.y))
                        pieces.color = (12, 45, 78)
                        print(pieces.color)
                    view.draw()
        view.draw()
        time.sleep(.001)

    pygame.quit()
