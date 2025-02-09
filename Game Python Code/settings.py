# settings.py

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
GRAVITY = 0.7
JUMP_FORCE = -12
SPEED = 5  # <---- ✅ Add this line
ANIMATION_SPEED = 10
PUNCH_ANIMATION_SPEED = 8
PUNCH_DURATION = 16

# Game States
# ✅ Define Game States
STATE_START = "start"
STATE_SELECT = "select"
STATE_PLAYING = "playing"
STATE_PAUSED = "paused"
STATE_WIN = "win"  # ✅ Add this
STATE_LOSE = "lose"  # ✅ Add this

