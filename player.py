import pygame
from constants import *
from circleshape import CircleShape  
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0 

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = direction * PLAYER_SHOOT_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)  # rotate left
        if keys[pygame.K_d]:
            self.rotate(dt)   # rotate right
        if keys[pygame.K_w]:
            self.move(dt)     # move forward
        if keys[pygame.K_s]:
            self.move(-dt)    # move backward

        # Only allow shooting if cooldown is over
        if keys[pygame.K_SPACE] and self.shoot_timer <= 0:
            self.shoot()
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN

        # Reduce timer every frame
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

    
