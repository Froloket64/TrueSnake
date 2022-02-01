##  An attempt to implement Snake in Python (Makes sense, ha)  ##

## NOTES:  
# + pg.Rect(x_offset, y_offset, width, height)

## TODO:
# + [-] Rewrite the SnakeSegment.move() to PROPERLY "redraw" the segment
# + [-] Add segment behaviour and adding functionality

import pygame as pg
from classes import *

pg.init()
clock = pg.time.Clock()


## Setup
# Colors
# WHITE = (255, 255, 255)
WHITE = "#fbf1c7"
BLUE = "#458588"


# Window propeties
window_size = (720, 720)
window_bg = WHITE

# Cell propeties
cell_amount = 10
cell_size = window_size[0] // cell_amount


# Create a window instance
window = Window(window_size, WHITE)

window.surface.fill(window_bg)


# Create a snake
snake = SnakeSegment(window, cell_size, BLUE)


pg.display.update()


## Event loop
running = True
timer = 0
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # Keybinds
        if event.type == pg.KEYDOWN:
            match event.key:
                case pg.K_ESCAPE:
                    running = False

                case pg.K_RIGHT:
                    snake.move((cell_size, 0))
                    timer = 0  # Reset passive move timer

                case pg.K_LEFT:
                    snake.move((-cell_size, 0))
                    timer = 0

                case pg.K_DOWN:
                    snake.move((0, cell_size))
                    timer = 0

                case pg.K_UP:
                    snake.move((0, -cell_size))
                    timer = 0


    if timer == 60:
        snake.passive_move()

    # timer = (timer + 1) % 61
    timer += 1
    timer %= 61

    pg.display.flip()
    clock.tick(60)



pg.quit()
