"""
This is a simple tic tac toe game that is meant to be implemented
as a multiplayer game.
It is the mega tic tac toe version that has nine game boards in
a master game board.

@Author: Peter Seger, Alex Chapman
"""
import pygame
import time
from com_client import client
import ast
import pygame_textinput # Import the textinput-module

clock = pygame.time.Clock()
WIDTH = 800
BOX_WIDTH = 20
GAP_WIDTH = 20
gap = 30
COLOR = None

class Board():
    def __init__(self, pieces, focus, height=300, width=300, color='Grey'):
        self.focus = focus
        self.height = height
        self.width = width
        self.color = color
        self.pieces = pieces


class Piece:
    def __init__(self, color, height=20, width=20, x=0, y=0):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def set_color(self, color='Green'):
        self.color = color

    def get_color(self):
        return 'hello' + self.color

    def collision(self, x, y):
        x_range = range(int(self.x), int(self.x) + self.width)
        y_range = range(int(self.y), int(self.y) + self.height)
        if x in x_range and y in y_range:
            return True
        else:
            return False


class Game():
    def __init__(self, pieces=[], focus=0):
        self.pieces = pieces    # List of game pieces
        self.focus = focus  # Focus used to determine if the game is active


def readin_data(data):
    """
    This function takes a list of nested lists and does the following:
    -unzips unto each game
    -makes board objects for each game
        -makes pieces objects for each board

    Returns all the pieces with the correct x and y values
    """
    width = WIDTH  # This can be changed
    height = WIDTH    # This can be changed

    row1 = data[0]
    row2 = data[1]
    row3 = data[2]

    game1 = row1[0]
    game2 = row1[1]
    game3 = row1[2]

    game4 = row2[0]
    game5 = row2[1]
    game6 = row2[2]

    game7 = row3[0]
    game8 = row3[1]
    game9 = row3[2]

    game_colors = [game1, game2, game3, game4, game5, game6, game7, game8, game9]
    game_objs = []
    # build a list of pieces for each game with [0] being the focus value
    j = 0
    for game in game_colors:
        gametemp = Game()
        pieces = []
        gametemp.focus = game[0]
        for i in range(1, 10):
            piece = Piece('Green')
            piece.color = game[i]
            piece.x = 0  # Set default x value
            piece.y = 0  # Set default y value
            pieces.append(piece)
        gametemp.pieces = pieces
        game_objs.append(gametemp)
        j += 1

    # Send list of game objs to get assigned x and y positions
    # comes back as a list of game objs
    coordinated_pieces = coordinate_pieces(game_objs, width, height)
    return coordinated_pieces


def coordinate_pieces(game_objs, width, height):
    """
    This function takes a list of game objects, the width & hieght of the board
    Returns the same list of game objects, except with x, y, and color
    """
    CELL_WIDTH = width / 3
    CELL_HEIGHT = height / 3
    ITEM_WIDTH = gap + (WIDTH - (9*gap))/10
    ITEM_HEIGHT = ITEM_WIDTH
    for cell_num, gametemp in enumerate(game_objs):
        for index, cell in enumerate(gametemp.pieces):
            cell_row_val = int((cell_num) / 3)
            cell_column_val = cell_num % 3
            index_row_val = int((index) / 3)
            index_column_val = index % 3
            cell.x = gap + CELL_WIDTH * cell_column_val + ITEM_WIDTH * index_column_val
            cell.y = gap + CELL_HEIGHT * cell_row_val + ITEM_HEIGHT * index_row_val
    return game_objs


class View_Setup():
    """
    This class sets up the board correctly and draws the
    pieces in their place
    """
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen

    def draw(self):
        blue_o = pygame.image.load("assets/blue_o.png")
        blue_x = pygame.image.load("assets/blue_x.png")
        red_o = pygame.image.load("assets/red_o.png")
        red_x = pygame.image.load("assets/red_x.png")
        background = pygame.image.load("assets/Background.png24")

        blue_o = pygame.transform.scale(blue_o, (40, 40))
        blue_x = pygame.transform.scale(blue_x, (40, 40))
        red_o = pygame.transform.scale(red_o, (40, 40))
        red_x = pygame.transform.scale(red_x, (40, 40))
        background = pygame.transform.scale(background, (815, 815))

        self.screen.fill(pygame.Color(25, 25, 25))
        self.screen.blit(background, (-15, -15))

        for game in self.model:
            if game.focus:
                w = game.pieces[8].x + 20 - game.pieces[0].x
                pygame.draw.rect(self.screen, pygame.Color(COLOR),
                                 pygame.Rect(game.pieces[0].x - 20,
                                             game.pieces[0].y - 20,
                                             w + 40,
                                             w + 40), 5)

            for piece in game.pieces:
                piece_to_use = None
                if piece.color == 'steelblue':
                    piece_to_use = None
                elif piece.color == 'blue':
                    piece_to_use = blue_o
                elif piece.color == 'red':
                    piece_to_use = red_x
                if piece_to_use is not None:
                    self.screen.blit(piece_to_use, (piece.x, piece.y))
        pygame.display.update()


