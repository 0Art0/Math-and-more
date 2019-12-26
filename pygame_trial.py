import pygame

#Reading events - keystrokes and escape
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT, )

#initialize pygame
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys, d=5):
        dist = {K_UP: (0, 5), K_DOWN : (0, -5), K_LEFT : (-5, 0), K_RIGHT : (5, 0)}

        for key in pressed_keys:
            if pressed_keys[key]:
                self.rect.move_ip(*dist[key])

#screen dimensions
sw, sh = 800, 600
screen = pygame.display.set_mode((sw, sh))

#screen and surface background
screen.fill((0, 0, 0))

player = Player()

#display surface
screen.blit(player.surf, (sw/3, sh/3))
pygame.display.flip()

#main loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False

    pressed_keys = pygame.key.get_pressed()

    print(pressed_keys)
    
    player.update(pressed_keys)
