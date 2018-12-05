import pygame as pg

# Game variables
GAME_NAME = 'Snake'
VERSION = ' Test'
TITLE = GAME_NAME + VERSION
WIDTH = 800
HEIGHT = 600
PIXEL_WIDTH = 25
GWIDTH = WIDTH / PIXEL_WIDTH
GHEIGHT = HEIGHT / PIXEL_WIDTH
SIZE = (WIDTH, HEIGHT)
CENTER = (WIDTH / 2, HEIGHT / 2)
FPS = 60
DEBUG = True

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (25, 25, 25)
LGRAY = (40, 40, 40)
RED = (230, 0, 0)
LRED = (255, 0, 0)
GREEN = (0, 230, 0)
LGREEN = (0, 255, 0)
BLUE = (0, 0, 230)
LBLUE = (0, 0, 255)

# Custom variables
MODE = "ai"
SPEED = 70
ADDITIVE = 10
BG = WHITE
if BG == BLACK:
    SK = WHITE
else:
    SK = BLACK
FOOD_COLOR = RED

# Keys
RIGHT = pg.K_RIGHT
LEFT = pg.K_LEFT
UP = pg.K_UP
DOWN = pg.K_DOWN
SPACE = pg.K_SPACE
Q = pg.K_q
W = pg.K_w
A = pg.K_a
E = pg.K_e


def cg_color(ic, ac):
    global FOOD_COLOR, FOOD_LCOLOR
    FOOD_COLOR = ic
    FOOD_LCOLOR = ac


def convert2rez(x, y):
    rezx = x * PIXEL_WIDTH
    rezy = y * PIXEL_WIDTH
    return rezx, rezy

