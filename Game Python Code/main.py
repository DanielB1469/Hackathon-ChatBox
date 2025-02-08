import pygame
from settings import *
from player import Player
from ui_screens import draw_start_screen, draw_select_screen, draw_pause_screen
from assets import enemy_sprites

# Initialize pygame
pygame.init()

# Constants
CHAR_SIZE = 32  # Character size (assumed to be 32x32)
SCALE = 4  # Scaling factor for visibility
WIN_WIDTH = CHAR_SIZE * 20  # 20 tiles wide
WIN_HEIGHT = CHAR_SIZE * 15  # 15 tiles high
FLOOR_HEIGHT = WIN_HEIGHT - CHAR_SIZE * 4  # Floor Y position

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

# Physics
GRAVITY = 0.8
JUMP_FORCE = -12
SPEED = 5
ANIMATION_SPEED = 10  # Adjust walking animation speed
PUNCH_ANIMATION_SPEED = 8  # Speed of punch animation
PUNCH_DURATION = 16  # How long the punch lasts

# Setup the window
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("AI Boxing Game")

# Game state
game_state = STATE_START

# Load font
font = pygame.font.Font(None, 40)

# Enemy Selection Variables
enemy_names = list(enemy_sprites.keys())
selected_enemy_index = 0
can_navigate = True  # Prevent holding navigation keys in menus

# Create player
player = Player(100, FLOOR_HEIGHT)

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(GRAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # **MENU NAVIGATION (KEYDOWN ONLY)**
        if game_state == STATE_START:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  
                game_state = STATE_SELECT

        elif game_state == STATE_SELECT:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and can_navigate:
                    selected_enemy_index = (selected_enemy_index + 1) % len(enemy_names)
                    can_navigate = False
                if event.key == pygame.K_UP and can_navigate:
                    selected_enemy_index = (selected_enemy_index - 1) % len(enemy_names)
                    can_navigate = False
                if event.key == pygame.K_RETURN:
                    enemy_name = enemy_names[selected_enemy_index]
                    enemy_sprite = enemy_sprites[enemy_name]
                    game_state = STATE_PLAYING

        elif game_state == STATE_PAUSED:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                game_state = STATE_PLAYING

        elif game_state == STATE_PLAYING:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                game_state = STATE_PAUSED
            player.handle_event(event)

        # **Reset Menu Navigation Delay**
        if event.type == pygame.KEYUP:
            can_navigate = True  # Allows another selection after releasing key

    keys = pygame.key.get_pressed()

    # **MENU SCREENS**
    if game_state == STATE_START:
        draw_start_screen(screen, font)

    elif game_state == STATE_SELECT:
        draw_select_screen(screen, font, enemy_names, selected_enemy_index)

    elif game_state == STATE_PAUSED:
        draw_pause_screen(screen, font)

    elif game_state == STATE_PLAYING:
        player.handle_input(keys)  # ✅ Allows smooth movement in-game
        player.apply_gravity(GRAVITY)
        player.update_animation(10, 8)
        player.draw(screen)

        screen.blit(enemy_sprite, (600, FLOOR_HEIGHT))  # Draw selected enemy

    pygame.display.flip()
    clock.tick(60)  # Limit FPS to 60

pygame.quit()
