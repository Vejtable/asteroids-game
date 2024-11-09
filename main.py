import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

#Main function
def main():
    #Initializes pygame and its modules
    pygame.init()
    #Screen object used to set screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #Clock object used to set FPS
    clock = pygame.time.Clock()

    #Sets up containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Puts Asteroids in containers
    Asteroid.containers = (asteroids, updatable, drawable)

    #Puts Shot in containers
    Shot.containers = (shots, updatable, drawable)

    #Puts asteroidfield in container
    AsteroidField.containers = updatable
    #Creates custom class
    asteroid_field = AsteroidField()

    #Places the Player in the updatable and drawable containers
    Player.containers = (updatable, drawable)

    #Spawn player in middle of screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #Delta time
    dt = 0

    #Main game loop
    while True:
        #Enables quitting out of the game window upon clicking 'X'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Updates objects in the 'updateable' container, dt makes the game time-stable regardless of fps
        for obj in updatable:
            obj.update(dt)

        #Checks for player/asteroid collision, closes the window and prints "Game over!" if collision takes place
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
        
        #Checks for shot/asteroid collision, kills both objects
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        #Sets the background colour, allowing 'draw' commands to be seen by contrast
        screen.fill("black")

        #Render each object in the 'drawable' container
        for obj in drawable:
            obj.draw(screen)

        #"Flips" the buffer (our screen), allowing for smoother visuals as the next frame is prepared "behind the scenes" instead of in a split second
        pygame.display.flip()
        
        #Sets target FPS to 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
