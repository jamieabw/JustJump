import pygame # type: ignore
import random
from map import Map
from player import Player

"""
CURRENTLY: there is a grid system, and a player (kind of?), there is momentum type physics and
gravity is already implemented, the camera has also been successfully implemented
TODO: 
- collisions
- test hard coded map
- artwork

"""


# constants
FPS = 60
WIDTH = 30
HEIGHT = 30
DOWN_ACCELERATION = 5
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
        self.checkCollision()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.downVel = -10
                if event.key == pygame.K_d: # this is currently only tapping, not holding FIX THIS
                    self.player.x += 10 # TEMPORARY!!!!!!

    def runLoop(self):
        while self.running:
            self.eventLoop()
            self.update()
            self.render()
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
        self.downVel += (DOWN_ACCELERATION / FPS)
        if self.moveVel != 0:
            self.moveVel = max(0, (self.moveVel - (FRICTION_ACCELERATION / FPS)))

        self.player.y += self.downVel
        self.player.x += self.moveVel
        self.cameraX = self.player.x - self.screen.get_width() // 2
        self.cameraX = min(max(0, self.cameraX), Map.TILE_SIZE * Map.MAP_TILE_SIZE - self.screen.get_width())
        self.cameraY = self.player.y - self.screen.get_height() // 2
        self.cameraY = min(max(0, self.cameraY), Map.TILE_SIZE * Map.MAP_TILE_SIZE - self.screen.get_height())


    def getTiles(self):
        # i need to somehow get this to be the index not the pixel pos
        leftTile = self.player.x // Map.TILE_SIZE
        rightTile = (self.player.x + self.player.width - 1) // Map.TILE_SIZE
        downTile = (self.player.y + self.player.height - 1) // Map.TILE_SIZE
        upTile = self.player.y // Map.TILE_SIZE
        return (upTile, rightTile, downTile, leftTile)

    def checkCollision(self):
        tiles = self.getTiles()
        for tile in tiles:
            if tile.tileType.name == "BLOCK" and self.player.getRect().colliderect(tile.getRect()):
                print("collision")
                self.downVel = 0
                self.player.y = tile.y - self.player.height

        

if __name__ == "__main__":
    main()