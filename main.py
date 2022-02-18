##  An attempt to implement Snake in Python (Makes sense, ha)  ##

## NOTES:  
# + pg.Rect(x_offset, y_offset, width, height)

## TODO:
# + [-] Rewrite the SnakeSegment.move() to PROPERLY "redraw" the segment
# + [-] Add segment behaviour and adding functionality

import pygame as pg
from classes import *
from tools import *
from random import randrange

pg.init()
clock = pg.time.Clock()


## Setup
# Config defaults
options = {
    # Window properties
    "window_size": (720, 720),
    "window_bg": "#fbf1c7",

    # Cell properties
    "cell_amount": 10,

    # Snake properties
    "snake_color": "#458588",
    "snake_segments": 5,

    # Apple propeties
    "apple_color": "#fb4934",

    # Others
    "frames": 20  # How many frames to wait between snake moves
}

config = parse_config("config.ini")  # Read configfile
options = patch_options(config, options)  # Set configured options

# Calculate cell size
cell_size = options["window_size"][0] // options["cell_amount"]

# Set directions associated with direction keys
dirs = {
    pg.K_RIGHT: (cell_size, 0),
    pg.K_LEFT: (-cell_size, 0),
    pg.K_DOWN: (0, cell_size),
    pg.K_UP: (0, -cell_size),
}

# Create a window instance
window = Window(options["window_size"], options["window_bg"])

# Create a snake
snake = SnakeSegment(window, cell_size, options["snake_color"])

for i in range(options["snake_segments"]):
    snake.add_segm()

# Add an apple
apple_init_x = randrange(0, options["cell_amount"]) * cell_size
apple_init_y = randrange(0, options["cell_amount"]) * cell_size

apple = Apple(window, cell_size, options["apple_color"], (apple_init_x, apple_init_y))

# Update the screen
pg.display.update()


## Event loop
running = True
timer = 0  # "Move timer"
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # Keybinds
        if event.type == pg.KEYDOWN:
            match event.key:
                case pg.K_ESCAPE:
                    running = False

                case pg.K_RIGHT | pg.K_LEFT | pg.K_DOWN | pg.K_UP:
                    snake.stage_move(dirs[event.key])



    if timer == options["frames"]:
        new_pos = snake.hitbox.move(*snake.current_dir)

        if pg.rect.Rect.colliderect(new_pos, apple.hitbox):
            x = randrange(0, options["cell_amount"]) * cell_size
            y = randrange(0, options["cell_amount"]) * cell_size

            apple.redraw((x, y))

            snake.add_segm()

        snake.passive_move()


    timer += 1
    timer %= options["frames"] + 1

    pg.display.flip()
    clock.tick(60)


pg.quit()
