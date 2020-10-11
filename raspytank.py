# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import cv2
from datetime import datetime
import time
cap = cv2.VideoCapture(0) 
import pygame.mixer

import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

def main():
    (w,h) = (600,480)  
    (x,y) = (w/2, h/2)
    pygame.init()      
    pygame.display.set_mode((w, h), 0, 16)  
    screen = pygame.display.get_surface()
    player = pygame.image.load("target.png").convert_alpha()    
    player=pygame.transform.scale(player, (80, 80))
    rect_player = player.get_rect()
    rect_player.center = (300, 200) 
   
  
    
      
    while (1):
        try:
         ret, frame = cap.read()
   
         pygame.mixer.init() #初期化
         
         date = datetime.now().strftime("%Y%m%d_%H%M%S")
         path = "d.jpg"
         cv2.imwrite(path, frame) 
         bg = pygame.image.load("d.jpg").convert_alpha()    
        
         rect_bg = bg.get_rect()
        
         pygame.display.update()            
         pygame.time.wait(30)               
         screen.fill((0, 20, 0, 0))         
         screen.blit(bg, rect_bg)          
        
         screen.blit(player, (x, y))
         for event in pygame.event.get():
          if event.type==QUIT:           
            pygame.quit()
            sys.exit(0)
          mouse_pressed = pygame.mouse.get_pressed()
          if mouse_pressed[0]: 
            x, y = pygame.mouse.get_pos()
            
            x -= player.get_width() / 2
            y -= player.get_height() / 2
            pygame.mixer.music.load("big-explosion1.wav")
            pygame.mixer.music.play(1)
          if event.type==KEYDOWN:       
            if event.key==K_LEFT:      
               pwm.set_pwm(15, 0, 850) 
               print("LEFT")          
               
               pwm.set_pwm(14, 0, 850)
               time.sleep(1)
               pwm.set_pwm(15, 0, 0)
               pwm.set_pwm(14, 0, 0)
            if event.key==K_RIGHT:
               pwm.set_pwm(15, 0, 850) 
               
               
               print("RIGHT")          
               #GPIO.cleanup()
               pwm.set_pwm(14, 0, 850)
               time.sleep(1)
               pwm.set_pwm(15, 0, 0)
               pwm.set_pwm(14, 0, 0)
            
            if event.key==K_UP:
               pwm.set_pwm(15, 0, 850) 
               
               
               print("FRONT")          
              
               pwm.set_pwm(14, 0, 1)
               time.sleep(1)
               pwm.set_pwm(15, 0, 0)
               pwm.set_pwm(14, 0, 0)
            
            if event.key==K_DOWN:
               pwm.set_pwm(15, 0, 1) 
              
               
               print("BACK")          
               
               pwm.set_pwm(14, 0, 850)
               time.sleep(1)
               pwm.set_pwm(15, 0, 0)
               pwm.set_pwm(14, 0, 0)
            
        except: 
          print("err")
         
if __name__ == "__main__":
 main()



