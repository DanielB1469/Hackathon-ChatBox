import pygame
from settings import SPEED, JUMP_FORCE, FLOOR_HEIGHT, CHAR_SIZE, SCALE
from assets import character_frames, punch_frames
from audio import block_sound, punch_sound, walking_sound, landing_sound  # Import the sounds

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)
        self.velocity_y = 0
        self.on_ground = False
        self.moving = False
        self.animation_index = 0
        self.frame_count = 0
        self.is_punching = False
        self.punch_index = 0
        self.punch_timer = 0
        self.move_played = False  # Track if move sound has played

    def handle_input(self, keys):
        """Handles movement continuously while keys are held"""
        self.moving = False

        if not self.is_punching:  # Prevent movement when punching
            if keys[pygame.K_a]:  # Move left
                self.rect.x -= SPEED
                self.moving = True
            if keys[pygame.K_d]:  # Move right
                self.rect.x += SPEED
                self.moving = True

        # Play walking sound when moving starts (but only once)
        if self.moving and not self.move_played:
            walking_sound.stop()  # Stop any previous walking sound to avoid overlap
            walking_sound.play()  # Play walking sound when moving
            self.move_played = True
        elif not self.moving:
            self.move_played = False  # Reset to allow sound to play again when movement starts

    def handle_event(self, event):
        """Handle key press actions (punching and jumping)"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not self.is_punching:
                self.is_punching = True
                self.punch_index = 0
                self.punch_timer = 16
                punch_sound.play()  # Play punch sound when punching

            if event.key == pygame.K_w and self.on_ground:
                self.velocity_y = JUMP_FORCE
                self.on_ground = False
                landing_sound.play()  # Play landing sound when jumping

    def apply_gravity(self, gravity):
        self.velocity_y += gravity
        self.rect.y += self.velocity_y

        # Floor collision
        if self.rect.y >= FLOOR_HEIGHT:
            self.rect.y = FLOOR_HEIGHT
            self.velocity_y = 0
            self.on_ground = True

    def update_animation(self, ANIMATION_SPEED, PUNCH_ANIMATION_SPEED):
        if self.is_punching:
            self.punch_timer -= 1
            if self.punch_timer <= 0:
                self.is_punching = False
            else:
                self.punch_index = (self.punch_timer // PUNCH_ANIMATION_SPEED) % len(punch_frames)
        elif self.moving:
            self.frame_count += 1
            if self.frame_count >= ANIMATION_SPEED:
                self.frame_count = 0
                self.animation_index = (self.animation_index + 1) % len(character_frames)
        else:
            self.animation_index = 0  # Reset to first frame when idle

    def draw(self, screen):
        if self.is_punching:
            screen.blit(punch_frames[self.punch_index], (self.rect.x, self.rect.y))
        else:
            screen.blit(character_frames[self.animation_index], (self.rect.x, self.rect.y))
