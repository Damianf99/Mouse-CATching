import pygame
import os
import time
import random

WIDTH, HEIGHT = 500, 500

# Ładowanie grafik zwykłych mysz
BOSS1 = pygame.image.load(os.path.join("assets", "boss1.png"))
BOSS2 = pygame.image.load(os.path.join("assets", "boss2.png"))
BOSS3 = pygame.image.load(os.path.join("assets", "boss3.png"))
BOSS4 = pygame.image.load(os.path.join("assets", "boss4.png"))
BOSS5 = pygame.image.load(os.path.join("assets", "boss5.png"))

# Ładowanie grafiki gracza

PLAYER = pygame.image.load(os.path.join("assets", "kotek.png"))

# Ładowanie grafik broni i bonusów

BLUE_CHEESE = pygame.image.load(os.path.join("assets", "Blue_Cheese.png"))
YELLOW_CHEESE = pygame.image.load(os.path.join("assets", "Cheese.png"))
GREEN_CHEESE = pygame.image.load(os.path.join("assets", "Green_Cheese.png"))
GREY_CHEESE = pygame.image.load(os.path.join("assets", "Grey_Cheese.png"))
VIOLET_CHEESE = pygame.image.load(os.path.join("assets", "Violet_Cheese.png"))
RED_CHEESE = pygame.image.load(os.path.join("assets", "Red_Cheese.png"))

BONUS_EXTRA_LIFE = pygame.image.load(os.path.join("assets", "extra_life1.png"))
BONUS_PLUS = pygame.image.load(os.path.join("assets", "plus.png"))


class Ship:

    def __init__(self,x,y,health=100):
        """
        Główna klasa odpowiedzialna za myszy, bossy i gracza
        """
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.cool_down_counter = 0
        self.lasers = []
        self.bonuses = []
        self.effects = []
        self.COOLDOWN = 60
        self.bonus_type = 1

    def draw(self, window):
        """
        Funkcja odpowiedzialna za ładowanie grafik obiektów, broni i bonusów
        """
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)
        for bonus in self.bonuses:
            bonus.draw(window)

    def move_lasers(self,vel,obj):
        """
        Funkcja odpowiedzialna za poruszanie bronią
        """
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)
    
    def move_bonuses(self,vel,obj):
        """
        Funkcja odpowiedzialna za poruszanie bonusami
        """
        self.cooldown()
        for bonus in self.bonuses:
            bonus.move(vel)
            if bonus.off_screen(HEIGHT):
                self.bonuses.remove(bonus)
            elif bonus.collision(obj):
                bonus_health = random.randint(1,obj.max_health*0.2)
                if obj.health == obj.max_health:
                    if self.bonus_type == 2:
                        obj.lives += 1
                    self.bonuses.remove(bonus)
                    return
                else:
                    if self.bonus_type == 2:
                        obj.lives += 1
                    if self.bonus_type == 1:
                        while obj.health <= obj.max_health:
                            if obj.health + bonus_health <= obj.max_health:
                                obj.health += bonus_health
                                break
                            else:
                                bonus_health = random.randint(1,obj.max_health*0.2)
                    self.bonuses.remove(bonus)

    def cooldown(self):
        """
        Funkcja odpowiadająca za czas w którym można oddać strzał
        """
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        """
        Funkcja odpowiedzialna za tworzenie strzału
        """
        if self.cool_down_counter == 0:
            laser = Lasery.Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self,x,y,health=100):
        """
        Klasa gracza
        """
        super().__init__(x,y,health)
        self.ship_img = PLAYER
        self.laser_img = pygame.image.load(os.path.join("assets","light_blast.png"))
        self.lasers = []
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        self.attack = 10
        self.name = ""
        self.level = 0
        self.score = 0
        self.gold = 0
        self.lives = 3
        self.velocity = 5
        self.laser_velocity = 5
        self.COOLDOWN = 30

    def move_lasers(self,vel,objs):
        """
        Funkcja odpowiedzialna za poruszanie bronią
        """
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        obj.health -= self.attack
                        if laser in self.lasers:
                            self.lasers.remove(laser)
                        if obj.health <= 0:
                            if obj.boss == True:
                                self.gold += random.randint(self.level*50,125*self.level)
                            objs.remove(obj)
                            self.gold += random.randint(25,50)
                            self.score += random.randint(self.level*10,25*self.level)
                            if laser in self.lasers:
                                self.lasers.remove(laser)

    def draw(self,window):
        """
        Funkcja rysująca statek gracza oraz broni i paska życia
        """
        super().draw(window)
        self.healthbar(window)

    def healthbar(self,window):
        """
        Funkcja tworząca pasek życia
        """
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))

