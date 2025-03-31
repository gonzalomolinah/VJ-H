'''
Hola este es modulo game,
este modulo manejara la escena donde ocurre nuestro juego
'''

if __name__ == "__main__": # Solo para que no ejecutes este archivo
    import sys
    print(
        "\033[38;2;255;0;0mESTE MODULO NO DEBE EJECUTARSE. EJECUTAR main.py\033[0m\n"
        * 3
    )
    sys.exit()

import pygame

from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT,K_m)

from elements.jorge import Player

from elements.bug import Enemy

import time

from scenes.pause import pause_screen

#from scenes.start import start_menu

def gameLoop():
    ''' iniciamos los modulos de pygame'''

    pygame.init()

    ''' Creamos y editamos la ventana de pygame (escena) '''
    ''' 1.-definir el tamaño de la ventana'''
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 700

    ''' 2.- crear el objeto pantalla'''
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image = pygame.image.load("assets/pixelBackground.jpg").convert()

    cursor_img = pygame.image.load("assets/crosshair.png")
    cursor_img = pygame.transform.scale(cursor_img, (50, 50))
    pygame.mouse.set_visible(False)
    cursor_img_rect = cursor_img.get_rect()

    #mostrar mmenu de inicio
    ''' Preparamos el gameloop '''
    ''' 1.- creamos el reloj del juego'''

    clock = pygame.time.Clock()
    ''' 2.- generador de enemigos'''

    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 600)

    ''' 3.- creamos la instancia de jugador'''
    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

    ''' 4.- contenedores de enemigos y jugador'''
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    ''' hora de hacer el gameloop '''
    # variable booleana para manejar el loop
    running = True

    lastShoot = time.time()
    # loop principal del juego

    score = 0

    while running:

        screen.blit(background_image, [0, 0])

        
        cursor_img_rect.center = pygame.mouse.get_pos()  # update position 
        screen.blit(cursor_img, cursor_img_rect) # draw the cursor

        score_font = pygame.font.SysFont('arial', 20)
        score_text = score_font.render(f'Score: {round(score)}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        
        # POR HACER (2.5): Pintar proyectiles en pantalla
        for projectile in player.projectiles:
            screen.blit(projectile.surf, projectile.rect)
        
        # POR HACER (2.5): Eliminar bug si colisiona con proyectil
        collisions = pygame.sprite.groupcollide(player.projectiles, enemies, True, True)
        score += 5 * len(collisions)
        pygame.sprite.groupcollide(player.projectiles, enemies, True, True)
        
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        enemies.update()
        
        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            running = False
        

        pygame.display.flip()
        
        # iteramos sobre cada evento en la cola
        for event in pygame.event.get():
            # se presiono una tecla?
            if event.type == KEYDOWN:
                # era la tecla de escape? -> entonces terminamos
                if event.key == K_m:
                    pygame.mouse.set_visible(True)
                    pause_screen(screen)
                    pygame.mouse.set_visible(False)

            # fue un click al cierre de la ventana? -> entonces terminamos
            elif event.type == QUIT:
                running = False
            
            elif event.type == ADDENEMY:
                new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            
            # POR HACER (2.4): Agregar evento disparo proyectil
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if time.time() - lastShoot > 1:
                    player.shoot(pygame.mouse.get_pos())
                    lastShoot = time.time()
        

        score += 0.1
        clock.tick(40)