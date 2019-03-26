import pygame
pygame.init()
running = True
gameWon = False

#Window Parameters
winSize = 700
win = pygame.display.set_mode((winSize,winSize))

#Caption
pygame.display.set_caption("Psychalaga!")

#Import images
ship_s = pygame.image.load('images/ship_stationary.png')
meteor = pygame.image.load('images/meteor2.png')
game_over = pygame.image.load('images/gameover.png')
game_win = pygame.image.load('images/gamewin.png')
instructions = pygame.image.load('images/instructions.png')
menu = pygame.image.load('images/menu.png')

stage1 = pygame.image.load('images/stage1.png')
stage2 = pygame.image.load('images/stage2.png')
stage3 = pygame.image.load('images/stage3.png')
stage4 = pygame.image.load('images/stage4.png')
stage5 = pygame.image.load('images/stage5.png')
stage6 = pygame.image.load('images/stage6.png')
stage7 = pygame.image.load('images/stage7.png')
stage8 = pygame.image.load('images/stage8.png')

#Velocities
playerVel = 10
bulletVel = 2
enemyVel = .5


class player(object):
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.vel = playerVel
        self.right = False
        self.left = False

    def draw(self, win):
        win.blit(ship_s, (self.x, self.y))

class projectile(object):
    def __init__(self,x, y):
        self.width = 5
        self.height = 15
        self.x = x
        self.y = y
        self.vel = bulletVel
        
    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))

class enemy(object):
    def __init__(self,x , y):
        self.width = 30
        self.height = 60
        self.x = x
        self.y = y
        self.vel = enemyVel

    def draw(self, win):
        win.blit(meteor, (self.x, self.y, self.width, self.height))

    def move(self):
        self.y += self.vel

class health(object):
    def __init__(self, health):
        self.health = health

    def draw(self, win):
        if(self.health > 0):
            pygame.draw.rect(win, (255, 225, 0) , (winSize - 107, winSize - 15, self.health, 10))

    def hurt(self):    
        self.health -= 10
            
        
        
def redrawGameWindow():
    win.fill((0, 0, 0))

    
    for bullet in bullets:
        bullet.draw(win)
    player.draw(win)
    for enemy in enemies:
        enemy.draw(win)

    if stage == 1:
        win.blit(stage1, (10, 10, 100, 20))
    if stage == 2:
        win.blit(stage2, (10, 10, 100, 20))
    if stage == 3:
        win.blit(stage3, (10, 10, 100, 20))
    if stage == 4:
        win.blit(stage4, (10, 10, 100, 20))
    if stage == 5:
        win.blit(stage5, (10, 10, 100, 20))
    if stage == 6:
        win.blit(stage6, (10, 10, 100, 20))
    if stage == 7:
        win.blit(stage7, (10, 10, 100, 20))
    if stage == 8:
        win.blit(stage8, (10, 10, 100, 20))


    pHealth.draw(win)
    pygame.display.update()


x = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if x:
        x = False
        win.blit(menu, (0, 0))
        
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RETURN]:
        running = False
    elif keys[pygame.K_i]:
        win.blit(instructions, (0, 0))
    elif keys[pygame.K_BACKSPACE]:
        win.blit(menu, (0, 0))
    

    pygame.display.update()
    

running = True


clock = pygame.time.Clock()

bullets = []
enemies = []
player = player(100, 100, winSize/2 - 40, winSize - 120)

pHealth = health(102)

gameCount = 0
stage = 1

