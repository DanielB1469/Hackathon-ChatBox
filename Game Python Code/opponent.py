import pygame

class Opponent:
    def __init__(self, x, y, speed, punch_range, punch_damage):
        self.rect = pygame.Rect(x, y, 128, 128)
        self.speed = speed  # ✅ Speed now varies per opponent
        self.punch_range = punch_range
        self.punch_damage = punch_damage  # ✅ Punch damage now varies per opponent
        self.health = 100  # ✅ Default health
        self.max_health = 100  # ✅ Max health for health bar
        self.state = "approaching"
        self.punch_timer = 0
        self.punch_count = 0
        self.punch_limit = 3

        # ✅ Load sprites (Replace with actual images)
        self.walk_frames = [
            pygame.transform.scale(pygame.image.load("RagWalk1.png"), (128, 128)),
            pygame.transform.scale(pygame.image.load("RagWalk2.png"), (128, 128)),
            pygame.transform.scale(pygame.image.load("RagWalk3.png"), (128, 128))
        ]
        self.punch_frames = [
            pygame.transform.scale(pygame.image.load("RagPunch1.png"), (128, 128)),
            pygame.transform.scale(pygame.image.load("RagPunch2.png"), (128, 128)),
        ]
        self.idle_frames = [self.walk_frames[0], self.walk_frames[1]]  # Idle = first two frames

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
            if self.punch_timer <= 0 or self.punch_count >= self.punch_limit:
                self.state = "retreating"

        elif self.state == "retreating":
            self.rect.x += -self.speed if self.rect.x < player_x else self.speed
            if abs(self.rect.x - player_x) > self.punch_range * 2:
                self.state = "approaching"

    def take_damage(self, amount):
        """Reduce opponent's health"""
        self.health -= amount
        if self.health < 0:
            self.health = 0  # Prevent negative health

    def attack(self, player):
        """Opponent punches the player with their damage value"""
        player.take_damage(self.punch_damage)

    def draw(self, screen):
        """Draws the opponent based on its current action."""
        if self.state == "punching":
            sprite = self.punch_frames[self.current_frame % len(self.punch_frames)]
        elif self.state == "approaching" or self.state == "retreating":
            sprite = self.walk_frames[self.current_frame % len(self.walk_frames)]
        else:
            sprite = self.idle_frames[self.current_frame % len(self.idle_frames)]

        screen.blit(sprite, (self.rect.x, self.rect.y))
