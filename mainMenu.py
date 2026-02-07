import pygame
import pygame_menu
from level import Level
from menu import Menu


class MainMenu(Menu):
    def __init__(self, sceneManager):
        self.Level = Level
        super().__init__(sceneManager)
        self.menu.add.label(
            "TimEscape",
            font_name=self.font,
            font_size=50,
            align=pygame_menu.locals.ALIGN_CENTER
        )

        self.menu.add.vertical_margin(80)
        self.menu.add.button('Play', self.startLevel)
        self.menu.add.button('Shop', self.startShop)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)
        #self.menu.mainloop(self.screen)

    def startLevel(self):
        print("e")
        self.sceneManager.changeScene(self.sceneManager.Level)

    def startShop(self):
        self.sceneManager.changeScene(self.sceneManager.ShopMenu)

