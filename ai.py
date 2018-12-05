from settings import *
import random as rand


class AI:

    def __init__(self, screen, snake, food):
        self.screen = screen
        self.snake = snake
        self.food = food

        self.direction = self.snake.direction
        self.hx = self.snake.head.x
        self.hy = self.snake.head.y
        self.fx = self.food.x
        self.fy = self.food.y
        self.bodies = self.snake.bodies

    def get_pos(self):
        self.direction = self.snake.direction
        self.bodies = self.snake.bodies
        self.hx = self.snake.head.x
        self.hy = self.snake.head.y
        self.fx = self.food.x
        self.fy = self.food.y

    def greater_change(self):
        self.get_pos()
        if abs(self.fx - self.hx) > abs(self.fy - self.hy):
            return 'x'
        elif abs(self.fx - self.hx) < abs(self.fy - self.hy):
            return 'y'
        elif abs(self.fx - self.hx) == abs(self.fy - self.hy):
            return 0

    def pos_change(self, var):

        def checkx():
            if self.fx - self.hx > 0:
                return 1, 0
            else:
                return -1, 0

        def checky():
            if self.fy - self.hy > 0:
                return 0, 1
            else:
                return 0, -1

        self.get_pos()
        if var == 'x':
            x, y = checkx()
            if self.check_dir(x, y) == 1:
                x, y = checky()
            return x, y
        else:
            x, y = checky()
            if self.check_dir(x, y) == 1:
                x, y = checkx()
            return x, y

    def check_dir(self, x, y):
        if self.direction != [x, y]:
            if x != 0:
                if self.direction != [-x, y]:
                    return False
                else:
                    return 1
            elif y != 0:
                if self.direction != [x, -y]:
                    return False
                else:
                    return 1
        else:
            return True

    def change_dir(self, x, y):
        self.snake.direction = [x, y]

    def check_space(self, x, y, near=True):
        if near:
            if x == -1 or x == GWIDTH or y == -1 or y == GHEIGHT:
                return True
        else:
            pass
        for body in self.bodies:
            if body.x == x and body.y == y:
                return True
            else:
                continue
        return False

    def flip(self):
        flip = rand.randint(0, 1)
        return flip

    def move(self):
        self.get_pos()
        if self.greater_change() == 0:
            if self.flip() == 0:
                x, y = self.pos_change('x')
                if self.check_space(self.hx + x, self.hy + y) is False:
                    if self.check_space(self.hx + (x * 2), self.hy + (y * 2), near=False) is False:
                        self.change_dir(x, y)
                else:
                    pass
            else:
                x, y = self.pos_change('y')
                if self.check_space(self.hx + x, self.hy + y) is False:
                    if self.check_space(self.hx + (x * 2), self.hy + (y * 2), near=False) is False:
                        self.change_dir(x, y)
        else:
            x, y = self.pos_change(self.greater_change())
            if self.check_space(self.hx + x, self.hy + y) is False:
                if self.check_space(self.hx + (x * 2), self.hy + (y * 2), near=False) is False:
                    self.change_dir(x, y)
            else:
                pass
