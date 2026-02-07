from pygame import init
from mainMenu import MainMenu
from sceneManager import SceneManager
from deathMenu import DeathMenu
from shopMenu import ShopMenu
from level import Level

def main(debug=False):
    init()
    manager = SceneManager(MainMenu, Level, MainMenu, DeathMenu, ShopMenu)
    manager.run()

if __name__ == "__main__":
    main()

# broken map seeds:
# 6065102 weird vertical islands
#
#
"""
potential idea to incorporate the inaccesibility of some islands as a feature of the game and to have a "multijump" ability
purchasable in the shop for a large amount which is similar to the debugging jumping mechanism

"""