import os, sys
from random import randint, choice
from math import sin, cos, radians

import pygame
from pygame import Rect, Color
from pygame.sprite import Sprite

from vec2d import vec2d

class Creep(pygame.sprite.Sprite): #the enemies that bounce background
    def __init__(self,screen,img_filename,init_position,init_direction,speed):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.speed = speed
        self.base_image_0 = creep_filenames[0]
        self.base_image_45 = creep_filenames[1]

        self.pos = vec2d(init_position)
        self.prev_pos = vec2d(self.pos)
        self.direction = vec2d(init_direction).normalized()

    def blitme(self): #placing the creep image
        self.image = pygame.image.load("greencreep_0.png")
        draw_pos = self.image.get_rect().move(self.pos.x - self.image.get_width() / 2, self.pos.y - self.image.get_height() / 2)
        self.screen.blit(self.image, draw_pos)
        creeps.append(Creep(screen, choice(creep_filenames), (randint(0, screen_width), randint(0, screen_height)), (choice([-1, 1]), choice ([-1, 1])), 0.1))



screen_width, screen_height = (400, 400)
bg_color = (150, 150, 80)
creep_filenames = [
'bluecreep.png',
'pinkcreep.png',
'graycreep.png'
]
n_creeps = 20

pygame.init()
screen = pygame.display.set_mode(
(screen_width, screen_height), 0, 32)
clock = pygame.time.Clock()

creeps = []
for i in range(n_creeps):
    creeps.append(Creep(screen, choice(creep_filenames), (randint(0, screen_width), randint(0, screen_height)), (choice ([-1, 1]), choice([-1, 1])), 0.1))

def update(self,time_passed):
    self._change_direction(time_passed)
    self.image = pygame.transform.rotate(self.base_image, -self.direction.angle)
    displacement = vec2d(
        self.self.direction.x * self.speed * time_passed,
        self.direction.y * self.speed * time_passed)
    self.pos += displacement

    self.image_w, self.image_h = self.image.get_size()
    bounds.rect = self.screen.get_rect().inflate(-self.image_w, -self.image_h)

    if self.pos.x < bounds_rect.left:
        self.pos.x = bounds_rect.left
        self.direction.x *= -1
    elif self.pos.x > bounds_rect.right:
        self.pos.x = bounds_rect.right
        self.direction.x *= -1
    elif self.pos.y < bounds_rect.top:
        self.pos.y = bounds_rect.top
        self.direction.y *= -1
    elif self.pos.y > bounds_rect.bottom:
        self.pos.y = bounds_rect.bottom
        self.direction.y *= -1

while True:
    time_passed = clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()
    screen.fill(bg_color)
    for creep in creeps:
        creep.update(time_passed)
        creep.blitme()

    pygame.display.flip() #updates display

if __name__ == "__main__":
    game = Game()
    game.run()
