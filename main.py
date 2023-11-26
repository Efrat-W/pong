import pygame
from sys import exit
from entity import *

WHITE = pygame.Color("white")
AQUA = pygame.Color("aquamarine1")
AQUA_DARK = pygame.Color("aquamarine3")

class Game:
    def __init__(self):
        pygame.init()

        self.W, self.H = 1024, 640
        self.win = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("Infinite Pong Game")

        self.clock = pygame.time.Clock()

        self.p1 = Paddle(self, 0, 100, 15, WHITE)
        self.p2 = Paddle(self, 1, 100, 15, WHITE)
        self.ball = Ball(self, 15, AQUA)

        self.movement = [False, False]
        self.opponent_movement = [False, False]

        self.bg_overlay = pygame.Surface((self.W, self.H))
        self.bg_overlay.fill((0,25,25))
        self.bg_overlay.set_alpha(200)


    def update_movement(self):
        self.p1.update(self.movement[1] - self.movement[0])
        self.p2.update(self.opponent_movement[1] - self.opponent_movement[0])
        
        self.ball.collision([self.p1, self.p2])
        self.goal()
        self.ball.update()

        self.p1.render(self.win)
        self.p2.render(self.win)
        self.ball.render(self.win)

    def draw_text(self, score1, score2):
        size = 250
        margin = 100
        font = pygame.font.SysFont("consolas", size, bold=True)
        score_L = font.render(str(score1), False, WHITE)
        score_R = font.render(str(score2), False, WHITE)
        
        x1 = self.W // 2 - int(score_L.get_width()) - margin
        x2 = self.W // 2 + margin
        y = (self.H - size) // 2
        
        self.win.blit(score_L, (x1, y))
        self.win.blit(score_R, (x2, y))

    def goal(self):
        if self.ball.pos[0] < self.ball.radius or self.ball.pos[0] > self.W - self.ball.radius:
            if self.ball.pos[0] > self.W//2:
                self.p1.score += 1
            else:
                self.p2.score += 1
            print(f'{self.p1.score} - {self.p2.score}')
            self.ball.pos[0] = self.W//2
            self.ball.dir[0] *= -1
            self.ball.vel = 3 + 0.1 * max(self.p1.score, self.p1.score)



    def run(self):
        while True:
            self.win.fill((0,0,0))
            self.draw_text(self.p1.score, self.p2.score)
            self.win.blit(self.bg_overlay, (0,0))
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
            self.clock.tick(120)


if __name__ == '__main__':
    Game().run()
