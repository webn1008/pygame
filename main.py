import pygame
# from module import function_hello, variable_player
from constants import *
from circleshape import *
from player import *
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updatable, drawable)
def main():
    pygame.init()
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    screen.fill("black")
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2, radius = 2, PLAYER_RADIUS = 20, PLAYER_SPEED = PLAYER_SPEED)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for player in updatable:
            updatable.update(dt)
        for player in drawable:
            drawable.draw(screen)
        # player.draw(screen)
        # player.update(dt)
        pygame.display.flip()
        # 60 frames per second
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
main()
