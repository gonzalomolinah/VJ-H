import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN

def start_screen(screen, gameLoop):

    """
    Muestra la pantalla de inicio y permite iniciar el juego o salir.
    """

    # Cargar imagen de fondo
    background_image = pygame.image.load("assets/foto_inicio.png").convert()
    background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))
    
    # Fuente y textos
    small_font = pygame.font.Font(None, 50)
    start_text = small_font.render("Iniciar Juego", True, (0, 0, 0))
    exit_text = small_font.render("Salir", True, (0, 0, 0))

    # Posición de los botones
    spacing = 150  
    base_y = 500  

    start_rect = start_text.get_rect(center=(screen.get_width() // 2 - spacing, base_y))
    exit_rect = exit_text.get_rect(center=(screen.get_width() // 2 + spacing, base_y))
    
    running = True
    pygame.mouse.set_visible(True)
    pygame.mixer.music.load("assets/menu_music.wav")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
    while running:
        screen.blit(background_image, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        
        start_color = (200, 200, 200) if start_rect.collidepoint(mouse_pos) else (255, 255, 255)
        exit_color = (200, 200, 200) if exit_rect.collidepoint(mouse_pos) else (255, 255, 255)
        pygame.draw.rect(screen, (50, 50, 50), start_rect, border_radius=10)
        pygame.draw.rect(screen, (50, 50, 50), exit_rect, border_radius=10)
        # Renderizar los textos con color según el mouse
        start_text = small_font.render("Iniciar Juego", True, start_color)
        exit_text = small_font.render("Salir", True, exit_color)

        # Dibujar textos en pantalla
        screen.blit(start_text, start_rect)
        screen.blit(exit_text, exit_rect)

        pygame.display.flip()  # Actualizar pantalla
        
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    running = False
                    pygame.mouse.set_visible(False)
                    pygame.mixer.music.stop()
                    gameLoop()  # Llamar a la función que inicia el juego
                elif exit_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()
