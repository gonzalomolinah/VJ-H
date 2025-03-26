import pygame


def morido():
    hola = True    
    clock = pygame.time.Clock() 
    screen = pygame.display.set_mode((1000, 700))
    while hola:
        # background_image = pygame.image.load("assets/pixelBackground.jpg").convert()
        # screen.blit(background_image, [0, 0])
        pygame.mouse.set_visible(False)


        screen_width = 1000
        screen_height = 700

        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 40)
        title = font.render('Game Over', True, (255, 255, 255))
        restart_button = font.render('R - Restart', True, (255, 255, 255))
        quit_button = font.render('Q - Quit', True, (255, 255, 255))
        screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/3))
        screen.blit(quit_button, (screen_width/2 - quit_button.get_width()/2, screen_height/2 + quit_button.get_height()/2))
        pygame.display.update()

        for event in pygame.event.get():
            # se presiono una tecla?
            if event.type == pygame.KEYDOWN:
                # era la tecla de escape? -> entonces terminamos
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    hola = False
            elif event.type == pygame.QUIT:
                    hola = False
        clock.tick(40)
    pygame.quit()   
    