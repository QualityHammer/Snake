from settings import *
import random as rand


class Food:

    def __init__(self, screen, snake):
        self.screen = screen
        self.snake = snake
        self.x = 0
        self.y = 0
        self.new_food()

    def new_food(self):
        self.x = rand.randint(0, GWIDTH - 1)
        self.y = rand.randint(0, GHEIGHT - 1)
        if self.check_unique() is False:
            self.new_food()

    def check_unique(self):
        try:
            if self.x == self.snake.head.x and self.y == self.snake.head.y:
                return False
            for body in self.snake.bodies:
                if body.x == self.x and body.y == self.y:
                    return False
            return True
        except AttributeError:
            pass

    def display(self):
        rezx, rezy = convert2rez(self.x, self.y)
        pg.draw.rect(self.screen, FOOD_COLOR, (rezx, rezy, PIXEL_WIDTH - 4, PIXEL_WIDTH - 4))

    def check_eaten(self, snake):
        if snake.head.x == self.x and snake.head.y == self.y:
            return True
        else:
            return False
