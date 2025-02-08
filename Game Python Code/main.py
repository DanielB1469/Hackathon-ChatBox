import pygame

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
ANIMATION_SPEED = 10  # Adjust animation speed

# Setup the window
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Pygame Platformer")

# Load character animation frames
character_frames = [
    pygame.transform.scale(pygame.image.load("SpriteWalking1.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
    pygame.transform.scale(pygame.image.load("SpriteWalking2.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
    pygame.transform.scale(pygame.image.load("SpriteWalking3.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
]

# Character properties
character = pygame.Rect(100, FLOOR_HEIGHT, CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)
velocity_y = 0
on_ground = False
moving = False
animation_index = 0
frame_count = 0

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # 60 FPS
    
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get key presses
    keys = pygame.key.get_pressed()
    
    # Movement logic
    moving = False
    if keys[pygame.K_a]:
        character.x -= SPEED
        moving = True
    if keys[pygame.K_d]:
        character.x += SPEED
        moving = True

    # Jumping
    if keys[pygame.K_w] and on_ground:
        velocity_y = JUMP_FORCE
        on_ground = False
    
    # Apply gravity
    velocity_y += GRAVITY
    character.y += velocity_y

    # Floor collision
    if character.y >= FLOOR_HEIGHT:
        character.y = FLOOR_HEIGHT
        velocity_y = 0
        on_ground = True

    # Keep character within screen bounds
    if character.x < 0:
        character.x = 0
    if character.x > WIN_WIDTH - character.width:
        character.x = WIN_WIDTH - character.width

    # Handle animation
    if moving:
        frame_count += 1
        if frame_count >= ANIMATION_SPEED:
            frame_count = 0
            animation_index = (animation_index + 1) % len(character_frames)
    else:
        animation_index = 0  # Reset to first frame when idle

    # Drawing
    screen.fill(GRAY)  # Background color
    pygame.draw.rect(screen, BLACK, (0, FLOOR_HEIGHT + CHAR_SIZE * SCALE, WIN_WIDTH, CHAR_SIZE * SCALE))  # Floor
    screen.blit(character_frames[animation_index], (character.x, character.y))  # Draw character

    # Update display
    pygame.display.flip()

pygame.quit()
