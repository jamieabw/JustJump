import pygame
import pygame_menu
from level import Level

class Menu:
    def __init__(self, screen, sceneManager):
        self.screen = screen
        self.sceneManager = sceneManager
        self.menu = pygame_menu.Menu("TimEscape", screen.get_width(), screen.get_height())
        #self.menu.add.text_input('Name :', default='John Doe')
        #self.menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)])
        self.menu.add.button('Play', self.startLevel)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)
        self.menu.mainloop(self.screen)

    def startLevel(self):
        self.sceneManager.changeScene(Level())
        self.sceneManager.beginScene()

