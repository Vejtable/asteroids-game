import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(1, 1)

        if Asteroid.containers:
            self.add(*Asteroid.containers)
    
    def draw(self, screen):
        color = (255, 255, 255)
        pygame.draw.circle(screen, color, (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt