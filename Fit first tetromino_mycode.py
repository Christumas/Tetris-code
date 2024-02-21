from pyboy import PyBoy, WindowEvent
import numpy as np
import random

pyboy = PyBoy("Tetris.gb", game_wrapper=True)
tetris = pyboy.game_wrapper()
tetris.start_game()

pyboy.set_emulation_speed(target_speed=1)

# find the array and shape of each starting block
# logic: loop through the array of each shape, find the values != 47, then make a numpy array based on that shape

# block_info = []
# for i in range(300):
#     tetris.reset_game()
#     first_block = tetris.game_area().base
#     block_info.append(first_block[1:4, 2:8])

# print(np.array(block_info))
# print(np.unique(block_info))
# print(np.shape(block_info))

pyboy.set_emulation_speed(target_speed=5)

shapes = {"O": 131, "S": 134, "J": 129, "Z": 130, "L": 132, "T": 133, "I": 143, }
to_left = ["O", "S", "L", "T", "I"]
to_right = ["J", "Z"]
transformations = {"O": 0, "S": 0, "J": 1, "Z": 0, "L": 3, "T": 2, "I": 1}


def left():
    pyboy.send_input(WindowEvent.PRESS_ARROW_LEFT)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_ARROW_LEFT)
    pyboy.tick()


def right():
    pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
    pyboy.tick()


def current_tetromino(array):
    block = np.array(array).flatten().max()
    for i in shapes:
        if shapes[i] == block:
            print(i)
            return i
        else:
            continue


while True:
    roi = tetris.game_area().base[1:5, 2:8]
    if current_tetromino(roi) in to_left:
        left()
    elif current_tetromino(roi) in to_right:
        right()
    else:
        pyboy.tick()
