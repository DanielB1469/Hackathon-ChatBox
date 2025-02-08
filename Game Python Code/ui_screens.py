import pygame
from settings import WHITE, BLACK

# ✅ Load the start screen image
start_screen_image = pygame.image.load("StartingScreen.webp")  
start_screen_image = pygame.transform.scale(start_screen_image, (800, 600))  # Adjust to match window size

def draw_start_screen(screen, font):
    """Draws the start screen with an image background"""
    screen.blit(start_screen_image, (0, 0))  # ✅ Display the background image



    pygame.display.flip()


def draw_select_screen(screen, font, enemies, selected_index):
    screen.fill(BLACK)
    title = font.render("Select Your Opponent", True, WHITE)
    screen.blit(title, (250, 150))

    for i, enemy in enumerate(enemies):
        color = WHITE if i == selected_index else (150, 150, 150)
        text = font.render(enemy, True, color)
        screen.blit(text, (350, 250 + i * 50))
    
    pygame.display.flip()

def draw_pause_screen(screen, font):
    screen.fill(BLACK)
    text = font.render("Game Paused - Press P to Resume", True, WHITE)
    screen.blit(text, (200, 300))
    pygame.display.flip()
