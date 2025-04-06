import pygame
from scenes.inicio import start_screen
import scenes.game as GameScene


def morido(score):
    esperando = True    
    clock = pygame.time.Clock() 
    screen = pygame.display.set_mode((700, 700))

    background_image = pygame.image.load("assets/foto_gameover.png").convert()
    background_image = pygame.transform.scale(background_image, (700, 700))
    
    while esperando:
        screen.blit(background_image, [0, 0])
        pygame.mouse.set_visible(False)


        screen_width = 700
        screen_height = 700

        screen.blit(background_image, (0, 0))

        font = pygame.font.SysFont('arial', 40)
        title = font.render('Game Over', True, (255, 255, 255))
        score_text = font.render(f'Score: {round(score)}', True, (255, 255, 255))
        restart_button = font.render('R - Restart', True, (255, 255, 255))
        quit_button = font.render('Q - Quit', True, (255, 255, 255))

        screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/3-50))
        screen.blit(score_text, (screen_width/2 - score_text.get_width()/2, screen_height/2 - score_text.get_height()/3))
        screen.blit(restart_button, (screen_width/2 - restart_button.get_width()/2, screen_height/2 + restart_button.get_height()/2))
        screen.blit(quit_button, (screen_width/2 - quit_button.get_width()/2, screen_height/2 + quit_button.get_height() + 20))
        pygame.display.update()

        for event in pygame.event.get():
            # se presiono una tecla?
            if event.type == pygame.KEYDOWN:
                # era la tecla de escape? -> entonces terminamos
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    esperando = False
                elif event.key == pygame.K_r:
                    esperando = False
                    pygame.mouse.set_visible(True)
                    score = start_screen(screen, GameScene.gameLoop)
                    morido(score)
                    pygame.mouse.set_visible(False)
            elif event.type == pygame.QUIT:
                    esperando = False
        clock.tick(40)
    pygame.quit()   
    