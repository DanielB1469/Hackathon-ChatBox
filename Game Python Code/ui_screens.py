import pygame
import math
from settings import WHITE, BLACK

# ✅ Load separate background images for different screens
start_screen_image = pygame.image.load("Startingscreen.webp")  
start_screen_image = pygame.transform.scale(start_screen_image, (1200, 600))  

select_screen_image = pygame.image.load("BoxingRing.png")  
select_screen_image = pygame.transform.scale(select_screen_image, (1200, 600))

def draw_start_screen(screen, font):
    """Draws the start screen with a unique background and fading text"""
    screen.blit(start_screen_image, (0, 0))  # ✅ Start screen background



    # ✅ Calculate alpha (transparency) value using a sine wave
    time_passed = pygame.time.get_ticks() / 1000  # Get time in seconds
    alpha = int((math.sin(time_passed * 2) + 1) / 2 * 255)  # Oscillates between 0 and 255

    # Create the "Press ENTER" text surface with alpha (fading effect)
    prompt = font.render("Press ENTER to Start", True, WHITE)
    prompt_surface = prompt.convert_alpha()
    prompt_surface.set_alpha(alpha)  # Apply fading effect

    screen.blit(prompt_surface, (450, 500))  # Draw fading text

    pygame.display.flip()

def draw_select_screen(screen, font, enemies, selected_index):
    """Draws the enemy selection screen with a different background"""
    screen.blit(select_screen_image, (0, 0))  # ✅ Background for selection

    title = font.render("Select Your Opponent", True, WHITE)
    screen.blit(title, (250, 150))

    for i, enemy in enumerate(enemies):
        color = WHITE if i == selected_index else (150, 150, 150)
        text = font.render(enemy, True, color)
        screen.blit(text, (350, 250 + i * 50))
    
    pygame.display.flip()

def draw_pause_screen(screen, font):
    """Draws the pause screen"""
    screen.fill(BLACK)
    text = font.render("Game Paused - Press P to Resume", True, WHITE)
    screen.blit(text, (200, 300))
    pygame.display.flip()
