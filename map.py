from tile import Tile
from tile import TileType
from island import Island
from random import randrange, randint, choice


X_TILES_GAP = 6 # maximum 14 tiles away x
Y_TILES_GAP = 2
SPAWN_TILE_X = 1
SPAWN_TILE_Y = 98

class Map:
    TILE_SIZE = Tile.TILE_SIZE
    MAP_TILE_SIZE = 100 # 800x800 tile map, so 6400x6400 pixel map
    def __init__(self):
        self.mapGrid = []
        self.islands = []
        

    """
    currently a temp function to draw a random hardcoded map, will eventually generate a random map
    """
    def createMapGrid(self):
        for y in range(Map.MAP_TILE_SIZE):
            temp = [] # stores all x for a given y
            for x in range(Map.MAP_TILE_SIZE):
                temp.append(Tile(x, y))
            self.mapGrid.append(temp)
        for cell in self.mapGrid[Map.MAP_TILE_SIZE-1]:
            cell.tileType = TileType.BLOCK
        for cell in self.mapGrid[0]:
            cell.tileType = TileType.BLOCK
        for i in range(Map.MAP_TILE_SIZE):
            self.mapGrid[i][0].tileType = TileType.BLOCK
            self.mapGrid[i][Map.MAP_TILE_SIZE-1].tileType = TileType.BLOCK

        self.mapGrid[Map.MAP_TILE_SIZE - 2][Map.MAP_TILE_SIZE - 2].tileType = TileType.EXIT
        self.populateWithIslands()
        self.fillAmbientIslands()
        for island in self.islands:
            tileX = int(island.x // Map.TILE_SIZE)
            tileY = int(island.y // Map.TILE_SIZE)
            self.mapGrid[tileY][tileX].tileType = TileType.BLOCK

    def populateWithIslands(self):
        self.islands.append(self.createPathIsland(Island(SPAWN_TILE_X * Map.TILE_SIZE, SPAWN_TILE_Y * Map.TILE_SIZE,0,0)))
        for i in range(100):
            try:
                self.islands.append(self.createPathIsland(self.islands[-1]))
            except IndexError:
                break
    

    def fillAmbientIslands(self, count=200):
        while len(self.islands) < count:
            x = randint(2, Map.MAP_TILE_SIZE - 10) * Map.TILE_SIZE
            y = randint(2, Map.MAP_TILE_SIZE - 10) * Map.TILE_SIZE

            width = randint(2, 6) * Map.TILE_SIZE
            height = randint(2, 6) * Map.TILE_SIZE

            island = Island(x, y, width, height)

            if not any(self.intersects(island, other) for other in self.islands):
                self.islands.append(island)


        


        

    def createPathIsland(self, prevIsland):
        xGap = (X_TILES_GAP * (randrange(4, 9) / 10)) * Map.TILE_SIZE
        yGap = (Y_TILES_GAP * (randrange(4,9) / 10)) * Map.TILE_SIZE
        width = randint(2, 4) * Map.TILE_SIZE
        height = randint(2, 4) * Map.TILE_SIZE
        island = Island(prevIsland.x + prevIsland.width + xGap, prevIsland.y - prevIsland.height - yGap, width, height)
        #island = Island(prevIsland.x +  xGap, prevIsland.y -  yGap, width, height)
        tileX = int(island.x // Map.TILE_SIZE)
        tileY = int(island.y // Map.TILE_SIZE)
        self.mapGrid[tileY][tileX]
        return island
    

    def intersects(self, a, b, padding_tiles=1):
        pad = padding_tiles * Map.TILE_SIZE

        return not (
            a.x + a.width + pad <= b.x - pad or
            a.x - pad >= b.x + b.width + pad or
            a.y + a.height + pad <= b.y - pad or
            a.y - pad >= b.y + b.height + pad
        )

        

    """
    debugging function to print out the grid in terminal
    """
    def __str__(self):
        result = ""
        for row in self.mapGrid:
            tempRow = []
            for tile in row:
                tempRow.append((tile.tileX, tile.tileY, tile.tileType.value))
            result += f"{tempRow}" + "\n"
        return result
    



if __name__ == "__main__":
    map = Map()
    map.createMapGrid()
    print(map)

