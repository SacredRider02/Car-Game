import pygame
from random import randint

pygame.init()

winwidth = 424
winheight = 754
win = pygame.display.set_mode((winwidth, winheight))

bg = pygame.image.load('road texture_img.jpg')
pl_car = pygame.image.load('pl_car.png')
en2 = pygame.image.load('en2.png')

font = pygame.font.SysFont('Comicsans', 100, True)
font2 = pygame.font.SysFont('Comicsans', 30, True)
gmText = font.render('Game Over!', 1, (255, 0, 0))

clock = pygame.time.Clock()


class Car:
    def __init__(self, x, y, width, height):
        self.width = 67
        self.height = 150
        self.x = x
        self.y = y
        self.vel = 10

    def draw(self, win):
        win.blit(pl_car, (self.x, self.y))


car = Car(181, 550, 20, 40)


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 65
        self.height = 129
        self.vel = 3

    def draw(self, win):
        win.blit(en2, (self.x, self.y))

a = randint(20, 349)
enemy = Enemy(a, 0)

timeCount = 600


def frameFormat():
    win.blit(bg, (0, 0))
    car.draw(win)
    scr = font2.render('Score: ' + str(score), 1, (0, 0, 254))
    win.blit(scr, (310, 20))
    for bullet in bullets:
        bullet.draw(win)
        timeCount = 30
    pygame.display.update()

bullets = []
score = 0

run = True
while run:
    clock.tick(30)
    a = randint(20, 349)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if timeCount % 60 == 0:
        bullets.append(Enemy(a, 0))

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.y += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    for enemy in bullets:
        if (car.x + 69 >= enemy.x and enemy.x + 65 >= car.x and
                enemy.y <= car.y + 150 and enemy.y + enemy.height >= car.y + 10):
            i = 0
            score = 0
            while i < 300:
                pygame.time.delay(10)
                i += 1
                car.x = 181
                bullets.clear()
                if keys[pygame.K_SPACE]:
                    i = 301
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        if car.x <= 349:
            car.x += 5
    if keys[pygame.K_LEFT]:
        if car.x >= 0:
            car.x -= 5

    score += 1
    if score % 50 == 0:
        for enemy in bullets:
            enemy.vel += 1
    timeCount -= 1
    frameFormat()


pygame.quit()
