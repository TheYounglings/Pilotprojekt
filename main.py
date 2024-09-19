import pygame
from os.path import join
from person import *
from gruppe import *



def main():
    pygame.init()

    WINDOW_HEIGHT, WINDOW_WIDTH = 500, 1000
    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

    clock = pygame.time.Clock()

    mennesker = Gruppe(100,screen,10,10)

    mennesker.update()

    running = True
    while running:  
        dt = clock.tick() / 1000
        fps = clock.get_fps()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  
        
        screen.fill((0, 128, 255))


        mennesker.draw(fps,dt)

        pygame.display.flip()
main() 
pygame.quit()

