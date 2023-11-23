import pygame
from sys import exit
from entity import *
#from math import abs

WHITE = (255,255,255)
class Game:
    def __init__(self):
        pygame.init()

        self.W, self.H = 1024, 640
        self.win = pygame.display.set_mode((self.W, self.H))

        self.p1 = Paddle(self, 0, 100, 15, WHITE)
        self.p2 = Paddle(self, 1, 100, 15, WHITE)
        self.ball = Ball(self, 10, WHITE)

        self.movement = [False, False]


    def update_movement(self):
        self.p1.update(self.movement[1] - self.movement[0])
        
        if self.ball.pos[0] <= self.ball.radius or self.ball.pos[0] >= self.W - self.ball.radius or self.collision():
            self.ball.dir[0] *= -1
        if self.ball.pos[1] <= self.ball.radius or self.ball.pos[1] >= self.H - self.ball.radius:
            self.ball.dir[1] *= -1
        self.ball.update()

        self.p1.render(self.win)
        self.p2.render(self.win)
        self.ball.render(self.win)


    def collision(self):
        if self.p1.y + self.ball.pos[1] <= self.p1.length and self.p1.x - self.ball.pos[0] <= self.p1.width + self.p1.margin:
            self.p1.color = (0,0,250)
        else:
            self.p1.color = WHITE

    def run(self):
        while True:
            self.win.fill((0,0,0))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                #client player movement
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_s or e.key == pygame.K_DOWN:
                        self.movement[1] = True
                    if e.key == pygame.K_w or e.key == pygame.K_UP:
                        self.movement[0] = True
                if e.type == pygame.KEYUP:
                    if e.key == pygame.K_s or e.key == pygame.K_DOWN:
                        self.movement[1] = False
                    if e.key == pygame.K_w or e.key == pygame.K_UP:
                        self.movement[0] = False
            
            self.update_movement()
            pygame.display.update()


if __name__ == '__main__':
    Game().run()
