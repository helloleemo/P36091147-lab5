import pygame
import os

MENU_IMAGE = pygame.image.load(os.path.join("images", "upgrade_menu.png"))
UPGRADE_IMAGE = pygame.image.load(os.path.join("images", "upgrade.png"))
SELL_IMAGE = pygame.image.load(os.path.join("images", "sell.png"))
ENEMY_IMAGE = pygame.image.load(os.path.join("images", "enemy.png"))


class UpgradeMenu:
    def __init__(self, x, y):

        self.image = pygame.transform.scale(MENU_IMAGE, (200, 200))
        self.upgrade_image = pygame.transform.scale(UPGRADE_IMAGE, (60, 40))
        self.sell_image = pygame.transform.scale(SELL_IMAGE, (40, 40))                               
        self.rect=self.image.get_rect()
        self.rect.center = (x, y)                      
        # (Q2) Add buttons here 
        self.__buttons = [Button(self.upgrade_image,"upgrade",x,y-70),Button(self.sell_image,"sell",x,y+70)] 

        

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.image,self.rect)
        # draw button
        # (Q2) Draw buttons here
        for btn in self.__buttons:
            win.blit(btn.image,btn.rect)


    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons


class Button:
    def __init__(self, image, name, x, y):
        self.name = name
        self.image = image
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)

    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """

        if(self.rect.collidepoint(x, y)):
            return True
        else:
            return False

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name






