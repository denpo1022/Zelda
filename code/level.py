"""Module controlling level"""

import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug


class Level:
    """Class representing a level"""

    def __init__(self) -> None:
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
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
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        debug(self.player.direction)
