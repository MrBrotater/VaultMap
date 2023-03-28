import pygame, sys

# SETTINGS -----------------------------------------------------------------------------------
pygame.init()

WIDTH = 700
HEIGHT = 700
FPS = 5
ROOMSIZE = 100

WORLD_MAP = [
['u', 'u', 'u', 'r', 'u', 'u', 'u'],
['u', 'u', 'r', 'r', 'r', 'u', 'u'],
['u', 'r', 'r', 'r', 'r', 'r', 'u'],
['r', 'r', 'r', 'p', 'r', 'r', 'r'],
['u', 'r', 'r', 'r', 'r', 'r', 'u'],
['u', 'u', 'r', 'r', 'r', 'u', 'u'],
['u', 'u', 'u', 'r', 'u', 'u', 'u'],
]

# DEBUG TOOL --------------------------------------------------------------------------------
font = pygame.font.Font(None, 30)

def debug(info, y=10, x=10):
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'White')
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    pygame.draw.rect(display_surface, 'Black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)

# ROOM CLASS ---------------------------------------------------------------------------------
class Room(pygame.sprite.Sprite):
    def __init__(self, pos, groups, roomtype):
        super().__init__(groups)
        self.pos = pos
        self.roomtype = roomtype
        self.rect = pygame.Rect(pos, (ROOMSIZE, ROOMSIZE))

# VAULTMAP CLASS -----------------------------------------------------------------------------
class VaultMap:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.portal = pygame.Rect((WIDTH//2-ROOMSIZE//8, HEIGHT//2-ROOMSIZE//8), (ROOMSIZE//4, ROOMSIZE//4))

        # sprite setup
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, column in enumerate(row):
                x = col_index * ROOMSIZE
                y = row_index * ROOMSIZE
                if column == 'r':
                    Room(pos=(x, y), groups=[self.visible_sprites], roomtype='unvisited')
                if column == 'p':
                    Room(pos=(x, y), groups=[self.visible_sprites], roomtype='current')
                    
    def run(self, current_position):
        for sprite in self.visible_sprites:
            #reset room types if portal is clicked
            if self.portal.collidepoint(current_position):
                for oldsprite in self.visible_sprites:
                    if oldsprite.roomtype == 'visited':
                        oldsprite.roomtype = 'unvisited'

            # update room types based on current position (last mouse click)
            if sprite.rect.collidepoint(current_position):
                for oldsprite in self.visible_sprites:
                    if oldsprite.roomtype == 'current':
                        oldsprite.roomtype = 'visited'
                sprite.roomtype = 'current'

            # draw the rooms
            if sprite.roomtype == 'current':
                pygame.draw.rect(self.display_surface, 'chartreuse3', sprite.rect)
                pygame.draw.rect(self.display_surface, 'black', sprite.rect, width=2)
            elif sprite.roomtype == 'visited':
                pygame.draw.rect(self.display_surface, 'darkgrey', sprite.rect)
                pygame.draw.rect(self.display_surface, 'black', sprite.rect, width=2)
            elif sprite.roomtype == 'unvisited':
                pygame.draw.rect(self.display_surface, 'gray30', sprite.rect)
                pygame.draw.rect(self.display_surface, 'black', sprite.rect, width=2)
            else:
                print(f'unexpected room type at {sprite.pos}')
        pygame.draw.rect(self.display_surface, 'purple', self.portal)

#MAIN GAME CLASS ------------------------------------------------------------------------------
class Game:
    def __init__(self):

        # general setup
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
