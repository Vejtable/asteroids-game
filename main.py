import pygame
from player import Player
from constants import *

clock = pygame.time.Clock()
dt = 0

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        dt = clock.tick(60) / 1000

        player.update(dt)
        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()