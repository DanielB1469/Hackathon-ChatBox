import pygame
from settings import SPEED, JUMP_FORCE, FLOOR_HEIGHT, CHAR_SIZE, SCALE, WIN_WIDTH, GRAVITY

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)
        self.velocity_y = 0
        self.on_ground = False
        self.moving = False
        self.animation_index = 0
        self.frame_count = 0
        self.facing_right = True  # ✅ Track which direction the player is facing

        # ✅ Health
        self.max_health = 100
        self.health = self.max_health

        # Punch state
        self.is_punching = False
        self.punch_index = 0
        self.punch_timer = 0

    def handle_input(self, keys):
        """Handles movement continuously while keys are held"""
        self.moving = False
        if not self.is_punching:  # Prevent movement when punching
            if keys[pygame.K_a]:  # Move left
                self.rect.x -= SPEED
                self.rect.x = max(0, self.rect.x)  # Prevent moving off-screen
                self.moving = True
                self.facing_right = False  # ✅ Correctly set facing direction

            if keys[pygame.K_d]:  # Move right
                self.rect.x += SPEED
                self.rect.x = min(WIN_WIDTH - self.rect.width, self.rect.x)  # Prevent moving off-screen
                self.moving = True
                self.facing_right = True  # ✅ Correctly set facing direction

    def handle_event(self, event):
        """Handle key press actions (jumping, punching)"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not self.is_punching:
                self.is_punching = True
                self.punch_index = 0
                self.punch_timer = 16

            if event.key == pygame.K_w and self.on_ground:
                self.velocity_y = JUMP_FORCE
                self.on_ground = False

    def apply_gravity(self):
        """Apply gravity to player character"""
        self.velocity_y += GRAVITY  # Apply downward force
        self.rect.y += self.velocity_y

        # ✅ Floor collision
        if self.rect.y >= FLOOR_HEIGHT:
            self.rect.y = FLOOR_HEIGHT
            self.velocity_y = 0
            self.on_ground = True

    def take_damage(self, amount):
        """Reduce health when hit"""
        self.health -= amount
        if self.health < 0:
            self.health = 0  # Prevent health from going negative

    def update_animation(self, ANIMATION_SPEED, PUNCH_ANIMATION_SPEED):
        """Handles animation updates for movement and punching"""
        if self.is_punching:
            self.punch_timer -= 1
            if self.punch_timer <= 0:
                self.is_punching = False
            else:
                self.punch_index = (self.punch_timer // PUNCH_ANIMATION_SPEED) % 2
        elif self.moving:
            self.frame_count += 1
            if self.frame_count >= ANIMATION_SPEED:
                self.frame_count = 0
                self.animation_index = (self.animation_index + 1) % 3
        else:
            self.animation_index = 0  # Reset to first frame when idle

    def draw(self, screen, character_frames, punch_frames):
        """Draw player sprite on screen and flip it based on direction"""
        if self.is_punching:
            sprite = punch_frames[self.punch_index]
        else:
            sprite = character_frames[self.animation_index]

        # ✅ Flip sprite if facing left
        if not self.facing_right:
            sprite = pygame.transform.flip(sprite, True, False)

        # ✅ Debugging: Print direction
        # print("Facing Right:", self.facing_right)  # Uncomment this to check in terminal

        # Draw the sprite
        screen.blit(sprite, (self.rect.x, self.rect.y))
