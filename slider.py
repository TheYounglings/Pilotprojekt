import pygame



pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 10*2)

class Slider():
    def __init__(self,posX,posY,name,screen,maks,variable=0):
        self.__posX = posX
        self.__posY = posY
        self.__length = 2*300
        self.__height = 2*25
        self.__variable = variable
        self.__name = name
        self.__maks = maks
        self.__min = 0
        self.screen = screen

        self.__sliderBar = pygame.FRect(self.__posX,self.__posY,self.__length,self.__height)

        self.__button = pygame.FRect(self.__posX-self.__height/4, self.__posY-2,self.__height/2,self.__height+4)

    @property
    def maks(self):
        return(self.__maks)

    @maks.setter
    def maks(self,maks):
        self.__maks = maks

    @property
    def variable(self):
        return(round(self.__variable,0))


    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()
        if self.__sliderBar.collidepoint(mouse_pos) and mouse[0]:
            self.__button.centerx = mouse_pos[0]
        self.__variable = (self.__button.centerx - self.__posX) * self.__maks/self.__length


    def draw(self):
        pygame.draw.rect(self.screen,"Black",self.__sliderBar) 
        pygame.draw.rect(self.screen,"Gray",self.__button) 

        antal = str(round(self.__variable,0))
        self.__textSurface = my_font.render(f'{antal} {self.__name}', False, "red")
        self.screen.blit(self.__textSurface, (self.__posX,self.__posY+6))