def to_array(thruput):
    """Placeholder method for determining functionality of game"""
    thruput = thruput[:int(len(thruput)/2)]
    print('attempting conversion on message')
    try:
        ls = ast.literal_eval(thruput)
        return ls
    except (SyntaxError, ValueError) as e:
        print('Player Two Has Not Yet Connected')
        return False
        # print(thruput)


def paint_boxes(ls, screen):
    gap = int((WIDTH - (9 * BOX_WIDTH)) / 10)
    for t, row in enumerate(ls):
        for i, cell in enumerate(row):
            top_base = t * ((4 * gap)+(3 * BOX_WIDTH)) + gap
            print(top_base)
            left_base = i * ((4 * gap)+(3 * BOX_WIDTH)) + gap
            for q, point in enumerate(cell):
                    x = left_base + q * (BOX_WIDTH + gap)
                    y = top_base + q * (BOX_WIDTH + gap)
                    pygame.draw.rect(screen, pygame.Color(point),
                                     pygame.Rect(x, y,
                                                 BOX_WIDTH, BOX_WIDTH))
    pygame.display.update()


def starting_screen(screen):
    run = True
    textinput = pygame_textinput.TextInput()
    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        # Feed it with events every frame
        if textinput.update(events):
            if textinput.get_text().lower() == 'red' or textinput.get_text().lower() == 'blue':
                run = False
                return textinput.get_text()

        background = pygame.image.load("assets/Background.png24")
        title_super = pygame.image.load("assets/SUPER.JPG")
        title_TicTac = pygame.image.load("assets/TicTac.JPG")

        background = pygame.transform.scale(background, (815, 815))
        title_super = pygame.transform.scale(title_super, (200, 70))
        # title_super = pygame.transform.rotate(title_super, -10)
        title_TicTac = pygame.transform.scale(title_TicTac, (600, 85))
        # title_TicTac = pygame.transform.rotate(title_TicTac, 30)

        myfont = pygame.font.SysFont("monospace", 28)

        # render text
        label = myfont.render("Red or Blue?", 1, (0, 0, 0))

        screen.blit(background, (-15, -15))
        screen.blit(title_TicTac, (60, 100))
        screen.blit(title_super, (30, 40))
        pygame.draw.rect(screen, pygame.Color(200, 200, 200), (290, 350, 220, 90))
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), (300, 400, 200, 30))
        screen.blit(textinput.get_surface(), (300, 400))
        screen.blit(label, (300, 360))

        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    pygame.init()

    pygame.display.set_caption('Super Tic Tac Toe')

    size = (WIDTH, WIDTH)
    screen = pygame.display.set_mode(size)
    user_color = starting_screen(screen).lower()

    # initializes and connects client object to server
    c = client()
    c.check_messages()

    data = [[[0,"Purple","Green","Green","Green","Green","Green","Green","Green","Green"],[0,"Green","Green","Green","Green","Green","Green","Green","Green","Green"],[0,"Purple","Green","Green","Green","Green","Green","Green","Green","Green"]],[[0,"Green","Green","Green","Green","Green","Green","Green","Green","Green"],[0,"Green","Green","Green","Green","Green","Green","Green","Green","Green"],[0,"Purple","Green","Green","Green","Green","Green","Green","Green","Green"]],[[0,"Green","Green","Green","Green","Green","Green","Green","Green","Green"],[0,"Green","Green","Green","Green","Green","Green","Green","Green","Green"],[0,"Green","Green","Green","Green","Green","Green","Green","Green","Green"]]]
    model = readin_data(data)
    view = View_Setup(model, screen)

    running = True

    user_color = input('What color are you?')
    c.send_message('u' + user_color)

    while running:
        mess = c.check_messages()
        mess = to_array(mess)
        if mess:
            print(mess)
            # paint_boxes(mess, screen)
            model = readin_data(mess)
            view = View_Setup(model, screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x is not None and y is not None:
                    send = '[' + str(x / WIDTH) + ', ' + str(y / WIDTH) + ']'
                    print(send)
                    c.send_message(str(send))
        view.draw()
        c.send_message('hb')

        time.sleep(.05)

    pygame.quit()
