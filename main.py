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
        self.opponent_movement = [False, False]


    def update_movement(self):
        self.p1.update(self.movement[1] - self.movement[0])
        self.p2.update(self.opponent_movement[1] - self.opponent_movement[0])
        
        if self.ball.collision([self.p1, self.p2]):
            self.ball.dir[0] *= -1
        elif self.ball.pos[0] < self.ball.radius or self.ball.pos[0] > self.W - self.ball.radius:
            self.goal()
        if self.ball.pos[1] <= self.ball.radius or self.ball.pos[1] >= self.H - self.ball.radius:
            self.ball.dir[1] *= -1
        self.ball.update()

        self.p1.render(self.win)
        self.p2.render(self.win)
        self.ball.render(self.win)


    def goal(self):
        if self.ball.pos[0] > self.W//2:
            self.p1.score += 1
        else:
            self.p2.score += 1
        print(f'{self.p1.score} - {self.p2.score}')
        self.ball.pos[0] = self.W//2
        self.ball.dir[0] *= -1


    def run(self):
        while True:
            self.win.fill((0,0,0))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                #p1 player left
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_s:
                        self.movement[1] = True
                    if e.key == pygame.K_w:
                        self.movement[0] = True
                #p2 player right
                    if e.key == pygame.K_DOWN:
                        self.opponent_movement[1] = True
                    if e.key == pygame.K_UP:
                        self.opponent_movement[0] = True

                    #debugging ball hard reset
                    if e.key == pygame.K_SPACE:
                        self.ball.pos = [self.W//2, self.H//2]
                        self.ball.dir[0], self.ball.dir[1] = -1, -1

                #p1 player left
                if e.type == pygame.KEYUP:
                    if e.key == pygame.K_s:
                        self.movement[1] = False
                    if e.key == pygame.K_w:
                        self.movement[0] = False
                #p2 player right
                    if e.key == pygame.K_DOWN:
                        self.opponent_movement[1] = False
                    if e.key == pygame.K_UP:
                        self.opponent_movement[0] = False
            
            self.update_movement()
            pygame.display.update()


if __name__ == '__main__':
    Game().run()
