import pygame

controls = {
    'wasd' : {'up' : pygame.K_w, 'down' : pygame.K_s},
    'arrows' : {'up': pygame.K_UP, 'down' : pygame.K_DOWN},
}

class Client:
    def __init__(self, control_choice):
        pygame.init()
        self.movement = [False, False]
        self.controls = controls[control_choice]

    def move(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()

            if e.type == pygame.KEYDOWN:
                if e.key == self.controls['down']:
                    self.movement[1] = True
                if e.key == self.controls['up']:
                    self.movement[0] = True
            
            if e.type == pygame.KEYUP:
                if e.key == self.controls['down']:
                    self.movement[1] = False
                if e.key == self.controls['up']:
                    self.movement[0] = False

        return self.movement