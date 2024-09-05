import pygame


#husk at flippe over på skærmen

def main():
    pygame.init()


    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 600))




    running = True
    while running:   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  
        screen.fill((0, 128, 255))
        


            


        pygame.display.flip()
        clock.tick(60) 
main() 
pygame.quit()

