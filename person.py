from random import randint
import pygame
import random


rects = []

class Person():
    def __init__(self,rask,screen,syg,smittet):
        self.__player_direction = pygame.math.Vector2(random.choice([-1,1]),random.choice([-1,1]))
        
        self.__rask = rask
        self.__img = self.__rask
        self.__syg = syg
        self.__player_rect = self.__img.get_frect(topleft = (randint(1,500),randint(1,250)))
        rects.append(self.__player_rect)
        self.__player_speed = random.uniform(0.05,0.2)
        self.screen = screen
        self.w, self.h = pygame.display.get_surface().get_size()
  
        self.__smittet = smittet
        self.__chance = 4
        self.__index = []

        

    @property
    def smittet(self):
        return(self.__smittet)
    
    @property
    def rect(self):
        return(self.__player_rect)
    


    def borderControl(self):
        if self.__player_rect.left + self.__player_direction.x*self.__player_speed <= 0 or self.__player_rect.right + self.__player_direction.x*self.__player_speed >= self.w:
            self.__player_direction.x *= -1
            self.__player_speed *= 1-randint(1,9)/10+randint(1,9)/10

        if self.__player_rect.top + self.__player_direction.y*self.__player_speed <= 0 or self.__player_rect.bottom + self.__player_direction.y*self.__player_speed >= self.h:
            self.__player_direction.y *= -1
            self.__player_speed *= 1-randint(1,9)/10+randint(1,9)/10
        
        if self.__player_speed > 0.1*2:
            self.__player_speed = 0.1


    def update(self,mennesker):
        self.__player_rect.center += self.__player_direction*self.__player_speed
        self.__mennesker = mennesker
        self.borderControl()
        self.smitte()


    def draw(self):
        self.screen.blit(self.__img,self.__player_rect) 

    def smitte(self):
        if self.__smittet == False:
            self.__index = self.__player_rect.collidelistall(rects)
            if self.__index != []:
                for index in self.__index:
                    if self.__mennesker[index].smittet == True:
                        if randint(0,100) <= self.__chance:
                            self.__smittet = True
                #tjek status af colliderede rect hvis den er smittet rol en terning og se om er smittet
        
        if self.__smittet == True:
            self.__img = self.__syg
    
