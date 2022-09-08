import pygame
import os
import time
import random
WIDTH, HEIGHT = 500, 500

# Ładowanie grafik broni i bonusów

BLUE_CHEESE = pygame.image.load(os.path.join("assets", "Blue_Cheese.png"))
YELLOW_CHEESE = pygame.image.load(os.path.join("assets", "Cheese.png"))
GREEN_CHEESE = pygame.image.load(os.path.join("assets", "Green_Cheese.png"))
GREY_CHEESE = pygame.image.load(os.path.join("assets", "Grey_Cheese.png"))
VIOLET_CHEESE = pygame.image.load(os.path.join("assets", "Violet_Cheese.png"))
RED_CHEESE = pygame.image.load(os.path.join("assets", "Red_Cheese.png"))

BONUS_EXTRA_LIFE = pygame.image.load(os.path.join("assets", "extra_life1.png"))
BONUS_PLUS = pygame.image.load(os.path.join("assets", "plus.png"))

class Laser:
    def __init__(self,x,y,img):
        """
        Funkcja iniciująca klase Laserów
        """
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
    
    def draw(self,window):
        """
        Funkcja odpowiedzialna za ładowanie grafiki w odpowiednim miejscu
        """
        window.blit(self.img, (self.x, self.y))
    
    def move(self,vel):
        """
        Funkcja odpowiedzialna za ruch bronią
        """
        self.y += vel

    def move_boss_laser(self,vel,obj):
        """
        Funkcja odpowiedzialna za ruch broni bossów
        """
        if obj.x < 175:
            self.y += vel
            self.x += int(vel/2)
        if 175 <= obj.x < 315:
            self.y += vel
        if obj.x >= 315:
            self.y += vel
            self.x -= int(vel/2)

    def off_screen(self, height):
        """
        Funkcja sprawdzająca czy broń znajduję się poza ekranem
        """
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        """
        Funkcja sprawdzająca kolizje z obiektem
        """
        return collide(self,obj)

class Bonus(Laser):
    def __init__(self,x,y,img):
        """
        Klasa Bonusu - zawiera wszystkie atrybuty z klasy Laser
        """
        super().__init__(x,y,img)
        self.mask = pygame.mask.from_surface(self.img)

def collide(obj1, obj2):
    """
    Funkcja sprawdzająca kolizje obiektów
    """
    col_x = int(obj2.x - obj1.x)
    col_y = int(obj2.y - obj1.y)
    return obj1.mask.overlap(obj2.mask,(col_x,col_y)) != None




