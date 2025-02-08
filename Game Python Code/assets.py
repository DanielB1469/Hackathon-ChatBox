import pygame
from settings import CHAR_SIZE, SCALE

# Load character animation frames
character_frames = [
    pygame.transform.scale(pygame.image.load("SpriteWalking1.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
    pygame.transform.scale(pygame.image.load("SpriteWalking2.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
    pygame.transform.scale(pygame.image.load("SpriteWalking3.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
]

punch_frames = [
    pygame.transform.scale(pygame.image.load("SpritePunch1.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
    pygame.transform.scale(pygame.image.load("SpritePunch2.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
]

# Load enemy sprites
enemy_sprites = {
    "Charles Mada": pygame.transform.scale(pygame.image.load("Sprite-0001.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
    "Raghav Sureshbabu": pygame.transform.scale(pygame.image.load("Sprite-0001.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
    "Danny Berry": pygame.transform.scale(pygame.image.load("Sprite-0001.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
    "Alok Sinha": pygame.transform.scale(pygame.image.load("Sprite-0001.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),

}
