import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, PLAYER_RADIUS, PLAYER_SPEED):
        self.x = x
        self.y = y
        self.radius = radius
        self.PLAYER_SPEED = PLAYER_SPEED
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = PLAYER_RADIUS
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # Override from CircleShape
        self.screen = screen
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def move(self, dt, PLAYER_SPEED):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rotation += dt * 300
        if keys[pygame.K_RIGHT]:
            self.rotation -= dt * 300
        if keys[pygame.K_UP]:
            self.move(dt, self.PLAYER_SPEED)
        if keys[pygame.K_DOWN]:
            self.move(dt, -self.PLAYER_SPEED)

