import pygame
from circleshape import CircleShape
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        for group in self.containers:
            group.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()  # remove current asteroid

        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # too small to split

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Random angle between 20 and 50 degrees
        angle = random.uniform(20, 50)

        # Calculate new velocity directions
        direction1 = self.velocity.rotate(angle) * 1.2
        direction2 = self.velocity.rotate(-angle) * 1.2

        # Spawn two smaller asteroids at current position
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)

        a1.velocity = direction1
        a2.velocity = direction2
        