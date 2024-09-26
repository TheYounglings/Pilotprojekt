import pygame
from os.path import join
from person import *
from gruppe import *
from slider import *
from score import *

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 40)


def main():
    pygame.init()
    buttonPressed = False
    gruppe = False

    WINDOW_HEIGHT, WINDOW_WIDTH = 500, 1000
    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

    clock = pygame.time.Clock()

    sliders = []



    antalSlider = Slider(10,10,"raske",screen,100)

    smittetSlider = Slider(10,50,"smittet",screen,100)

    mundbindSlider = Slider(10,90,"mundbind",screen,100)

    vaccineSlider = Slider(10,130,"vaccineret",screen,100)

    #sliders.append(antalSlider)
    sliders.append(smittetSlider)
    sliders.append(mundbindSlider)
    sliders.append(vaccineSlider)



    #mennesker = Gruppe(300,screen,10,10,10)

    #mennesker.update()

    startButton = pygame.FRect(WINDOW_WIDTH/2,WINDOW_HEIGHT/2,100,100)



    running = True
    while running:  
        dt = clock.tick() / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  

        mouse_pos = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()

        screen.fill((0, 128, 255))



        if buttonPressed == False:
            antalSlider.draw()
            antalSlider.update()
            for slider in sliders:
                slider.draw()
                slider.update()
 

            

            
            pygame.draw.rect(screen,"Black",startButton) 
            startButtonText = my_font.render("start", False, "green")
            screen.blit(startButtonText, (WINDOW_WIDTH/2,WINDOW_HEIGHT/2+15))
            if startButton.collidepoint(mouse_pos) and mouse[0]:
                buttonPressed = True
        elif gruppe == False:
            mennesker = Gruppe(antalSlider.variable,screen,smittetSlider.variable,mundbindSlider.variable,vaccineSlider.variable)
            mennesker.update()
            gruppe = True
        else:

            mennesker.draw(dt)
            for scores in scoreBox:
                scores.draw(screen)
 


        pygame.display.flip()
main() 
pygame.quit()

