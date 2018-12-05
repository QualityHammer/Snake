from settings import *
import random as rand


class AI:

    def __init__(self, screen, snake, food):
        self.screen = screen
        self.snake = snake
        self.food = food
        self.path = Path(self.snake, self.food)

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

    @staticmethod
    def flip():
        flip = rand.randint(0, 1)
        return flip

    def move(self):
        self.get_pos()


class Path:

    # 0 = empty
    # 1 = Head
    # 2 = Body
    # 3 = Food
    def __init__(self, snake, food):
        self.snake = snake
        self.food = food
        self.grid = []

        self.create_grid()

    def create_path(self):
        hx = self.snake.head.x
        hy = self.snake.head.y
        fx = self.food.x
        fy = self.food.y
        chx = fx - hx
        chy = fy - hy
        abschx = abs(fx - hx)
        abschy = abs(fy - hy)

        if chx > 0:
            if chy > 0:
                # Bottom Right
                pass
            elif chy < 0:
                # Top Right
                pass
            else:
                # Straight Right
                pass
        elif chx < 0:
            if chy > 0:
                # Bottom Left
                pass
            elif chy < 0:
                # Top Left
                pass
            else:
                # Straight Left
                pass
        else:
            if chy > 0:
                # Straight Down
                pass
            elif chy < 0:
                # Straight Up
                pass

    def check_pos(self, x, y):
        return self.grid[y][x]

    def create_grid(self):
        for y in GHEIGHT:
            row = []
            for x in GWIDTH:
                if self.check_headpos(x, y):
                    row.append(1)
                elif self.check_bodypos(x, y):
                    row.append(2)
                elif self.check_foodpos(x, y):
                    row.append(3)
                else:
                    row.append(0)
            self.grid.append(row)

    def check_foodpos(self, x, y):
        if self.food.x == x and self.food.y == y:
            return True
        else:
            return False

    def check_bodypos(self, x, y):
        for body in self.snake.bodies:
            if body.x == x and body.y == y:
                return True
            else:
                continue
        return False

    def check_headpos(self, x, y):
        if self.snake.head is None:
            return False
        elif self.snake.head.x == x and self.snake.head == y:
            return True
        else:
            return False
