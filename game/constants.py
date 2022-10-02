
# rgb colors
from enum import Enum

WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0, 0, 0)

BLOCK_SIZE = 20
SPEED = 20




class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4