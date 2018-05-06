import pygame
import pygame, sys 

from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 320), 0, 32)
pygame.display.set_caption("Hello, Plan Y")
while True: 
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            
            sys.exit()# 退出系统
            
    pygame.display.update()# 绘制屏幕内
