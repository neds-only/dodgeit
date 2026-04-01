#initiate pygame
import pygame
import time
import random
import pygame.display
pygame.init()
#set the screen and background
screen=pygame.display.set_mode((800,600))
#load the background then change its size
background=pygame.image.load('assets/background1.png')
background=pygame.transform.scale(background,(800,600))
#load the image of the player and transform the size
player=pygame.image.load('assets/char1.png')
player=pygame.transform.scale(player,(130,130))
#make the loop for pygame to keep repeating the screen+then add the option to close the loop
running=True
x = 0
y = 383
ox=0
oy=0
a=0
while running:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            running=False
    screen.blit(background, (0, 0))
#pygame.key.get_pressed--gives a list of boolean values eg-[True,False,True] and pygame.k_const
#is the index for which it acesses the list.
    key=pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        x-=5
#dont try to change key[pygame.K_const] its an unchangable value we can only control the movement
    if x <= 0:
        x = 0
    if key[pygame.K_RIGHT]:
        x+=5
    if x>=680:
        x=680
    screen.blit(player,(x,y))
    oy+=8
    pygame.draw.rect(screen,'purple',(ox,oy,40,40))
    pygame.display.update()
    font=pygame.font.Font(None,40)
    if oy>600:
        ox= random.randint(0, 800)
        oy=0
        a+=1
    text1 = font.render('score:' + str(a), True, 'red')
    screen.blit(text1, (0, 0))
    pygame.display.update()
    ro=pygame.Rect(ox,oy,20,20)#rect should be 'Rect' V.IMP
    rp=pygame.Rect(x,y,100,100)
    gameloop=False
    font1=pygame.font.Font(None,100)
    if rp.colliderect(ro):
        gameloop=True
    if gameloop==True:
        text=font1.render('game over',False,'purple')
        text2=font.render('press R to restart',True,'red')
        screen.blit(text2,(255,300))
        screen.blit(text,(200,240))
        pygame.display.update()
        time.sleep(5)
        running=False
pygame.quit()





