import pygame as pg
from typing import Tuple  # Just some type hints


# class Window():
#     def __init__(self, size, cell_amount, bg, *, cell_size):
#         self.size = size
#         self.cell_amount = cell_amount
#         self.bg = bg

#         if cell_size:
#             self.cell_size = cell_size
#         else:
#             self.cell_size = self.size[0] // self.cell_amount


class SnakeSegment():
    def __init__(self, size: int, color: str, pos: Tuple[int, int] = (0, 0), latest_dir: Tuple[int, int] = (0, 0)):
        '''
        size:  Size of the square segment in pixels
        color:  Color of the segment in HEX or RGB (mb others too)
        '''
        self.size = size
        self.color = color
        self.hitbox = pg.rect.Rect(pos, (size, size))
        self.segm = None
        self.latest_dir = latest_dir

    # Draw on screen/surface
    def draw(self, surface):
        pg.draw.rect(surface, self.color, self.hitbox)

    # Move the snake (+ clear the cell on previous position)
    def move(self, dir, surface, bg_color):
        prev_pos = self.hitbox.copy()  # Save previous position
        self.hitbox.move_ip(dir)

        self.draw(surface)  # Draw the snake on the new position
        pg.draw.rect(surface, bg_color, prev_pos)  # Erase the rect on snake's previous position

        self.latest_dir = dir

    # Move in the latest direction every frame / set period of time (called by event loop)
    def passive_move(self, surface, bg_color):
        if sum(self.latest_dir):  # If `latest_dir` is not (0, 0)
            self.move(self.latest_dir, surface, bg_color)

    # Attach a new segment to the body
    def add_segm(self):
        if self.segm:
            self.segm.add_segm()
        else:
            self.segm = SnakeSegment(self.size, self.color)
