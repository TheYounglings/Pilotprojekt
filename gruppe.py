import pygame
import random
from person import *
from os.path import join


class Gruppe():
    def __init__(self,antal,screen, antalSmittet):
        self.__mennesker = []



        self.__antal = antal
        self.__antalSmittet = antalSmittet
        self.screen = screen
        path = join('Normalstickman.png')
        self.__rask = pygame.image.load(path).convert_alpha()
        self.__rask = pygame.transform.scale(self.__rask,(30,30))
        
        path = join('Sickstickman.png')
        self.__sick = pygame.image.load(path).convert_alpha()
        self.__sick = pygame.transform.scale(self.__sick,(30,30))        

    
    def update(self):
        n = 0
        s = 0
        while n < self.__antal:
            i = n
            while s < self.__antalSmittet:
                i = Person(self.__rask,self.screen,self.__sick,True)  
                self.__mennesker.append(i)
                n += 1
                s += 1       
            i = Person(self.__rask,self.screen,self.__sick,False)
            self.__mennesker.append(i)
            n += 1
        


    
    def draw(self):
        for personer in self.__mennesker:
            personer.update(self.__mennesker)
            personer.draw()
