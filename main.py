import pygame
# from module import function_hello, variable_player
from constants import *
from circleshape import *
from player import *

def main():
    pygame.init()
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    pygame.display.flip()
    Player.draw(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2, radius = PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        Player.draw(screen)
        # 60 frames per second
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
main()
