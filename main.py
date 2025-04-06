"""
Hola este es modulo principal,
el codigo que al ejecutar pondra en marchas nuestro juego
"""
import pygame
import scenes.game as GameScene
import scenes.death as dt
from scenes.inicio import start_screen  # Importamos la pantalla de inicio

# Inicializamos pygame
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()
# Configuramos la pantalla
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Mostramos la pantalla de inicio antes de iniciar el juego
score = start_screen(screen, GameScene.gameLoop)

# Si el juego termina, mostramos la pantalla de muerte
dt.morido(score)