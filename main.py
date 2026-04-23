#initiate pygame
import pygame
import random
pygame.init()
#set the screen and background
screen=pygame.display.set_mode((800,600))
#load the background then change its size
background=pygame.image.load('assets/background1.png')
background=pygame.transform.scale(background,(800,600))
#load the image of the player and transform the size
player=pygame.image.load('assets/char1.png')
player=pygame.transform.scale(player,(130,130))
font1 = pygame.font.Font(None, 100)
font = pygame.font.Font(None, 40)
#make the loop for pygame to keep repeating the screen+then add the option to close the loop
running=True
x = 0
y = 383
ox=400
oy=0
a=0
gameloop = 'playing'
while running:
        for i in pygame.event.get():
                if i.type == pygame.QUIT:
                        running = False
                if i.type==pygame.KEYDOWN:
                        if gameloop=='game over':
                                if i.key == pygame.K_r:
                                        gameloop = 'playing'
                                        x = 0
                                        y = 383
                                        ox = 400
                                        oy = 0
                                        a = 0
        screen.blit(background, (0, 0))
        # pygame.key.get_pressed--gives a list of boolean values eg-[True,False,True] and pygame.k_const
        # is the index for which it acesses the list.
        if gameloop == 'playing':
                key = pygame.key.get_pressed()
                if key[pygame.K_LEFT]:
                        x -= 5
                # dont try to change key[pygame.K_const] its an unchangable value we can only control the movement
                if key[pygame.K_RIGHT]:
                        x += 5
                x = min(670, max(0, x))
                screen.blit(player, (x, y))
                oy += 8
                pygame.draw.rect(screen, 'purple', (ox, oy, 40, 40))
                if oy > 600:
                        ox = random.randint(0, 760)
                        oy = 0
                        a += 1
                text1 = font.render('score:' + str(a), True, 'red')
                screen.blit(text1, (0, 0))
                ro = pygame.Rect(ox, oy, 40, 40)  # rect should be 'Rect' V.IMP
                rp = pygame.Rect(x, y, 100, 100)
                if rp.colliderect(ro):
                        gameloop = 'game over'
        elif gameloop == 'game over':
                text = font1.render('game over', True, 'purple')
                text2 = font.render('press R to restart', True, 'red')
                screen.blit(text2, (255, 300))
                screen.blit(text, (200, 240))
        pygame.display.update()
pygame.quit()



