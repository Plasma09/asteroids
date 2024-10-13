import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
               
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        # Delta Time
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()