# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from circleshape import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    # Initialize Pygame
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0  

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    BLACK = (0, 0, 0)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while running:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
         
         screen.fill(BLACK)
         player.draw(screen)
         dt = clock.tick(60) / 1000
         pygame.display.flip()
    
    pygame.quit()



if __name__ == "__main__":
    main()
