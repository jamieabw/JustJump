from menu import Menu
import pygame_menu

class ShopMenu(Menu):
    def __init__(self, sceneManager):
        super().__init__(sceneManager)
        self.customTheme.title = True
        self.menu.set_title("Shop")

        self.menu.add.vertical_margin(80)
        self.menu.add.button('Exit', self.titleScreen)

    def startLevel(self):
        print("e")
        self.sceneManager.changeScene(self.sceneManager.Level)

    def titleScreen(self):
        self.sceneManager.changeScene(self.sceneManager.MainMenu)

