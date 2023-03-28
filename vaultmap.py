import pygame
from settings import *
from room import Room
from debug import debug


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

