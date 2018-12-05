from settings import *


class Snake:

    def __init__(self, screen, starting_length=3):
        self.screen = screen
        self.length = starting_length
        self.head = None
        self.bodies = []
        self.direction = [1, 0]
        self.crashed = False

    def create_snake(self):
        self.head = Head(6, 6, self.direction)
        self.bodies = []
        self.bodies.append(Body(self.head))
        for body in range(2, self.length):
            self.bodies.append(Body(self.bodies[len(self.bodies) - 1]))

    def display(self):
        self.screen.fill(BG)
        rezx, rezy = convert2rez(self.head.x, self.head.y)
        pg.draw.rect(self.screen, SK, (rezx, rezy, PIXEL_WIDTH - 4, PIXEL_WIDTH - 4))
        for body in self.bodies:
            rezx, rezy = convert2rez(body.x, body.y)
            pg.draw.rect(self.screen, SK, (rezx, rezy, PIXEL_WIDTH - 4, PIXEL_WIDTH - 4))

    def shift(self):
        if len(self.bodies) + 1 < self.length:
            self.bodies.append(Body(self.bodies[len(self.bodies) - 1]))
        for body in reversed(self.bodies):
            body.x = body.leader.x
            body.y = body.leader.y
        self.head.x += self.direction[0]
        self.head.y += self.direction[1]

    def check_crash(self):
        if self.head.x == -1 or self.head.x == GWIDTH or self.head.y == -1 or self.head.y == GHEIGHT:
            return True
        for body in self.bodies:
            if self.head.x == body.x and self.head.y == body.y:
                return True
        return False

    def add_length(self, add):
        self.length += add

    def change_direction(self, x, y):
        if self.direction[0] == -x or self.direction[1] == -y:
            pass
        else:
            self.direction = [x, y]

    def print_snake(self):
        print()
        print('Head:', self.head.x, self.head.y)
        bodies = 0
        for body in self.bodies:
            print('Body' + str(bodies) + ':', body.x, body.y)
            bodies += 1
        print()


class Head:

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction


class Body:

    def __init__(self, leader):
        self.leader = leader
        self.direction = leader.direction
        self.x = leader.x - self.direction[0]
        self.y = leader.y - self.direction[1]
