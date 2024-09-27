import pygame

from pygame.locals import *

from os.path import join
from person import *
from gruppe import *
from slider import *
from score import *
from settings import *




def main():
    
    pygame.init()

    pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
    my_font = pygame.font.SysFont('Comic Sans MS', 40)

    comicFontS = pygame.font.SysFont('Comic Sans MS',20)

    titelFont = pygame.font.SysFont('showcardgothic',100)

    settings.init()

    buttonPressed = False
    gruppe = False

    WINDOW_WIDTH, WINDOW_HEIGHT = 1920, 1080
    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),FULLSCREEN)

    clock = pygame.time.Clock()

    sliders = []

    antalSlider = Slider(20,20,"raske",screen,300)

    smittetSlider = Slider(20,100,"smittet",screen,300)

    mundbindSlider = Slider(20,180,"mundbind",screen,300)

    vaccineSlider = Slider(20,260,"vaccineret",screen,300)

    smitteChanceSlider = Slider(20,340,"smitte chance",screen,100)

    dødChanceSlider = Slider(20,420,"døds chance",screen,100)

    sliders.append(smittetSlider)
    sliders.append(mundbindSlider)
    sliders.append(vaccineSlider)
    sliders.append(smitteChanceSlider)
    sliders.append(dødChanceSlider)

    startButton = pygame.FRect(20,500,100,100)

    resetButtonBorder = pygame.FRect(10-1,WINDOW_HEIGHT-400-1,(90+2),(30+2))
    resetButton = pygame.FRect(10,WINDOW_HEIGHT-400,90,30)

    running = True
    while running:  
        dt = clock.tick() / 1000
        keys=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[K_ESCAPE]:
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
            screen.blit(startButtonText, (20,500+15))

            titelTex1 = titelFont.render("Pandemic",False, "black")
            titelTex2 = titelFont.render("Simulator",False, "black")

            screen.blit(titelTex1,(WINDOW_WIDTH/2-125*2,0))
            screen.blit(titelTex2,(WINDOW_WIDTH/2-125*2,WINDOW_HEIGHT/10))

            if startButton.collidepoint(mouse_pos) and mouse[0]:
                buttonPressed = True
        elif gruppe == False:
            mennesker = Gruppe(antalSlider.variable,screen,smittetSlider.variable,mundbindSlider.variable,vaccineSlider.variable,smitteChanceSlider.variable,dødChanceSlider.variable)
            mennesker.update()
            gruppe = True
        else:
            mennesker.draw(dt)
            for scores in settings.scoreBox:
                scores.draw(screen)
            pygame.draw.rect(screen,"Black",resetButtonBorder)
            pygame.draw.rect(screen,"White",resetButton) 
            settings.raskeScoreBox.update(settings.raskeScore)
            settings.smittetScoreBox.update(settings.smittetScore)
            settings.mundbindScoreBox.update(settings.mundbindScore)
            settings.vaccineretScoreBox.update(settings.vaccineScore)
            settings.immunScoreBox.update(settings.imunScore)
            settings.dødeScoreBox.update(settings.deadScore)

            settings.smitteChanceScoreBox.update(smitteChanceSlider.variable) 
            settings.dødeChanceScoreBox.update(dødChanceSlider.variable)    

            resetText = comicFontS.render("Genstart",False,"black")
            screen.blit(resetText,(10+2,WINDOW_HEIGHT-400))
            if resetButton.collidepoint(mouse_pos) and mouse[0]:
                running = False
                main()

 


        pygame.display.flip()
main() 


    
    
pygame.quit()

