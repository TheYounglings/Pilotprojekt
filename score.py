import pygame



class Score():
    def __init__(self,posX,posY,name,variable):
        pygame.font.init() # you have to call this at the start, 
            # if you want to use this module.
        global my_font

        my_font = pygame.font.SysFont('Comic Sans MS', 15)
        self.__posX = posX
        self.__posY = posY
        self.__length = 140
        self.__height = 25
        self.__variable = variable
        self.__name = name
        self.__scoreBox = pygame.FRect(self.__posX,self.__posY,self.__length,self.__height)
        self.__scoreBoxBorder = pygame.FRect(self.__posX-1,self.__posY-1,self.__length+2,self.__height+2)

    
    def update(self,variable):
        self.__variable = variable

    def draw(self,screen):
        pygame.draw.rect(screen,"Black",self.__scoreBoxBorder)

        pygame.draw.rect(screen,"White",self.__scoreBox)
        
        antal = str(self.__variable)
        self.__textSurface = my_font.render(f'{antal} {self.__name}', False, "darkgreen")
        screen.blit(self.__textSurface, (self.__posX+5,self.__posY))