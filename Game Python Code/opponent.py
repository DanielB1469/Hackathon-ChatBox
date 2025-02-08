import pygame

class Opponent:
    def __init__(self, x, y, speed, punch_range):
        self.rect = pygame.Rect(x, y, 128, 128)  # ✅ Use a rect like Player
        self.speed = speed
        self.punch_range = punch_range
        self.state = "approaching"  # States: approaching, punching, retreating
        self.punch_timer = 0
        self.punch_count = 0
        self.punch_limit = 3  # Maximum punches in a sequence

        # Load animations
        self.walk_frames = [
            pygame.transform.scale(pygame.image.load("RagWalk1.png"), (128, 128)),
            pygame.transform.scale(pygame.image.load("RagWalk2.png"), (128, 128)),
            pygame.transform.scale(pygame.image.load("RagWalk3.png"), (128, 128))
        ]
        self.punch_frames = [
            pygame.transform.scale(pygame.image.load("RagPunch1.png"), (128, 128)),
            pygame.transform.scale(pygame.image.load("RagPunch2.png"), (128, 128)),
        ]
        self.idle_frames = [
            pygame.transform.scale(pygame.image.load("RagWalk1.png"), (128, 128)),
            pygame.transform.scale(pygame.image.load("RagWalk1.png"), (128, 128)),
        ]
        
        self.current_frame = 0
        self.animation_speed = 10
        self.frame_counter = 0

    def update(self, player_x):
        """AI Behavior: Approaches, Attacks, Retreats"""
        if self.state == "approaching":
            if abs(self.rect.x - player_x) > self.punch_range:
                self.rect.x += self.speed if self.rect.x < player_x else -self.speed
            else:
                self.state = "punching"
                self.punch_timer = 30
                self.punch_count = 0

        elif self.state == "punching":
            self.punch_timer -= 1
            if self.punch_timer % 10 < 5:
                self.current_frame = 0
            else:
                self.current_frame = 1
            
            if self.punch_timer <= 0 or self.punch_count >= self.punch_limit:
                self.state = "retreating"

        elif self.state == "retreating":
            self.rect.x += -self.speed if self.rect.x < player_x else self.speed
            if abs(self.rect.x - player_x) > self.punch_range * 2:
                self.state = "approaching"

    def draw(self, screen):
        """Draws the opponent based on its current action."""
        if self.state == "punching":
            screen.blit(self.punch_frames[self.current_frame], (self.rect.x, self.rect.y))
        elif self.state == "approaching" or self.state == "retreating":
            screen.blit(self.walk_frames[self.current_frame % len(self.walk_frames)], (self.rect.x, self.rect.y))
        else:
            screen.blit(self.idle_frames[self.current_frame % len(self.idle_frames)], (self.rect.x, self.rect.y))
