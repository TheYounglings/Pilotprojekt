from random import randint
import pygame
import random
from score import * 
import settings








class Person():
    def __init__(self,rask,screen,syg,smittet,død,immun,mundbind,mundbindSurf,mundbindSygSurf,mundbindImmunSurf,vaccineSurf,vaccine,smitteChance,dødChance):

        self.__player_direction = pygame.math.Vector2(random.choice([-1,1]),random.choice([-1,1]))
        self.__lastIndex = []
        self.__rask = rask
        self.__død = død
        self.__immun = immun
        self.__mundbindSurf = mundbindSurf
        self.__mundbindSygSurf = mundbindSygSurf
        self.__mundbindImmunSurf = mundbindImmunSurf
        self.__vaccineSurf = vaccineSurf
        self.__erVaccineret = vaccine

        settings.raskeScore += 1

        if mundbind == True:
            self.__img = self.__mundbindSurf

            settings.mundbindScore += 1
        elif self.__erVaccineret == True :
            self.__img = self.__vaccineSurf
            settings.vaccineScore += 1
        else:
            self.__img = self.__rask
        self.__syg = syg
        self.__player_speed = random.uniform(40,60)
        self.screen = screen
        self.w, self.h = pygame.display.get_surface().get_size()
        self.__wait = 0
        self.__smittet = smittet
        self.__dødChance = dødChance
        self.__chance = smitteChance
        self.__mundbind = mundbind
        self.__index = []
        self.__dead = False
        self.__player_rect = self.__img.get_frect(topleft = (randint(1,self.w-50),randint(1,self.h-50)))
        settings.rects.append(self.__player_rect)


        

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


    def update(self,mennesker,dt):
        # settings.raskeScoreBox.update(settings.raskeScore)
        # settings.smittetScoreBox.update(settings.smittetScore)
        # settings.mundbindScoreBox.update(settings.mundbindScore)
        # settings.vaccineretScoreBox.update(settings.vaccineScore)
        # settings.immunScoreBox.update(settings.imunScore)
        # settings.dødeScoreBox.update(settings.deadScore)
        # settings.smitteChanceScoreBox.update(self.__chance)
        # settings.dødeChanceScoreBox.update(self.__dødChance)

        if self.__dead == False:
            self.__dt = dt
            self.__player_rect.center += self.__player_direction*self.__player_speed*self.__dt
            self.__mennesker = mennesker
            self.borderControl()
            if self.__erVaccineret == False:

                self.smitte()
                if self.__smittet == True:
                    self.raske()


    def draw(self):
        self.screen.blit(self.__img,self.__player_rect) 

    def smitte(self):
        if self.__smittet == False:
                self.__index = self.__player_rect.collidelistall(settings.rects)
                if self.__index != []:
  
                    for index in self.__index:
                        if index in self.__lastIndex:
                            continue
                        else:
                            if self.__mennesker[index].smittet:
                                if self.__mennesker[index].__mundbind == True:
                                    tempChance = self.__chance * 0.5
                                else:
                                    tempChance = self.__chance
                                if randint(1,100) <= tempChance:
                                    self.__smittet = True
                                    self.__wait = 0
                        #tjek status af colliderede rect hvis den er smittet rol en terning og se om er smittet
        self.__lastIndex = self.__index 

        if self.__smittet == True and True == (self.__img == self.__mundbindImmunSurf or self.__img == self.__immun):
            settings.imunScore -= 1


        if self.__smittet == True and self.__img != self.__syg and self.__img != self.__mundbindSygSurf:
            settings.smittetScore += 1
            settings.raskeScore -= 1

        if self.__smittet == True and self.__mundbind == False:
            self.__img = self.__syg

        elif self.__smittet == True and self.__mundbind == True:
            self.__img = self.__mundbindSygSurf
            

    
    def raske(self):
        if self.__wait > 20/self.__dt:
            if randint(1,100) <= self.__dødChance:
                self.__player_speed = 0
                if self.__img == self.__mundbindSygSurf:
                    settings.mundbindScore -= 1
                self.__img = self.__død
                self.__smittet = False
                self.__wait = -1
                self.__dead = True
                settings.deadScore += 1
                settings.smittetScore -= 1
                
            elif (self.__player_speed != 0):
                self.__smittet = False
                self.__chance *= 0.5
                settings.smittetScore -= 1
                settings.raskeScore += 1
                settings.imunScore += 1
                if self.__mundbind == False:
                    self.__img = self.__immun
                else:
                    self.__img = self.__mundbindImmunSurf
                self.__wait = -1
        self.__wait += 1