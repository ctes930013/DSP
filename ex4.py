# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 20:37:18 2016

@author: user
"""

#_*_ coding:utf-8 _*_
# bouncingcircle.py

import pygame, random, math, time, sys
from pygame.locals import *
from thinkdsp import *

pygame.init()

green = (0,255,0)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
bluegreen = (0,255,255)

pygame.mixer.init()

#radius = 20

size = 1200, 640
screen = pygame.display.set_mode((size))
screen.fill(black)
background = pygame.Surface(size)
background = background.convert()
background.fill(black)

class stony(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((30,30))
		color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
		pygame.draw.circle(self.image, color, (15,15), 15,0)
		self.rect = self.image.get_rect()
		self.rect.centerx = random.randrange(0,1200)
		self.rect.centery = random.randrange(0,640)
		self.dx = random.randrange(-45,50)
		self.dy = random.randrange(-45,50)
	def checkbound(self):
		if (self.rect.left <= 0 or self.rect.right >= screen.get_width()):
			self.dx *= -1
		if (self.rect.top <= 0 or self.rect.bottom >= screen.get_height()):
			self.dy *= -1
	def update(self):
		self.checkbound()
		self.rect.centerx += self.dx
		self.rect.centery += self.dy
	
#檢查是否有球和玩家發生撞擊
def checkhit(a,b,ra,rb):
    rb = math.sqrt(math.pow(rb,2)+math.pow(rb,2))
    xa = a.rect.centerx
    xb = b.centerx
    ya = a.rect.centery
    yb = b.centery
    hit = math.sqrt(math.pow((xb-xa),2)+math.pow((yb-ya),2))
    if(hit <= (ra+rb)):
        return True
    else:
        return False
        
#輸出文字
def printchar(chstr,fonts,color,x,y,size):
    pygame.font.get_fonts()
    font = pygame.font.Font(fonts,size)
    text = font.render('%s'%chstr,True,color)
    screen.blit(text,(x,y))

#輸出當前血量
def HP(count): 
    if count == 1:
        color = (155,255,45)
    elif count == 2:
        color = (100,75,235)
    elif count == 3:
        color = (165,205,200)
    elif count == 4:
        color = (80,215,180)
    elif count == 5:
        color = (255,0,0)
    else:
        color = (100,100,100)
    pygame.font.get_fonts()
    font = pygame.font.Font(None,22)
    text = font.render('%s'%count,True,color)
    screen.blit(text,(1140,40))               

shipimg = pygame.image.load("spaceship.png")
shipimg = shipimg.convert()
shipimg = pygame.transform.scale(shipimg, [50,50])
shipimg.set_colorkey((0,0,0))
shiprect = shipimg.get_rect()
shiprect.center = (600,580)

snow_list = []
for i in range(50):
    x = random.randrange(0, 1200)
    y = random.randrange(0, 640)
    snow_list.append([x, y])

b1 = stony()
b2 = stony()
b3 = stony()
b4 = stony()
b5 = stony()
b6 = stony()
allsprites = pygame.sprite.Group(b1, b2, b3, b4, b5, b6)
count = 5  #紀錄當前的血量
clock = pygame.time.Clock()
running = True
alien = pygame.mixer.Sound("alien.ogg")
alien.play(-1)
chstr = u"Time:"

#產生Pink雜音
signal = PinkNoise()
wave = signal.make_wave(duration=2,framerate=11025)
track = pygame.mixer.Sound("Pinknoise.ogg")
starttime = time.time()
while running:
    #清除螢幕
    screen.fill(black)
    endtime = time.time()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    for i in range(len(snow_list)):   
        # Draw the snow flake
        pygame.draw.circle(screen, white, snow_list[i], 2)
         
        # Move the snow flake down one pixel
        snow_list[i][1] += 1
         
        # If the snow flake has moved off the bottom of the screen
        if snow_list[i][1] > 640:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, 1200)
            snow_list[i][0] = x    
    
    outtime = round((endtime-starttime),2)
    HP(count)
    #me = unicode(outtime, "big5")
    printchar(chstr,None,green,1100,20,22)
    printchar(outtime,None,green,1150,20,22)  
    printchar("HP:",None,red,1100,40,22)
    printchar("/5",None,red,1150,40,22)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and shiprect.right < 1150:
        shiprect.centerx += 70
    if keys[pygame.K_LEFT] and shiprect.left > 50:
        shiprect.centerx -= 70 
    if keys[pygame.K_DOWN] and shiprect.bottom < 605:
        shiprect.centery += 70
    if keys[pygame.K_UP] and shiprect.top > 62:
        shiprect.centery -= 70    
    
    if pygame.sprite.collide_rect(b1, b2):
        b1.dx *= -1
        b1.dy *= -1
        b2.dx *= -1
        b2.dy *= -1
        track.play()
    if pygame.sprite.collide_rect(b1, b3):
        b1.dx *= -1
        b1.dy *= -1
        b3.dx *= -1
        b3.dy *= -1
        track.play()
    if pygame.sprite.collide_rect(b1, b4):
        b1.dx *= -1
        b1.dy *= -1
        b4.dx *= -1
        b4.dy *= -1
        track.play() 
    if pygame.sprite.collide_rect(b1, b5):
        b1.dx *= -1
        b1.dy *= -1
        b5.dx *= -1
        b5.dy *= -1
        track.play() 
    if pygame.sprite.collide_rect(b1, b6):
        b1.dx *= -1
        b1.dy *= -1
        b6.dx *= -1
        b6.dy *= -1
        track.play()     
    if pygame.sprite.collide_rect(b2, b3):
        b2.dx *= -1
        b2.dy *= -1
        b3.dx *= -1
        b3.dy *= -1		
        track.play() 
    if pygame.sprite.collide_rect(b2, b4):
        b2.dx *= -1
        b2.dy *= -1
        b4.dx *= -1
        b4.dy *= -1		
        track.play() 
    if pygame.sprite.collide_rect(b2, b5):
        b2.dx *= -1
        b2.dy *= -1
        b5.dx *= -1
        b5.dy *= -1		
        track.play()
    if pygame.sprite.collide_rect(b2, b6):
        b2.dx *= -1
        b2.dy *= -1
        b6.dx *= -1
        b6.dy *= -1		
        track.play()    
    if pygame.sprite.collide_rect(b3, b4):
        b3.dx *= -1
        b3.dy *= -1
        b4.dx *= -1
        b4.dy *= -1		
        track.play()
    if pygame.sprite.collide_rect(b3, b5):
        b3.dx *= -1
        b3.dy *= -1
        b5.dx *= -1
        b5.dy *= -1		
        track.play()
    if pygame.sprite.collide_rect(b3, b6):
        b3.dx *= -1
        b3.dy *= -1
        b6.dx *= -1
        b6.dy *= -1		
        track.play() 
    if pygame.sprite.collide_rect(b4, b5):
        b4.dx *= -1
        b4.dy *= -1
        b5.dx *= -1
        b5.dy *= -1		
        track.play()
    if pygame.sprite.collide_rect(b4, b6):
        b4.dx *= -1
        b4.dy *= -1
        b6.dx *= -1
        b6.dy *= -1		
        track.play()
    if pygame.sprite.collide_rect(b5, b6):
        b5.dx *= -1
        b5.dy *= -1
        b6.dx *= -1
        b6.dy *= -1		
        track.play() 
    if checkhit(b1,shiprect,15,25) == True:
        b1.dx *= -1
        b1.dy *= -1
        count = count -1 
    if checkhit(b2,shiprect,15,25) == True:
        b2.dx *= -1
        b2.dy *= -1
        count = count -1
    if checkhit(b3,shiprect,15,25) == True:
        b3.dx *= -1
        b3.dy *= -1
        count = count -1
    if checkhit(b4,shiprect,15,25) == True:
        b4.dx *= -1
        b4.dy *= -1
        count = count -1
    if checkhit(b5,shiprect,15,25) == True:
        b5.dx *= -1
        b5.dy *= -1
        count = count -1
    if checkhit(b6,shiprect,15,25) == True:
        b6.dx *= -1
        b6.dy *= -1 
        count = count -1
    if count <= 0:
        count = 0
        printchar("GAMEOVER",None,bluegreen,450,320,60) 
        femaleha = pygame.mixer.Sound("Femaleha.ogg")
        femaleha.play()
        if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
            pygame.quit()
			
    allsprites.clear(screen, background)
    allsprites.update()
    allsprites.draw(screen)
    screen.blit(shipimg, shiprect.topleft)
    pygame.display.update()
    clock.tick(15)

pygame.quit()