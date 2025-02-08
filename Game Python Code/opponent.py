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
        self.facing_right = True  # ✅ Keeps track of opponent's direction

        # ✅ Health
        self.max_health = 100
        self.health = self.max_health

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
        # ✅ Update facing direction based on player's position
        self.facing_right = self.rect.x < player_x

        if self.state == "approaching":
            if abs(self.rect.x - player_x) > self.punch_range:
                self.rect.x += self.speed if self.facing_right else -self.speed
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
            self.rect.x += -self.speed if self.facing_right else self.speed
            if abs(self.rect.x - player_x) > self.punch_range * 2:
                self.state = "approaching"

    def take_damage(self, amount):
        """Reduce health when hit"""
        self.health -= amount
        if self.health < 0:
            self.health = 0  # Prevent health from going negative

    def draw(self, screen):
        """Draws the opponent based on its current action, ensuring it faces the player."""
        if self.state == "punching":
            sprite = self.punch_frames[self.current_frame]
        elif self.state == "approaching" or self.state == "retreating":
            sprite = self.walk_frames[self.current_frame % len(self.walk_frames)]
        else:
            sprite = self.idle_frames[self.current_frame % len(self.idle_frames)]

        # ✅ Flip sprite if opponent is facing left
        if not self.facing_right:
            sprite = pygame.transform.flip(sprite, True, False)

        screen.blit(sprite, (self.rect.x, self.rect.y))
