import pygame
from os.path import join
from person import *


#husk at flippe over på skærmen



def main():
    pygame.init()
    WINDOW_HEIGHT, WINDOW_WIDTH = 500, 1000
    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))


    
    path = join('Normalstickman.png')
    player_surf = pygame.image.load(path).convert_alpha()
    player_surf = pygame.transform.scale(player_surf,(30,30))

    mennesker = []

    n = 0
    while n < 100:
        i = n
        i = Person(player_surf,screen)
        mennesker.append(i)
        n += 1

    carl = Person(player_surf,screen)

    # player_rect = player_surf.get_frect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
    # player_direction = pygame.math.Vector2(1,-1)
    # player_speed = 0.1




    clock = pygame.time.Clock()





    running = True
    while running:  
        clock.tick()  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  
        
        screen.fill((0, 128, 255))

        for personer in mennesker:
            personer.update(mennesker)
            personer.draw()

        carl.update()

        carl.draw()

        pygame.display.flip()
main() 
pygame.quit()

