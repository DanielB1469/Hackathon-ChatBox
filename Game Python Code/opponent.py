import pygame
from settings import WIN_WIDTH
from assets import OPPONENT_SPRITES

class Opponent:
    def __init__(self, x, y, speed, punch_range, punch_damage, name):
        """Initialize opponent with health, speed, and animations."""
        self.start_x = x  
        self.start_y = y  
        self.rect = pygame.Rect(x, y, 128, 128)
        self.speed = speed  
        self.punch_range = punch_range
        self.punch_damage = punch_damage
        self.health = 100  
        self.max_health = 100  
        self.state = "approaching"
        self.facing_right = True
        self.punch_timer = 0  # ✅ Controls punch animation timing

        # ✅ Load sprites based on opponent name
        self.walk_frames = OPPONENT_SPRITES[name]["walk"]
        self.punch_frames = OPPONENT_SPRITES[name]["punch"]
        self.idle_frames = OPPONENT_SPRITES[name]["idle"]

        self.current_frame = 0
        self.animation_speed = 10
        self.frame_counter = 0

    def take_damage(self, amount):
        """Reduces opponent's health when hit."""
        self.health -= amount
        if self.health < 0:
            self.health = 0  

    def reset_position(self):
        """Resets the opponent to their starting position after each round."""
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.health = self.max_health  
        self.state = "approaching"  

    def update(self, player_x):
        """AI Behavior: Approaches, Attacks, Retreats"""
        if abs(self.rect.x - player_x) > self.punch_range:
            # ✅ Move toward player
            if self.rect.x < player_x:
                self.rect.x += self.speed
                self.facing_right = True
            else:
                self.rect.x -= self.speed
                self.facing_right = False
            self.state = "approaching"

        else:
            self.state = "punching"
            self.punch_timer = 10  # ✅ Set punch animation duration

        # ✅ Keep Opponent Within Bounds
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > WIN_WIDTH - self.rect.width:
            self.rect.x = WIN_WIDTH - self.rect.width

    def draw(self, screen):
        """Draws the opponent based on its current action."""
        if self.state == "punching":
            # ✅ Show punch animation while punch_timer > 0
            if self.punch_timer > 0:
                sprite = self.punch_frames[self.current_frame % len(self.punch_frames)]
                self.punch_timer -= 1
            else:
                self.state = "approaching"  # ✅ Return to normal movement

        elif self.state == "approaching":
            sprite = self.walk_frames[self.current_frame % len(self.walk_frames)]

        else:
            sprite = self.idle_frames[0]  

        # ✅ Flip Sprite if Opponent Faces Left
        if not self.facing_right:
            sprite = pygame.transform.flip(sprite, True, False)

        screen.blit(sprite, (self.rect.x, self.rect.y))
