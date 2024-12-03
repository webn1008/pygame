def __init__(self, x, y, radius):
    # we will be using this later
    if hasattr(self, "containers"):
        super().__init__(self.containers)
    else:
        super().__init__()

    self.position = pygame.Vector2(x, y)
    self.velocity = pygame.Vector2(0, 0)
    self.radius = radius