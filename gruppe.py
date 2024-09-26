import pygame
import random
from person import *
from os.path import join
from slider import *


class Gruppe():
    def __init__(self,antal,screen, antalSmittet,antalMundbind,antalVaccine,smitteChance,dødChance):
        self.__mennesker = []

        self.__antal = antal
        self.__antalSmittet = antalSmittet
        self.__antalMundbind = antalMundbind
        self.__antalVaccine = antalVaccine

        self.__smitteChance = smitteChance
        self.__dødChance = dødChance

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

        path = join('immunstickman.png')    
        self.__immun = pygame.image.load(path).convert_alpha()
        self.__immun = pygame.transform.scale(self.__immun,(30,30)) 

        path = join('mundbindstickman.png')    
        self.__mundbindSurf = pygame.image.load(path).convert_alpha()
        self.__mundbindSurf = pygame.transform.scale(self.__mundbindSurf,(30,30))  

        path = join('mundbindsygstickman.png')    
        self.__mundbindSygSurf = pygame.image.load(path).convert_alpha()
        self.__mundbindSygSurf = pygame.transform.scale(self.__mundbindSygSurf,(30,30))  

        path = join('mundbindimmunstickman.png')    
        self.__mundbindImmunSurf = pygame.image.load(path).convert_alpha()
        self.__mundbindImmunSurf = pygame.transform.scale(self.__mundbindImmunSurf ,(30,30))  

        path = join('vaccinestickman.png')    
        self.__vaccineSurf = pygame.image.load(path).convert_alpha()
        self.__vaccineSurf = pygame.transform.scale(self.__vaccineSurf ,(30,30))  

        



    
    def update(self):
        n = 0
        s = 0
        m = 0
        v = 0
        while n < self.__antal:
            i = Person(self.__rask,self.screen,self.__sick,False,self.__død,self.__immun,False,self.__mundbindSurf,self.__mundbindSygSurf,self.__mundbindImmunSurf,self.__vaccineSurf,False,self.__smitteChance,self.__dødChance)
            self.__mennesker.append(i)
            n += 1
        while s < self.__antalSmittet:
            i = Person(self.__rask,self.screen,self.__sick,True,self.__død,self.__immun,False,self.__mundbindSurf,self.__mundbindSygSurf,self.__mundbindImmunSurf,self.__vaccineSurf,False,self.__smitteChance,self.__dødChance)  
            self.__mennesker.append(i)
            s += 1   
        while m < self.__antalMundbind:
            i = Person(self.__rask,self.screen,self.__sick,False,self.__død,self.__immun,True,self.__mundbindSurf,self.__mundbindSygSurf,self.__mundbindImmunSurf,self.__vaccineSurf,False,self.__smitteChance,self.__dødChance)
            self.__mennesker.append(i)
            m += 1  
        while v < self.__antalVaccine:
            i = Person(self.__rask,self.screen,self.__sick,False,self.__død,self.__immun,False,self.__mundbindSurf,self.__mundbindSygSurf,self.__mundbindImmunSurf,self.__vaccineSurf,True,self.__smitteChance,self.__dødChance)
            self.__mennesker.append(i)
            v += 1  


        


    
    def draw(self,dt):
        for personer in self.__mennesker:
            personer.update(self.__mennesker,dt)
            personer.draw()
