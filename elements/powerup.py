import pygame
import random

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.type = random.choice(['speed','shield'])
        self.image = pygame.image.load(f'assets/powerup_{self.type}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 60))
        self.surf = self.image
        self.rect = self.image.get_rect(
            center=(random.randint(50, screen_width - 50), random.randint(50, screen_height - 50))
        )
    def update(self):
        pass  # Puedes animarlo si quieres
