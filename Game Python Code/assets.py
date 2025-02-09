import pygame
from settings import CHAR_SIZE, SCALE


# ✅ Load character animation frames (for player)
character_frames = [
    pygame.transform.scale(pygame.image.load("SpriteWalking1.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
    pygame.transform.scale(pygame.image.load("SpriteWalking2.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
    pygame.transform.scale(pygame.image.load("SpriteWalking3.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
]

# ✅ Load punch animation frames (for player)
punch_frames = [
    pygame.transform.scale(pygame.image.load("SpritePunch1.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
    pygame.transform.scale(pygame.image.load("SpritePunch2.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
]

# ✅ Load opponent sprites
OPPONENT_SPRITES = {
    "Charles Mada": {
        "walk": [
            pygame.transform.scale(pygame.image.load("Charles1.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
            pygame.transform.scale(pygame.image.load("Charles2.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
            pygame.transform.scale(pygame.image.load("Charles3.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
        ],
        "punch": [
            pygame.transform.scale(pygame.image.load("Charles4.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
            pygame.transform.scale(pygame.image.load("Charles5.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
        ],
        "idle": [
            pygame.transform.scale(pygame.image.load("Charles1.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE))
        ]
    },
    "Raghav Sureshbabu": {
        "walk": [
            pygame.transform.scale(pygame.image.load("RagWalk1.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
            pygame.transform.scale(pygame.image.load("RagWalk2.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
            pygame.transform.scale(pygame.image.load("RagWalk3.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
        ],
        "punch": [
            pygame.transform.scale(pygame.image.load("RagPunch1.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
            pygame.transform.scale(pygame.image.load("RagPunch2.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
        ],
        "idle": [
            pygame.transform.scale(pygame.image.load("RagWalk1.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE))
        ]
    },
    "Danny Berry": {
        "walk": [
            pygame.transform.scale(pygame.image.load("Danny1.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
            pygame.transform.scale(pygame.image.load("Danny2.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
            pygame.transform.scale(pygame.image.load("Danny3.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
        ],
        "punch": [
            pygame.transform.scale(pygame.image.load("Danny4.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
            pygame.transform.scale(pygame.image.load("Danny5.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
        ],
        "idle": [
            pygame.transform.scale(pygame.image.load("Danny1.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE))
        ]
    },
        "Alok Sinha": {
        "walk": [
            pygame.transform.scale(pygame.image.load("Alok1.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
            pygame.transform.scale(pygame.image.load("Alok2.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
            pygame.transform.scale(pygame.image.load("Alok3.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
        ],
        "punch": [
            pygame.transform.scale(pygame.image.load("Alok4.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
            pygame.transform.scale(pygame.image.load("Alok5.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE)),
        ],
        "idle": [
            pygame.transform.scale(pygame.image.load("Alok1.png"), (CHAR_SIZE * SCALE, CHAR_SIZE * SCALE))
        ]
    }
}


