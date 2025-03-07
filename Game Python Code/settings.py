# settings.py
# ✅ Define Opponents with Different Stats
OPPONENTS = {
    "Charles Mada": {"speed": 10, "punch_damage": 1},
    "Raghav Sureshbabu": {"speed": 1, "punch_damage": 10},
    "Danny Berry": {"speed": 5, "punch_damage": 6},
    "Alok Sinha": {"speed": 6, "punch_damage": 5}
}


# Constants
CHAR_SIZE = 32
SCALE = 4
WIN_WIDTH = CHAR_SIZE * 36
WIN_HEIGHT = CHAR_SIZE * 18
FLOOR_HEIGHT = WIN_HEIGHT - CHAR_SIZE * 4

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

# Physics & Movement
GRAVITY = 0.3
JUMP_FORCE = -12
SPEED = 5  # <---- ✅ Add this line
ANIMATION_SPEED = 10
PUNCH_ANIMATION_SPEED = 8
PUNCH_DURATION = 8

# ✅ Define Game States
STATE_START = "start"
STATE_SELECT = "select"
STATE_PLAYING = "playing"
STATE_PAUSED = "paused"
STATE_WIN = "win"
STATE_LOSE = "lose"
STATE_ROUND_WIN = "round_win"
STATE_ROUND_LOSE = "round_lose"
STATE_GAME_OVER = "game_over"  # ✅ Final winner is determined here


