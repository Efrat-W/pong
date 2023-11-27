import pygame
from random import randint


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
        self.vel = 5
        self.score = 0

    def update(self, pos=0):
        temp_y = self.y + pos * self.vel
        if self.vel * 2 < temp_y < self.game.H - self.vel * 2 - self.length:
            self.y = temp_y


    def render(self, surface):
        pygame.draw.circle(surface, self.color, (self.x + self.width // 2, self.y), self.width // 2)
        pygame.draw.rect(surface, self.color, [self.x, self.y, self.width, self.length])
        pygame.draw.circle(surface, self.color, (self.x + self.width // 2, self.y + self.length), self.width // 2)



class Ball:
    def __init__(self, game, radius, color):
        self.radius = radius
        self.color = color
        self.pos = [game.W // 2, game.H // 2]
        self.vel = 3
        self.dir = [1,1]
        self.game = game

        self.trail = []


    def collision(self, paddles):
        bounding_box = [self.pos[0] - self.radius, self.pos[1] - self.radius, self.radius * 2, self.radius * 2]
        
        for i, paddle in enumerate(paddles):
            if pygame.Rect(paddle.x, paddle.y, paddle.width, paddle.length).colliderect(bounding_box):
                self.dir[0] *= -1
                self.pos[0] = paddle.x - self.radius - 1 if i else paddle.x + paddle.width + self.radius + 1
                self.vel += 0.01
                return True
        
        if bounding_box[1] <= 0 or bounding_box[1] >= self.game.H - self.radius:
            self.dir[1] *= -1
            return True
                

    def update(self):
        self.trail.append(Particle(self.pos[0], self.pos[1], self.radius * 2, pygame.Color("cadetblue")))
        for particle in self.trail:
            particle.update()
            if particle.radius <= 0:
                self.trail.remove(particle)

        self.pos[0] += self.dir[0] * self.vel
        self.pos[1] += self.dir[1] * self.vel

    def glow(self):
        radius = self.radius * 2
        surface = pygame.Surface((radius*2, radius*2))
        pygame.draw.circle(surface, pygame.Color("aquamarine3"), (radius, radius), radius)
        surface.set_colorkey((0,0,0))
        surface.set_alpha(50)
        return surface, (int(self.pos[0] - radius), int(self.pos[1] - radius))

    def render(self, surface):
        for particle in self.trail:
            particle.render(surface)
        #pygame.draw.circle(surface, pygame.Color("cadetblue3"), self.pos, self.radius + 2)
        pygame.draw.circle(surface, self.color, self.pos, self.radius)


class Particle:
    def __init__(self, x, y, size, color) -> None:
        offset_x = randint(-5, 5)
        offset_y = randint(-5, 5)
        self.pos = [x + offset_x, y + offset_y]
        self.radius = randint(size//4,size//2 + size//3)
        #self.timer = self.radius
        self.color = color

    def update(self):
        #self.timer -= 1
        self.radius -= 1

    def render(self, surface):
        radius = self.radius
        part_surface = pygame.Surface((radius*2, radius*2))
        pygame.draw.circle(part_surface, self.color, (radius, radius), radius)
        part_surface.set_colorkey((0,0,0))
        part_surface.set_alpha(20 * self.radius)
        surface.blit(part_surface, (int(self.pos[0] - radius), int(self.pos[1] - radius)))
        #pygame.draw.circle(surface, self.color, self.pos, self.radius)
