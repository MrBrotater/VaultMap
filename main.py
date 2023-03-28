import pygame, sys
from settings import *
from vaultmap import VaultMap
from debug import debug


class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Vault Room Tracker')
        self.clock = pygame.time.Clock()

        self.vaultmap = VaultMap()

    def run(self):
        current_position = (350,350)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    current_position = event.pos
            
            self.screen.fill('black')
            self.vaultmap.run(current_position)
            debug('Click portal to reset map')
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()


