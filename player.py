from pygame import Rect
from tile import Tile, TileType

class Player:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.color = (255, 255, 255)  # White color

    def getRect(self):
        return Rect(self.x, self.y, self.width, self.height)

    def getColour(self):
        return self.color
    
    def isOnFloor(self, tilesBelow):
        for tile in tilesBelow:
            if not tile:
                continue
            else:
                if tile.tileType == TileType.BLOCK:
                    self.y = tile.y - self.height
                    return True
        return False
