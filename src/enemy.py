from pygame import Rect


class Enemy:
    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.alive = True

    def getRect(self):
        return Rect(self.x, self.y, self.width, self.height)
    
    def takeDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.alive = False