from settings import *
from display import Button, Title
import sys

pg.init()
clock = pg.time.Clock()


def starting_screen(screen):
    intro = True
    title = Title(screen, 'Snake', SK, CENTER[1] - 200)
    play = Button(screen, 'Play', CENTER[0] - 250, CENTER[1] - 100, 200, 150, BLUE, LBLUE)
    bquit = Button(screen, 'Quit', CENTER[0] + 50, CENTER[1] - 100, 200, 150, RED, LRED)
    screen.fill(BG)
    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        title.display()
        if play.display():
            intro = False
        if bquit.display():
            sys.exit()
        pg.display.update()
        clock.tick(15)


def end_screen(screen):
    end = True
    title = Title(screen, 'You lose', SK, CENTER[1] - 200)
    restart = Button(screen, 'Restart', CENTER[0] - 250, CENTER[1] - 100, 200, 150, BLUE, LBLUE)
    bquit = Button(screen, 'Quit', CENTER[0] + 50, CENTER[1] - 100, 200, 150, RED, LRED)
    screen.fill(BG)
    while end:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        title.display()
        if restart.display():
            pg.time.delay(100)
            return True
        if bquit.display():
            sys.exit()
        pg.display.update()
        clock.tick(15)
