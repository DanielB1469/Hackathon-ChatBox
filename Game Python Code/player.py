import pygame
from settings import SPEED, JUMP_FORCE, FLOOR_HEIGHT, GRAVITY

class Player:
    def __init__(self, x, y):
        """Initialize the player with position, health, and animation variables."""
        self.start_x = x  # Store starting X position
        self.start_y = y  # Store starting Y position
        self.rect = pygame.Rect(x, y, 128, 128)
        self.velocity_y = 0
        self.on_ground = False
        self.moving = False
        self.is_punching = False
        self.is_blocking = False
        self.health = 100
        self.max_health = 100

        # Animation Variables
        self.animation_index = 0  # Tracks animation frame
        self.frame_count = 0  # Controls animation speed
        self.punch_timer = 0  # Controls punch animation timing
        self.facing_right = True  # Tracks player direction

    def handle_input(self, keys):
        """Handles movement, jumping, and blocking."""
        self.moving = False

        if not self.is_punching and not self.is_blocking:  # Prevents movement while punching/blocking
            if keys[pygame.K_a]:  # Move left
                self.rect.x -= SPEED
                self.moving = True
                self.facing_right = False  # Face left
            if keys[pygame.K_d]:  # Move right
                self.rect.x += SPEED
                self.moving = True
                self.facing_right = True  # Face right

        # Jumping
        if keys[pygame.K_w] and self.on_ground:
            self.velocity_y = JUMP_FORCE
            self.on_ground = False

        # Blocking
        if keys[pygame.K_g]:  
            self.is_blocking = True
            self.is_punching = False  # Prevent punching while blocking
        else:
            self.is_blocking = False  # Release block

    def handle_event(self, event):
        """Handles discrete key presses like punching."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not self.is_punching and not self.is_blocking:
                self.is_punching = True
                self.punch_timer = 10  # Duration of punch animation

    def apply_gravity(self):
        """Apply gravity to the player."""
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        # Prevent falling through floor
        if self.rect.y >= FLOOR_HEIGHT:
            self.rect.y = FLOOR_HEIGHT
            self.velocity_y = 0
            self.on_ground = True

    def take_damage(self, amount):
        """Reduce health when hit, unless blocking."""
        if self.is_blocking:
            amount *= 0.3  # Reduce damage by 70% when blocking
        self.health -= amount
        if self.health < 0:
            self.health = 0  # Prevent negative health

    def update_animation(self, ANIMATION_SPEED, PUNCH_ANIMATION_SPEED):
        """Handles animation updates for movement, punching, and blocking."""
        if self.is_punching:
            self.punch_timer -= 1
            if self.punch_timer <= 0:
                self.is_punching = False  # Stop punch animation
        elif self.moving:
            self.frame_count += 1
            if self.frame_count >= ANIMATION_SPEED:
                self.frame_count = 0
                self.animation_index = (self.animation_index + 1) % 3  # Cycle through walk frames
        else:
            self.animation_index = 0  # Reset to idle frame

    def reset_position(self):
        """Resets the player to their starting position after each round."""
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.health = self.max_health  # Reset health

    def draw(self, screen, character_frames, punch_frames):
        """Draws the player sprite based on the current animation state."""
        if self.is_punching:
            sprite = punch_frames[0]
        elif self.is_blocking:
            sprite = character_frames[2]  # Use a blocking frame
        else:
            sprite = character_frames[self.animation_index]

        # Flip sprite if facing left
        if not self.facing_right:
            sprite = pygame.transform.flip(sprite, True, False)

        screen.blit(sprite, (self.rect.x, self.rect.y))

