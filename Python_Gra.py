import pygame
import os
import time
import random
from gui_gra import Ships, Lasers, gui, First_weapon, Store_4, Save_name
pygame.font.init()

Ships.Ships_main(Lasers)

# Zadeklarowanie oraz załadowanie szerokości i wysokości programu
WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Mouse CATching")

# Ładowanie grafik zwykłych myszy
BOSS1 = pygame.image.load(os.path.join("assets", "boss1.png"))
BOSS2 = pygame.image.load(os.path.join("assets", "boss2.png"))
BOSS3 = pygame.image.load(os.path.join("assets", "boss3.png"))
BOSS4 = pygame.image.load(os.path.join("assets", "boss4.png"))
BOSS5 = pygame.image.load(os.path.join("assets", "boss5.png"))

# Ładowanie grafiki gracza

PLAYER = pygame.image.load(os.path.join("assets", "kotek.png"))

# Ładowanie tła

BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "tlo.png")), (WIDTH,HEIGHT))

def collide(obj1, obj2):
    """
    Funkcja sprawdzająca kolizje obiektów
    """
    col_x = int(obj2.x - obj1.x)
    col_y = int(obj2.y - obj1.y)
    return obj1.mask.overlap(obj2.mask,(col_x,col_y)) != None

def main(run):
    """
    Funkcja trzymająca główną pętle programu
    """
    FPS = 200
    global next_level
    next_level = 1
    main_font = pygame.font.SysFont("ansifixed", 40)
    lost_font = pygame.font.SysFont("ansifixed", 60)

    enemies = []
    wave_length = 5
    enemy_vel = 1
    enemy_laser_vel = 5
    enemy_type = 0

    player = Ships.Player(WIDTH/2 - 50, HEIGHT - int(PLAYER.get_height()) - 25)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    if run[0]:
        First_weapon.change_player(player)

    def redraw_window():
        """
        Funkcja odpowiedzialna za odświeżanie ekranu
        """
        WIN.blit(BG, (0,0))
        # Tworzenie tekstu do środka gry
        lives_label = main_font.render(f"Lives: {player.lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {player.level}", 1, (255,255,255))
        score_label = main_font.render(f"Score: {player.score}", 1, (255,255,255))
        gold_label = main_font.render(f"Gold: {player.gold}", 1, (255,255,255))

        global acces, next_level
        if (player.level%5 == 0 and player.level != 0) and acces == 1:
            time.sleep(1)
            Store_4.store_4(player)
            acces = 2
            redraw_window()

        WIN.blit(lives_label, (10, 10))
        WIN.blit(gold_label, (10, 10 + int(lives_label.get_height()) + 5))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        WIN.blit(score_label, (WIDTH - score_label.get_width() - 10, 10 + int(level_label.get_height()) + 5))

        if next_level == player.level:
            if player.level%5 == 4:
                acces = 1
            for enemy in enemies:
                enemy.health += 10*player.level
                enemy.max_health = enemy.health
            next_level = player.level + 1

        for enemy in enemies:
            enemy.draw(WIN)

        for boss in enemies:
            boss.draw(WIN)

        player.draw(WIN)

        if lost:
            if player.level <= 30:
                NBG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "gameover1.png")), (WIDTH,HEIGHT))
            elif player.level > 30:
                NBG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "gameover.png")), (WIDTH,HEIGHT))
            WIN.blit(NBG, (0,0))

        pygame.display.update()
    #Główna pętla
    while run[0]:
        clock.tick(FPS)
        redraw_window()

        if player.health <= 0 and player.lives > 0:
            player.lives -= 1
            player.health = player.max_health

        if player.lives <= 0 or player.level > 30:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS/2:
                Save_name.save_name(player)
                run[0] = False
            else:
                continue
        if player.level %5 != 4 or player.level == 0:
            if len(enemies) == 0:
                enemy_type = 1
                player.level += 1
                wave_length += 3
                for i in range(wave_length):
                    enemy = Ships.Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500*int((player.level+4)/5), int(-100*int((player.level+4)/5))), random.choice(["red", "blue", "yellow", "grey", "violet"]))
                    enemies.append(enemy)
        
        #Tworzenie bossa co 5 poziomów
        if player.level %5 == 4 and player.level != 0:
            if len(enemies) == 0:
                enemy_type = 2
                player.level += 1
                boss = Ships.Boss(WIDTH/2, -HEIGHT)
                if player.level %5 == 0 and player.level != 5:
                    boss.health *= (player.level/5)
                    boss.attack += player.level
                    boss.max_health = boss.health
                if player.level == 10:
                    boss.ship_img = pygame.image.load(os.path.join("assets","bb2.png"))
                    boss.laser_img = pygame.image.load(os.path.join("assets","Red_Sapphire.png"))
                if player.level == 15:
                    boss.ship_img = pygame.image.load(os.path.join("assets","bb3.png"))
                    boss.laser_img = pygame.image.load(os.path.join("assets","Falcon_Blue_Eye.png"))
                if player.level == 20:
                    boss.ship_img = pygame.image.load(os.path.join("assets","bb4.png"))
                    boss.laser_img = pygame.image.load(os.path.join("assets","Violet_Gem.png"))
                if player.level == 25:
                    boss.ship_img = pygame.image.load(os.path.join("assets","bb5.png"))
                    boss.laser_img = pygame.image.load(os.path.join("assets","Mistic_Ball_.png"))
                if player.level == 30:
                    boss.ship_img = pygame.image.load(os.path.join("assets","bb6.png"))
                    boss.laser_img = pygame.image.load(os.path.join("assets","Mistic_Violet_Ball_.png"))
                enemies.append(boss)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run[0] = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x > 0: # lewa strona
            player.x -= player.velocity
        if keys[pygame.K_d] and player.x + player.velocity + player.get_width() - 10 < WIDTH: # prawa strona
            player.x += player.velocity
        if keys[pygame.K_SPACE]:
            player.shoot()

        if enemy_type == 1:
            for enemy in enemies[:]:
                enemy.move(enemy_vel)
                enemy.move_lasers(enemy_laser_vel, player)
                enemy.move_bonuses(enemy_laser_vel, player)

                if random.randrange(0, 2*60) == 1:
                    enemy.shoot()

                if random.randrange(0, 5*60) == 1:
                    enemy.bonus_type = 1
                    enemy.shoot_bonus()

                if collide(enemy, player):
                    player.health -= 10
                    enemies.remove(enemy)

        if enemy_type == 2:
            for boss in enemies[:]:
                boss.move(boss.velocity)
                boss.move_lasers(boss.laser_velocity, player)
                boss.move_bonuses(boss.laser_velocity, player)

                if random.randrange(0, 2*60) == 1:
                    boss.shoot()

                if random.randrange(0, 2*60) == 1:
                    if boss.bonus_list_size() == 0:
                        bonus_chance = random.randrange(0, 2*60)
                        if bonus_chance < 60:
                            boss.bonus_type = 2
                            boss.shoot_bonus()
                        elif bonus_chance >= 60:
                            boss.bonus_type = 1
                            boss.shoot_bonus()

        player.move_lasers(-player.laser_velocity, enemies)

def main_menu():
    """
    Funkcja uruchamiająca program
    """
    title_font = pygame.font.SysFont("arial", 70)
    run = [True]
    global acces
    acces = 1
    while run[0]:
        WIN.blit(BG, (0,0))
        pygame.display.update()
        gui.run_gui(run)
        main(run)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run[0] = False
    pygame.display.quit()
    pygame.quit()
    exit()


main_menu()


