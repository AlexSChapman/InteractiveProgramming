"""
    Client Script for Super Tic Tac tic_tac_toe
    @Author Alex Chapman
    3/6/17
"""

from com_client import client
import pygame
import sys
import time
import ast

# initialize colors to be used
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# non-magic number size implementation
width = 500

pygame.init()
screen = pygame.display.set_mode((width, width))

# initializes and connects client object to server
c = client()
c.check_messages()


def check_mouse():
    """
    Finds and gets all mouse clicked positions in the scope of the pygame
    window.
    """
    events = pygame.event.get()
    for event in events:
        # if x clicked
        if event.type == pygame.QUIT:
            sys.exit()
        # if mousebutton pressed, return mouse position
        if event.type == pygame.MOUSEBUTTONDOWN:
            return pygame.mouse.get_pos()


def draw():
    """Placeholder for later draw"""
    screen.fill((255, 255, 255))
    pygame.draw.lines(screen, BLUE, False, [[0, width / 3],
                                            [width, width/3],
                                            [0, 2/3 * width],
                                            [width, 2/3 * width],
                                            [width / 3, 0],
                                            [width / 3, width],
                                            [2/3 * width, 0],
                                            [2/3 * width, width]], 5)

    for i in range(0, 3):
        pygame.draw.lines(screen, RED, False, [[0, width / 9+i*width/3],
                                               [width, width/9+i*width/3],
                                               [0, 2/9 * width+i*width/3],
                                               [width, 2/9*width+i*width/3],
                                               [width / 9 + i * width / 3, 0],
                                               [width / 9 + i*width/3, width],
                                               [2/9 * width + i * width/3, 0],
                                               [2/9*width+i*width/3, width]],
                          5)

    pygame.display.flip()


def print_messages(thruput):
    """Placeholder method for determining functionality of game"""
    thruput = thruput[:int(len(thruput)/2)]
    lines = ['-----', '-----', '-----', '|', '-----', '-----', '-----', '|', '-----', '-----', '-----']
    try:
        ls = ast.literal_eval(thruput)
        board = []
        for ROW in ls:
            rows = []
            for row in range(0, 3):
                for ITEM in ROW:
                    for i in range(0, 3):
                        rows.append(ITEM[i + row * 3 + 1])
                    rows.append('|')
            print(rows)
            print(lines)
            # board.append(rows)
            # board.append(lines)
        print('*******************************')
        print()
        print(board)
    except (SyntaxError, ValueError) as e:
        print(e)
        # print(thruput)


first = True
while(1):
    if first:
        color = input('What color are you?')
        c.send_message('u' + color)
        first = False
    draw()
    print_messages(c.check_messages())
    temp = check_mouse()
    if temp is not None:
        send = '[' + str(temp[0] / width) + ', ' + str(temp[1] / width) + ']'
        print(send)
        c.send_message(str(send))
    c.send_message('hb')
    time.sleep(.05)
