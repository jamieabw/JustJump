import pygame # type: ignore
import random
from map import Map
from player import Player
from tile import TileType

"""
CURRENTLY: there is a grid system, and a player (kind of?), there is momentum type physics and
gravity is already implemented, the camera has also been successfully implemented
TODO: 
- collisions - figure out the tiling indexes for the left, right, up, and down
- implement left and right movement
- proper map loading from file
- procedural map generation
- test hard coded map
- artwork

"""


# constants
FPS = 60
WIDTH = 30
HEIGHT = 30
DOWN_ACCELERATION = 10
MOVEMENT_ACCELERATION = 1.5
FRICTION_ACCELERATION = 1.5

def main():
    test = TestGame()
    test.run()

class TestGame:
    def __init__(self):
        self.delta = 0
        self.downVel = 0
        self.moveVel = 0
        self.tilesToCheck = ()
        self.pipes = []
        self.cameraX, self.cameraY = (0,0)
        self.map = Map()
        self.map.createMapGrid()


    # function to start the game
    def run(self):
        self.screen = pygame.display.set_mode((1000, 800))
        self.running = True
        self.clock = pygame.time.Clock()
        self.player = Player(200, 0)
        self.runLoop()

    
    def eventLoop(self):
        
        #self.checkCollision()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.y -= 10
                    self.downVel = -10
                if event.key == pygame.K_d: # this is currently only tapping, not holding FIX THIS
                    self.player.x += 10 # TEMPORARY!!!!!!

    def runLoop(self):
        while self.running:
            self.update()
            self.render()
            self.eventLoop()
            self.clock.tick(FPS)


    def render(self):
        self.screen.fill((0,0,0))
        for row in self.map.mapGrid:
            for tile in row:
                tempRect = tile.getRect()
                tempRect.x -= (self.cameraX)
                tempRect.y -= (self.cameraY)
                pygame.draw.rect(self.screen, tile.getColour(), tempRect)
        pygame.draw.rect(self.screen, self.player.getColour(), self.player.getRect().move(-self.cameraX, -self.cameraY))
        pygame.display.update()
        pygame.display.flip()

    def update(self):
        self.getTilesToCheck()
        if not self.player.isOnFloor((self.tilesToCheck[2], self.tilesToCheck[3])):
            self.downVel += (DOWN_ACCELERATION / FPS)
        else:
            self.downVel = 0
        if self.moveVel != 0:
            self.moveVel = max(0, (self.moveVel - (FRICTION_ACCELERATION / FPS)))

        self.player.y += self.downVel
        self.player.x += self.moveVel
        self.cameraX = self.player.x - self.screen.get_width() // 2
        self.cameraX = min(max(0, self.cameraX), Map.TILE_SIZE * Map.MAP_TILE_SIZE - self.screen.get_width())
        self.cameraY = self.player.y - self.screen.get_height() // 2
        self.cameraY = min(max(0, self.cameraY), Map.TILE_SIZE * Map.MAP_TILE_SIZE - self.screen.get_height())


    def getTilesToCheck(self):
        # i need to somehow get this to be the index not thed pixel pos
        cornerCoords = self.getPlayerCornerCoords()
        self.tilesToCheck = []
        for x,y in cornerCoords:
            self.tilesToCheck.append(self.map.mapGrid[int(y)][x])
        return self.tilesToCheck
    
    
    def testTiles(self):
        for tile in self.tilesToCheck:
            tile.tileType = TileType.BLOCK
    
    def getPlayerCornerCoords(self):
        # gets each corner of the player rect hitbox for determining which tiles to check for collisions
        topLeft = (self.player.x // Map.TILE_SIZE, self.player.y // Map.TILE_SIZE)
        topRight= ((self.player.x + self.player.width) // Map.TILE_SIZE, self.player.y // Map.TILE_SIZE)
        bottomLeft = (self.player.x // Map.TILE_SIZE, (self.player.y + self.player.height) // Map.TILE_SIZE)
        bottomRight = ((self.player.x + self.player.width) // Map.TILE_SIZE, (self.player.y + self.player.height) // Map.TILE_SIZE)
        return [topLeft, topRight, bottomRight, bottomLeft]

    def checkCollision(self):
        # this is actually working?
        tiles = self.getTilesToCheck()
        for tile in tiles:
            if tile.tileType.name == "BLOCK" and self.player.getRect().colliderect(tile.getRect()):
                print("collision")
                self.downVel = 0
                self.player.y = tile.y - self.player.height


        

if __name__ == "__main__":
    main()