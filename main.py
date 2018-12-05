from settings import *
from snake import Snake
from food import Food
from screens import starting_screen, end_screen
from display import Title, Score
from ai import AI
import sys


class Game:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(SIZE)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.snake = Snake(self.screen)
        self.food = Food(self.screen, self.snake)
        self.start = Title(self.screen, 'Press space to start', SK, CENTER[1] - 200)
        self.score = Score(self.screen, 0)
        self.speed = SPEED
        self.ai = None
        self.score_timer = 0

    def new(self):
        starting_screen(self.screen)
        self.run()
        if MODE == 'ai':
            pg.time.delay(10000)
        if end_screen(self.screen):
            self.new()

    def run(self):
        self.playing = True
        self.snake.create_snake()
        if MODE == 'ai':
            self.ai = AI(self.screen, self.snake, self.food)
        self.screen.fill(BG)
        self.start.display()
        space = False
        while space is False:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == SPACE:
                        space = True
            pg.display.update()
        while self.playing:
            self.clock.tick(FPS)
            pg.time.delay(self.speed)
            self.events()
            if MODE == 'ai':
                self.ai_update()
            self.updates()
            self.draw()

    def events(self):
        if MODE == 'play':
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == Q:
                        self.snake.print_snake()
                    elif event.key == W:
                        self.snake.shift()
                    elif event.key == E:
                        self.snake.add_length(2)
                    elif event.key == UP:
                        self.snake.change_direction(0, -1)
                    elif event.key == RIGHT:
                        self.snake.change_direction(1, 0)
                    elif event.key == DOWN:
                        self.snake.change_direction(0, 1)
                    elif event.key == LEFT:
                        self.snake.change_direction(-1, 0)
        else:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == Q:
                        self.snake.print_snake()

    def ai_update(self):
        self.ai.move()

    def updates(self):
        self.snake.shift()
        if self.food.check_eaten(self.snake):
            self.snake.add_length(ADDITIVE)
            self.food.new_food()
            self.score.update(score=10)
            if MODE == 'speed':
                self.speed -= 5
        if self.snake.check_crash():
            self.playing = False
            self.running = False
        if self.snake.head.x == 0 and self.snake.head.y == 0:
            self.score.update(color=BG)
            self.score_timer = self.snake.length
        elif self.score_timer > 0:
            self.score.update(color=BG)
            self.score_timer -= 1
        else:
            self.score.update(color=SK)

    def draw(self):
        self.snake.display()
        self.food.display()
        self.score.display()
        pg.display.update()


g = Game()
while g.running:
    g.new()

pg.quit()
