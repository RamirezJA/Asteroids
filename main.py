import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    black = (0, 0, 0)  # Ensure black is defined if not in constants
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(black)  # Correct way to fill the screen with black
        pygame.display.flip()

if __name__ == "__main__":
    main()
