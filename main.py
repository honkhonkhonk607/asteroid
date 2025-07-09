# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a Clock object and initialize dt
    clock = pygame.time.Clock()
    dt = 0

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set static containers
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    # Create objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)

    field = AsteroidField()  # automatically added to updatable


    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Fill screen with black
        screen.fill((0, 0, 0))

        # Update all updatables and drawables
        updatable.update(dt)

        # Player-asteroid collision
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                return
            
        # Killing asteroids
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split() 
                    shot.kill()

        for obj in drawable:
            obj.draw(screen)

        # Update the display
        pygame.display.flip()

        # Control the frame rate and calculate delta time
        dt = clock.tick(60) / 1000  # dt is in seconds

if __name__ == "__main__":
    main()

print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")
