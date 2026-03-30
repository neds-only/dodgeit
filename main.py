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
#make the loop for pygame to keep repeating the screen+then add the option to close the loop
running=True
x = 0
y = 370
ox=0
oy=0
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
    if oy>600:
        ox= random.randint(0, 800)
        oy=0
    ro=pygame.Rect(ox,oy,40,40)#rect should be 'Rect' V.IMP
    rp=pygame.Rect(x,y,130,130)
    if rp.colliderect(ro):
        print('HIT')
pygame.quit()









