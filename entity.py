import pygame

class Paddle:
    def __init__(self, game, side, length, width, color):
        self.game = game
        self.length = length
        self.width = width
        self.color = color
        self.margin = 20
        self.x = game.W - self.width - self.margin if side else self.margin
        #pos
        self.y = game.H // 2 - self.length // 2
        self.vel = 0.7
        self.score = 0

    def update(self, pos=0):
        temp_y = self.y + pos * self.vel
        if self.vel * 2 < temp_y < self.game.H - self.vel * 2 - self.length:
            self.y = temp_y

    def render(self, surface):
        pygame.draw.rect(surface, self.color, [self.x, self.y, self.width, self.length])


class Ball:
    def __init__(self, game, radius, color):
        self.radius = radius
        self.color = color
        self.pos = [game.W // 2, game.H // 2]
        self.vel = 0.5
        self.acc = 0
        self.dir = [1,1]

    def collision(self, paddles):
        bounding_box = [self.pos[0] - self.radius, self.pos[1] - self.radius, self.radius * 2, self.radius * 2]
        for i, paddle in enumerate(paddles):
            if pygame.Rect(paddle.x, paddle.y, paddle.width, paddle.length).colliderect(bounding_box):
                self.pos[0] = paddle.x - self.radius - 1 if i else paddle.x + paddle.width + self.radius + 1
                self.acc = 0
                return True

    def update(self):
        self.pos[0] += self.dir[0] * self.vel
        self.pos[1] += self.dir[1] * (self.vel + self.acc)

    def render(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)