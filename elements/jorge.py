"""
Hola este es modulo Jorge,
este modulo manejara la creacion y movimiento de Jorge
"""

if __name__ == "__main__": # Solo para que no ejecutes este archivo
    import sys
    print(
        "\033[38;2;255;0;0mESTE MODULO NO DEBE EJECUTARSE. EJECUTAR main.py\033[0m\n"
        * 3
    )
    sys.exit()

import pygame
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT, RLEACCEL)
import math

from elements.projectile import Projectile


JorgePNG = pygame.image.load('assets/JorgeVJ.png')
JorgePNG_scaled = pygame.transform.scale(JorgePNG, (80, 80))

class Player(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super(Player, self).__init__()
        self.surf = JorgePNG_scaled
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.derecha = True
        self.speed = 5  # Velocidad predeterminada
        
        # POR HACER (2.3): Crear lista de proyectiles
        self.projectiles = pygame.sprite.Group()

    def update(self, pressed_keys):
        # Usar self.speed para aplicar la velocidad del jugador
        if pressed_keys[pygame.K_w]:
            self.rect.move_ip(0, -self.speed)
        if pressed_keys[pygame.K_s]:
            self.rect.move_ip(0, self.speed)
        if pressed_keys[pygame.K_a]:
            if self.derecha:
                self.surf = pygame.transform.flip(self.surf, True, False)
                self.derecha = False
            self.rect.move_ip(-self.speed, 0)
        if pressed_keys[pygame.K_d]:
            if not self.derecha:
                self.surf = pygame.transform.flip(self.surf, True, False)
                self.derecha = True
            self.rect.move_ip(self.speed, 0)
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height
        
        # Actualizar la posición de los proyectiles
        self.projectiles.update()


    def shoot(self, mouse_pos): 
        
        # POR HACER (2.3): Crear y calcular dirección proyectil
        direction = [mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery]
        lenght = math.hypot(direction[0], direction[1])
        direction = [direction[0] / lenght, direction[1] / lenght]

        proyectile = Projectile(self.rect.center, direction, self.screen_width, self.screen_height)
        self.projectiles.add(proyectile)