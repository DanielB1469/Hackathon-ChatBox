import pygame
from settings import *
from player import Player
from opponent import Opponent
from ui_screens import (
    draw_start_screen,
    draw_select_screen,
    draw_pause_screen,
    draw_win_screen,
    draw_lose_screen
)
from assets import enemy_sprites, character_frames, punch_frames

# ✅ Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("AI Boxing Game")

# ✅ Load Game Background
game_background = pygame.image.load("BoxingRing.png")
game_background = pygame.transform.scale(game_background, (WIN_WIDTH, WIN_HEIGHT))

# ✅ Game state
game_state = STATE_START

# ✅ Load font
font = pygame.font.Font(None, 40)

# ✅ Enemy Selection Variables
enemy_names = list(enemy_sprites.keys())
selected_enemy_index = 0
can_navigate = True  # Prevent holding navigation keys in menus
enemy_name = "Opponent"  # Default opponent name

# ✅ Create player and opponent
player = Player(100, FLOOR_HEIGHT)
opponent = Opponent(600, FLOOR_HEIGHT, speed=2, punch_range=100)

# ✅ Function to draw labeled health bars
def draw_health_bars(screen, player, opponent, opponent_name):
    """Draws labeled health bars for player and opponent"""
    font = pygame.font.Font(None, 36)  # ✅ Set font for labels

    # ✅ Player Health Bar (Labeled "You")
    pygame.draw.rect(screen, (255, 0, 0), (50, 30, 400, 20))  # Background
    pygame.draw.rect(screen, (0, 255, 0), (50, 30, 400 * (player.health / player.max_health), 20))  # Health
    player_label = font.render("You", True, (255, 255, 255))  # ✅ Label "You"
    screen.blit(player_label, (50, 5))  # Position label above health bar

    # ✅ Opponent Health Bar (Labeled with Name)
    pygame.draw.rect(screen, (255, 0, 0), (550, 30, 400, 20))  # Background
    pygame.draw.rect(screen, (0, 255, 0), (550, 30, 400 * (opponent.health / opponent.max_health), 20))  # Health
    enemy_label = font.render(opponent_name, True, (255, 255, 255))  # ✅ Label with enemy's name
    screen.blit(enemy_label, (550, 5))  # Position label above health bar

# ✅ Function to check game over
def check_game_over():
    global game_state
    if player.health <= 0:
        print("Game Over! You lost!")
        game_state = STATE_LOSE  # ✅ Now switches to lose screen
        player.health=100
        opponent.health=100

    elif opponent.health <= 0:
        print("You won the fight!")
        game_state = STATE_WIN  # ✅ Now switches to win screen
        player.health=100
        opponent.health=100

# ✅ Main game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(GRAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # **Start Screen Logic**
        if game_state == STATE_START:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  
                game_state = STATE_SELECT

        # **Selection Screen Logic**
        elif game_state == STATE_SELECT:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_enemy_index = (selected_enemy_index + 1) % len(enemy_names)
                if event.key == pygame.K_UP:
                    selected_enemy_index = (selected_enemy_index - 1) % len(enemy_names)
                if event.key == pygame.K_RETURN:
                    enemy_name = enemy_names[selected_enemy_index]  # ✅ Get selected opponent name
                    opponent = Opponent(600, FLOOR_HEIGHT, speed=2, punch_range=100)  # ✅ Reset opponent
                    game_state = STATE_PLAYING

        # **Pause Screen Logic**
        elif game_state == STATE_PAUSED:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                game_state = STATE_PLAYING

        # **Win/Lose Handling**
        elif game_state in [STATE_WIN, STATE_LOSE]:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # ✅ Restart the match
                    print("Restarting Match...")  # ✅ Debugging
                    player.health = player.max_health
                    opponent.health = opponent.max_health
                    game_state = STATE_PLAYING

                if event.key == pygame.K_j:  # ✅ Go back to character select
                    print("Returning to Character Select...")  # ✅ Debugging
                    game_state = STATE_SELECT

        # **Game Playing Logic**
        elif game_state == STATE_PLAYING:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                game_state = STATE_PAUSED
            player.handle_event(event)

    keys = pygame.key.get_pressed()

    # **Screen Rendering Based on State**
    if game_state == STATE_START:
        draw_start_screen(screen, font)
    elif game_state == STATE_SELECT:
        draw_select_screen(screen, font, enemy_names, selected_enemy_index)
    elif game_state == STATE_PAUSED:
        draw_pause_screen(screen, font)
    elif game_state == STATE_WIN:
        draw_win_screen(screen, font)
    elif game_state == STATE_LOSE:
        draw_lose_screen(screen, font)
    elif game_state == STATE_PLAYING:
        screen.blit(game_background, (0, 0))

        # ✅ Update Player
        player.handle_input(keys)
        player.apply_gravity()
        player.update_animation(10, 8)
        player.draw(screen, character_frames, punch_frames)

        # ✅ Update Opponent AI
        opponent.update(player.rect.x)
        opponent.draw(screen)

        # ✅ Draw labeled health bars
        draw_health_bars(screen, player, opponent, enemy_name)

        # ✅ Attack Logic
        if player.is_punching and abs(player.rect.x - opponent.rect.x) < 50:
            opponent.take_damage(5)

        if opponent.state == "punching" and abs(player.rect.x - opponent.rect.x) < 50:
            player.take_damage(5)

        # ✅ Check for game over
        check_game_over()

    pygame.display.flip()
    clock.tick(60)  # Limit FPS to 60

pygame.quit()
