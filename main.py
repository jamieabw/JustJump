from pygame import init
from mainMenu import MainMenu
from sceneManager import SceneManager
from deathMenu import DeathMenu
from shopMenu import ShopMenu
from level import Level

def main():
    init()
    manager = SceneManager(MainMenu, Level, MainMenu, DeathMenu, ShopMenu)
    manager.run()

if __name__ == "__main__":
    main()

"""
features to add:
- weapon
- coins
- upgrades through shop
- particle system?
- audio
- high score
BUG: when jumping on the exit it double increments the level counter, no idea why
"""