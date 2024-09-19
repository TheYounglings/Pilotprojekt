import pygame
import random
from person import *
from os.path import join


class Gruppe():
    def __init__(self,antal,screen, antalSmittet,antalMundbind):
        self.__mennesker = []



        self.__antal = antal
        self.__antalSmittet = antalSmittet
        self.__antalMundbind = antalMundbind
        self.screen = screen
        path = join('Normalstickman.png')
        self.__rask = pygame.image.load(path).convert_alpha()
        self.__rask = pygame.transform.scale(self.__rask,(30,30))
        
        path = join('Sickstickman.png')
        self.__sick = pygame.image.load(path).convert_alpha()
        self.__sick = pygame.transform.scale(self.__sick,(30,30))  

        path = join('Dødstickman.png')    
        self.__død = pygame.image.load(path).convert_alpha()
        self.__død = pygame.transform.scale(self.__død,(30,30))   



    
    def update(self):
        n = 0
        s = 0
        m = 0
        while n < self.__antal:
            i = n
            while s < self.__antalSmittet:
                i = Person(self.__rask,self.screen,self.__sick,True,self.__død,False)  
                self.__mennesker.append(i)
                n += 1
                s += 1   
            while m < self.__antalMundbind:
                i = Person(self.__rask,self.screen,self.__sick,False,self.__død,True)
                self.__mennesker.append(i)
                n += 1
                s += 1  
            i = Person(self.__rask,self.screen,self.__sick,False,self.__død,False)
            self.__mennesker.append(i)
            n += 1
        


    
    def draw(self,fps,dt):
        for personer in self.__mennesker:
            personer.update(self.__mennesker,fps,dt)
            personer.draw()
