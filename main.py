import pygame
# from module import function_hello, variable_player
from constants import *

# Define colors
black = (0, 0, 0)

def main():
    # Add your main function code here
    pass

if __name__ == "__main__":
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    pygame.init()
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill(black)
        pygame.display.flip()
main()
