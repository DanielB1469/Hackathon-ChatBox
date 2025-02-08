import pygame

# Initialize Pygame's mixer for sound effects
pygame.mixer.init()

# Load sound effects (MP3 files)
block_sound = pygame.mixer.Sound("assets/sounds/Block.mp3")
punch_sound = pygame.mixer.Sound("assets/sounds/punch.mp3")
walking_sound = pygame.mixer.Sound("assets/sounds/Walking.mp3")
knock_out_sound = pygame.mixer.Sound("assets/sounds/Knock Out.mp3")
landing_sound = pygame.mixer.Sound("assets/sounds/landing.mp3")

# Set volume for sounds
block_sound.set_volume(1.0)
punch_sound.set_volume(1.0)
walking_sound.set_volume(1.0)
knock_out_sound.set_volume(1.0)
landing_sound.set_volume(1.0)
