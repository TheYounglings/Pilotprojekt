from random import randint
import pygame
import random



class Person():
    def __init__(self,img,screen):
        self.__player_direction = pygame.math.Vector2(1,1)
        
        self.__img = img

        self.__player_rect = self.__img.get_frect(topleft = (randint(1,500),randint(1,250)))
        self.__player_speed = random.uniform(0.05,0.2)

        self.screen = screen

        self.w, self.h = pygame.display.get_surface().get_size()



    def borderControl(self):
        if self.__player_rect.left + self.__player_direction.x*self.__player_speed <= 0 or self.__player_rect.right + self.__player_direction.x*self.__player_speed >= self.w:
            self.__player_direction.x *= -1
            self.__player_speed *= 1-randint(1,9)/10+randint(1,9)/10

        if self.__player_rect.top + self.__player_direction.y*self.__player_speed <= 0 or self.__player_rect.bottom + self.__player_direction.y*self.__player_speed >= self.h:
            self.__player_direction.y *= -1
            self.__player_speed *= 1-randint(1,9)/10+randint(1,9)/10
        
        if self.__player_speed > 0.1*2:
            self.__player_speed = 0.1


    def update(self,andre):
        self.__player_rect.center += self.__player_direction*self.__player_speed
        self.__andre = andre
        self.borderControl()


    def draw(self):
        self.screen.blit(self.__img,self.__player_rect) 

    def smitte(self):
        index = pygame.collidelist(self.__andre) 
        if index != -1: #Lav noget der tjekker om den allerede er ramt
            #tjek status af colliderede rect hvis den er smittet rol en terning og se om er smittet
    