class Enemy(Ship):
    #Mapa wyboru myszy
    COLOR_MAP = {
                "grey": (BOSS1, GREY_CHEESE),
                "violet": (BOSS2, VIOLET_CHEESE),
                "blue": (BOSS3, BLUE_CHEESE),
                "red": (BOSS4, RED_CHEESE),
                "yellow": (BOSS5, YELLOW_CHEESE)
                }

    def __init__(self,x,y,color,health=0):
        """
        Klasa przeciwników
        """
        super().__init__(x,y,health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.flag = 1
        self.max_health = health
        self.COOLDOWN = 30
        self.boss = False

    def move(self, vel):
        """
        Funkcja odpowiedzialna za poruszanie się przeciwników
        """
        if self.y < 100:
            self.y += vel
        if self.flag == 1:
            self.x += vel
            if self.x > WIDTH - 50:
                self.flag = 0
        if self.flag == 0:
            self.x -= vel
            if self.x < 0:
                self.flag = 1

    def shoot(self):
        """
        Funkcja tworząca strzał
        """
        if self.cool_down_counter == 0:
            laser = Lasery.Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def shoot_bonus(self):
        """
        Funkcja tworząca bonus
        """
        if self.cool_down_counter == 0:
            bonus = Lasery.Bonus(self.x, self.y, BONUS_PLUS)
            self.bonuses.append(bonus)
            self.cool_down_counter = 1

    def draw(self,window):
        """
        Funkcja odpowiedzialna za rysowanie myszy, broni, bonusów i pasku życia
        """
        super().draw(window)
        self.healthbar(window)

    def healthbar(self,window):
        """
        Funkcja tworząca pasek życia
        """
        pygame.draw.rect(window, (255,0,0), (self.x + 22, self.y + self.ship_img.get_height() - 25, self.ship_img.get_width()/2, 5))
        pygame.draw.rect(window, (0,255,0), (self.x + 22, self.y + self.ship_img.get_height() - 25, self.ship_img.get_width() * (self.health/self.max_health)/2, 5))

class Boss(Ship):
    def __init__(self,x,y):
        """
        Klasa bossów
        """
        super().__init__(x,y)
        self.health = 1000
        self.attack = 20
        self.ship_img = pygame.image.load(os.path.join("assets","bigboss.png"))
        self.laser_img = pygame.image.load(os.path.join("assets","frozen_starlight.png"))
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = self.health
        self.boss = True
        self.flag = 1
        self.velocity = 2
        self.laser_velocity = 6
        self.COOLDOWN = 30

    def move(self, vel):
        """
        Funkcja odpowiedzialna za poruszanie bossów
        """
        if self.y < 100:
            self.y += vel
        if self.flag == 1:
            self.x += vel
            if self.x > WIDTH + 50:
                self.flag = 0
        if self.flag == 0:
            self.x -= vel
            if self.x < -150:
                self.flag = 1

    def shoot(self):
        """
        Funkcja tworząca strzał
        """
        if self.cool_down_counter == 0:
            laser = Lasery.Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def shoot_bonus(self):
        """
        Funkcja tworząca bonusy
        """
        if self.cool_down_counter == 0:
            bonus = Lasery.Bonus(self.x, self.y, BONUS_PLUS)
            if self.bonus_type == 2:
                bonus.img = BONUS_EXTRA_LIFE
            self.bonuses.append(bonus)
            self.cool_down_counter = 1

    def bonus_list_size(self):
        return len(self.bonuses)

    def move_lasers(self,vel,obj):
        """
        Funkcja odpowiedzialna za poruszanie bronią
        """
        self.cooldown()
        for laser in self.lasers:
            laser.move_boss_laser(vel,self)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= self.attack
                self.lasers.remove(laser)

    def draw(self,window):
        """
        Funkcja rysująca bossa, broń, bonusy i pasek życia
        """
        super().draw(window)
        self.healthbar(window)

    def healthbar(self,window):
        """
        Funkcja tworząca pasek życia
        """
        pygame.draw.rect(window, (255,0,0), (self.x + 22, self.y + self.ship_img.get_height(), self.ship_img.get_width()/2, 5))
        pygame.draw.rect(window, (0,255,0), (self.x + 22, self.y + self.ship_img.get_height(), self.ship_img.get_width() * (self.health/self.max_health)/2, 5))

def Ships_main(Lasers):
    """
    Funkcja przejmująca moduł Laserów
    """
    global Lasery
    Lasery = Lasers

def collide(obj1, obj2):
    """
    Funkcja sprawdzająca kolizje obiektów
    """
    col_x = int(obj2.x - obj1.x)
    col_y = int(obj2.y - obj1.y)
    return obj1.mask.overlap(obj2.mask,(col_x,col_y)) != None




