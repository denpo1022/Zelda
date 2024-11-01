"""Module controlling level"""

from typing import Iterable
import pygame
from pygame.sprite import AbstractGroup
from settings import *
from tile import Tile
from player import Player
from debug import debug


class Level:
    """Class representing a level"""

    def __init__(self) -> None:
        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()

        # spite setup
        self.create_map()

    def create_map(self) -> None:
        """Method that create map"""
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == "x":
                    Tile((x, y), [self.visible_sprites, self.obstacles_sprites])
                if col == "p":
                    self.player = Player(
                        (x, y), [self.visible_sprites], self.obstacles_sprites
                    )

    def run(self) -> None:
        """Method that run the stage"""
        # update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


class YSortCameraGroup(pygame.sprite.Group):
    """Vertical camera group"""

    def __init__(self) -> None:

        # general setup
        super().__init__(self)
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2(100, 200)

    def custom_draw(self, player: Player) -> None:
        """Custom drawing sprites method"""

        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
