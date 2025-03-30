import pygame
from pygame.locals import (K_m, K_ESCAPE, QUIT)

def pause_screen(screen):
    """
    Muestra el menú de pausa y maneja la lógica de reanudar o salir del juego.
    """
    pygame.mouse.set_visible(True)
    pygame.display.flip()
    background_image = pygame.image.load("assets/foto_pause.png").convert()
    background_image = pygame.transform.scale(background_image,(screen.get_width(),screen.get_height()))
    small_font = pygame.font.Font(None, 50)
    resume_text = small_font.render("Volver al juego", True, (0, 0, 0))
    exit_text = small_font.render("Salir del juego", True, (0, 0, 0))
    
    spacing = 150
    base_y = 500
    resume_rect = resume_text.get_rect(center=(screen.get_width()//2 - spacing, base_y))
    exit_rect = exit_text.get_rect(center=(screen.get_width()//2 + spacing, base_y))
    
    running = True
    while running:
        screen.blit(background_image, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        resume_color = (200, 200, 200) if resume_rect.collidepoint(mouse_pos) else (255, 255, 255)
        exit_color = (200, 200, 200) if exit_rect.collidepoint(mouse_pos) else (255, 255, 255)

        # Draw buttons with some color change when the mouse is over them
        pygame.draw.rect(screen, (50, 50, 50), resume_rect, border_radius=10)
        pygame.draw.rect(screen, (50, 50, 50), exit_rect, border_radius=10)

        # Redraw the text with the appropriate color
        resume_text = small_font.render("Volver al juego", True, resume_color)
        exit_text = small_font.render("Salir del juego", True, exit_color)

        screen.blit(resume_text, resume_rect)
        screen.blit(exit_text, exit_rect)

        pygame.display.flip()  # Update the screen
        
        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if resume_rect.collidepoint(event.pos):
                    running = False  # Resume the game
                    pygame.mouse.set_visible(False)
                elif exit_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()