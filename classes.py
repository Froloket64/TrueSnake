import pygame as pg
from typing import Tuple  # Just some type hints


class Window():
    def __init__(self, size, bg_color):
        '''
        size:  Window size
        bg:  Background color
        '''

        self.size = size
        self.bg_color = bg_color

        # Init a pg.Surface
        self.surface = pg.display.set_mode(size)


class SnakeSegment():
    def __init__(self, window, size: int, color: str, pos: Tuple[int, int] = (0, 0), latest_dir: Tuple[int, int] = (0, 0)):
        '''
        surface:  A pg.Surface on which it's displayed
        size:  Size of the square segment in pixels
        color:  Color of the segment in HEX or RGB (mb others too)
        '''

        self.window = window
        # self.window.surface = self.window
        self.size = size
        self.color = color
        self.hitbox = pg.rect.Rect(pos, (size, size))
        self.segm = None
        self.latest_dir = latest_dir

        # Draw the segment
        self.draw()

    # Draw on screen/surface (an alias to pg.draw.rect)
    def draw(self):
        pg.draw.rect(self.window.surface, self.color, self.hitbox)

    # Move the snake (+ clear the cell on previous position)
    def move(self, dir):
        prev_pos = self.hitbox.copy()  # Save previous position
        self.hitbox.move_ip(dir)

        self.draw()  # Draw the snake on the new position
        pg.draw.rect(self.window.surface, self.window.bg_color, prev_pos)  # Erase the rect on snake's previous position

        self.latest_dir = dir

    # Move in the latest direction every frame / set period of time (called by event loop)
    def passive_move(self):
        if sum(self.latest_dir):  # If `latest_dir` is not (0, 0)
            self.move(self.latest_dir)

    # Attach a new segment to the body
    def add_segm(self):
        if self.segm:
            self.segm.add_segm()
        else:
            self.segm = SnakeSegment(self.window.surface, self.size, self.color)
