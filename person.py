from random import randint
import pygame
import random


rects = []

class Person():
    def __init__(self,rask,screen,syg,smittet,død,mundbind,mundbindSurf):
        self.__player_direction = pygame.math.Vector2(random.choice([-1,1]),random.choice([-1,1]))
        self.__lastIndex = []
        self.__rask = rask
        self.__død = død
        self.__mundbindSurf = mundbindSurf
        if mundbind == False:
            self.__img = self.__rask
        else:
            self.__img = self.__mundbindSurf
        self.__syg = syg
        self.__player_speed = random.uniform(40,60)
        self.screen = screen
        self.w, self.h = pygame.display.get_surface().get_size()
        self.__wait = 0
        self.__smittet = smittet
        self.__dødChance = 10
        self.__chance = 10
        self.__mundbind = mundbind
        self.__index = []
        self.__dead = False
        self.__player_rect = self.__img.get_frect(topleft = (randint(1,950),randint(1,450)))
        rects.append(self.__player_rect)

        

    @property
    def smittet(self):
        return(self.__smittet)
    
    @property
    def rect(self):
        return(self.__player_rect)
    


    def borderControl(self):
        if self.__player_rect.left + self.__player_direction.x*self.__player_speed*self.__dt <= 0 or self.__player_rect.right + self.__player_direction.x*self.__player_speed * self.__dt >= self.w:
            self.__player_direction.x *= -1
            self.__player_speed += randint(1,20) - randint(1,20)

        if self.__player_rect.top + self.__player_direction.y*self.__player_speed*self.__dt <= 0 or self.__player_rect.bottom + self.__player_direction.y*self.__player_speed*self.__dt >= self.h:
            self.__player_direction.y *= -1
            self.__player_speed += randint(1,20)-randint(1,20)
        
        if self.__player_speed > 40 or self.__player_speed < 60:
            self.__player_speed = 50


    def update(self,mennesker,fps,dt):
        if self.__dead == False:
            self.__dt = dt
            self.__player_rect.center += self.__player_direction*self.__player_speed*self.__dt
            self.__mennesker = mennesker
            self.borderControl()
            self.smitte()
            self.__fps = fps
            if self.__smittet == True:
                self.raske()


    def draw(self):
        self.screen.blit(self.__img,self.__player_rect) 

    def smitte(self):
        if self.__smittet == False:
                self.__index = self.__player_rect.collidelistall(rects)
                if self.__index != []:
  
                    for index in self.__index:
                        if index in self.__lastIndex:
                            continue
                        else:
                            if self.__mennesker[index].smittet:
                                if self.__mundbind == True:
                                    tempChance = self.__chance * 0.5
                                else:
                                    tempChance = self.__chance
                                if randint(0,100) <= tempChance:
                                    self.__smittet = True
                                    self.__wait = 0
                        #tjek status af colliderede rect hvis den er smittet rol en terning og se om er smittet
        self.__lastIndex = self.__index 
        if self.__smittet == True and self.__mundbind == False:
            self.__img = self.__syg
        elif self.__smittet == True and self.__mundbind == True:
            self.__img = self.__sygMundbind
    
    def raske(self):
        if self.__wait > 10000:
            if randint(0,100) <= self.__dødChance:
                self.__player_speed = 0
                self.__img = self.__død
                self.__smittet = False
                self.__wait = -1
                self.__dead = True
            elif (self.__player_speed != 0):
                self.__smittet = False
                self.__chance *= 0.5
                if self.__mundbind == False:
                    self.__img = self.__rask
                else:
                    self.__img = self.__mundbindSurf
                self.__wait = -1
        self.__wait += 1