while running:
    clock.tick(1000)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for bullet in bullets:
        if bullet.y < winSize and bullet.y > 0:
            bullet.y -= bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    
    if stage == 1:
        if gameCount == 0:
            enemies.append(enemy(200, 0))
            
        if gameCount == 3000:
            enemies.append(enemy(600, 0))
            
        if gameCount == 6000:
            enemies.append(enemy(400, 0))
            
        if gameCount == 9000:
            enemies.append(enemy(400, 0))
            
        if gameCount == 10000:
            enemies.append(enemy(500, 0))
            
        if gameCount == 13000:
             gameCount = -1
             stage += 1

    if stage == 2:
        if gameCount == 0:
            enemies.append(enemy(200, 0))
            
        if gameCount == 1000:
            enemies.append(enemy(400, 0))
            
        if gameCount == 3000:
            enemies.append(enemy(600, 0))
            
        if gameCount == 5000:
            enemies.append(enemy(130, 0))
            
        if gameCount == 6000:
            enemies.append(enemy(400, 0))
            
        if gameCount == 8000:
            enemies.append(enemy(100, 0))
            
        if gameCount == 10000:
            enemies.append(enemy(500, 0))
            
        if gameCount == 13000:
             gameCount = -1
             stage += 1

    if stage == 3:
        if gameCount == 0:
            enemies.append(enemy(200, 0))
            
        if gameCount == 1000:
            enemies.append(enemy(400, 0))
            
        if gameCount == 3000:
            enemies.append(enemy(600, 0))
            
        if gameCount == 4000:
            enemies.append(enemy(200, 0))
            enemies.append(enemy(400, 0))
            
        if gameCount == 5000:
            enemies.append(enemy(130, 0))
            
        if gameCount == 6000:
            enemies.append(enemy(400, 0))
            
        if gameCount == 8000:
            enemies.append(enemy(100, 0))
            enemies.append(enemy(400, 0))
            
        if gameCount == 10000:
            enemies.append(enemy(500, 0))
            
        if gameCount == 13000:
             gameCount = -1
             stage += 1

    if stage == 4:
        if gameCount == 0:
            enemies.append(enemy(200, 0))
            enemies.append(enemy(400, 0))
            
        if gameCount == 1000:
            enemies.append(enemy(400, 0))
            
        if gameCount == 2000:
            enemies.append(enemy(200, 0))
            
        if gameCount == 3000:
            enemies.append(enemy(600, 0))
            enemies.append(enemy(400, 0))
            
        if gameCount == 4000:
            enemies.append(enemy(100, 0))
            
        if gameCount == 5000:
            enemies.append(enemy(130, 0))
            enemies.append(enemy(400, 0))
            
        if gameCount == 6000:
            enemies.append(enemy(400, 0))
            
        if gameCount == 7000:
            enemies.append(enemy(200, 0))
            
        if gameCount == 8000:
            enemies.append(enemy(100, 0))
            
        if gameCount == 9000:
            enemies.append(enemy(430, 0))
            
        if gameCount == 10000:
            enemies.append(enemy(500, 0))
            
        if gameCount == 13000:
             gameCount = -1
             stage += 1

    if stage == 5:
        if gameCount == 0:
            enemies.append(enemy(200, 0))

        if gameCount == 1000:
            enemies.append(enemy(600, 0))

        if gameCount == 2000:
            enemies.append(enemy(300, 0))
            
        if gameCount == 3000:
            enemies.append(enemy(200, 0))

        if gameCount == 4000:
            enemies.append(enemy(430, 0))
            enemies.append(enemy(530, 0))

        if gameCount == 5000:
            enemies.append(enemy(100, 0))
            
        if gameCount == 6000:
            enemies.append(enemy(250, 0))

        if gameCount == 7000:
            enemies.append(enemy(500, 0))
            enemies.append(enemy(300, 0))

        if gameCount == 8000:
            enemies.append(enemy(475, 0))
            
        if gameCount == 9000:
            enemies.append(enemy(300, 0))
            
        if gameCount == 10000:
            enemies.append(enemy(100, 0))
            enemies.append(enemy(230, 0))
            
        if gameCount == 13000:
             gameCount = -1
             stage += 1

    if stage == 6:
        if gameCount == 0:
            enemies.append(enemy(100, 0))

        if gameCount == 1000:
            enemies.append(enemy(300, 0))

        if gameCount == 2000:
            enemies.append(enemy(200, 0))
            
        if gameCount == 3000:
            enemies.append(enemy(400, 0))

        if gameCount == 4000:
            enemies.append(enemy(300, 0))
            enemies.append(enemy(200, 0))

        if gameCount == 5000:
            enemies.append(enemy(500, 0))
            
        if gameCount == 6000:
            enemies.append(enemy(200, 0))

        if gameCount == 7000:
            enemies.append(enemy(200, 0))
            enemies.append(enemy(400, 0))

        if gameCount == 8000:
            enemies.append(enemy(100, 0))
            
        if gameCount == 9000:
            enemies.append(enemy(300, 0))
            
        if gameCount == 10000:
            enemies.append(enemy(500, 0))
            enemies.append(enemy(600, 0))
            
        if gameCount == 13000:
             gameCount = -1
             stage += 1


    if stage == 7:
        if gameCount == 0:
            enemies.append(enemy(200, 0))

        if gameCount == 1000:
            enemies.append(enemy(600, 0))

        if gameCount == 2000:
            enemies.append(enemy(300, 0))
            
        if gameCount == 3000:
            enemies.append(enemy(200, 0))

        if gameCount == 4000:
            enemies.append(enemy(430, 0))
            enemies.append(enemy(530, 0))

        if gameCount == 5000:
            enemies.append(enemy(100, 0))
            
        if gameCount == 6000:
            enemies.append(enemy(250, 0))

        if gameCount == 7000:
            enemies.append(enemy(500, 0))
            enemies.append(enemy(300, 0))

        if gameCount == 8000:
            enemies.append(enemy(475, 0))
            
        if gameCount == 9000:
            enemies.append(enemy(300, 0))
            
        if gameCount == 10000:
            enemies.append(enemy(100, 0))
            enemies.append(enemy(230, 0))
            
        if gameCount == 13000:
             gameCount = -1
             stage += 1


    if stage == 8:
        if gameCount == 0:
            enemies.append(enemy(400, 0))

        if gameCount == 1000:
            enemies.append(enemy(600, 0))
            enemies.append(enemy(500, 0))

        if gameCount == 2000:
            enemies.append(enemy(350, 0))
            
        if gameCount == 3000:
            enemies.append(enemy(300, 0))

        if gameCount == 4000:
            enemies.append(enemy(100, 0))
            enemies.append(enemy(250, 0))

        if gameCount == 5000:
            enemies.append(enemy(300, 0))
            
        if gameCount == 6000:
            enemies.append(enemy(500, 0))

        if gameCount == 7000:
            enemies.append(enemy(100, 0))
            enemies.append(enemy(300, 0))

        if gameCount == 8000:
            enemies.append(enemy(200, 0))
            
        if gameCount == 9000:
            enemies.append(enemy(400, 0))
            
        if gameCount == 10000:
            enemies.append(enemy(100, 0))
            enemies.append(enemy(230, 0))
            
        if gameCount == 13000:
             running = False
             gameWon = True
     
    for en in enemies:
        if en.y > winSize:
            pHealth.hurt()
            enemies.pop(enemies.index(en))
        elif(en.x + en.width//2 >= player.x and en.x + en.width//2 <= player.x + player.width) and en.y > player.y:
            pHealth.hurt()
            enemies.pop(enemies.index(en))
        else:
            en.move()

    for en in enemies:
        for bullet in bullets:
            if(bullet.x + bullet.width//2 >= en.x and bullet.x + bullet.width//2 <= en.x + en.width) and bullet.y < en.y :
                bullets.pop(bullets.index(bullet))
                enemies.pop(enemies.index(en))


    #KEY INPUTS
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if len(bullets) < 1:
            bullets.append(projectile(round(player.x + player.width //2 - 2.5), round(player.y + player.height //2)))
    
    if keys[pygame.K_a] and player.x > 0:
        player.x -= player.vel
        player.right = False
        player.left = True
    elif keys[pygame.K_d] and player.x + player.width < winSize:
        player.x += player.vel
        player.right = True
        player.left = False
    elif keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player.vel
        player.right = False
        player.left = True
    elif keys[pygame.K_RIGHT] and player.x + player.width < winSize:
        player.x += player.vel
        player.right = True
        player.left = False
    else:
        player.right = False
        player.left = False
    
    gameCount += 1

    if(pHealth.health < 0):
        running = False
        
    redrawGameWindow()

running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if gameWon:
        win.blit(game_win, (0, 0))
    else:
        win.blit(game_over, (0, 0))

    pygame.display.update()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RETURN]:
        running = False

pygame.quit()
