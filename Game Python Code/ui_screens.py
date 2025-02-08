import pygame
from settings import WHITE, BLACK, STATE_START, STATE_SELECT, STATE_PAUSED, STATE_PLAYING

def draw_start_screen(screen, font):
    screen.fill(BLACK)
    title = font.render("AI Boxing Game", True, WHITE)
    prompt = font.render("Press ENTER to Start", True, WHITE)
    screen.blit(title, (300, 200))
    screen.blit(prompt, (270, 300))
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
