from pyboy import PyBoy
from pyboy import WindowEvent
import numpy as np

pyboy = PyBoy("Tetris.gb", game_wrapper=True)
tetris = pyboy.game_wrapper()
tetris.start_game()

pyboy.set_emulation_speed(target_speed=1)

# # shape of the screen
# print(tetris.shape)
#
# # find out first tetromino
# first_block = tetris.game_area().base
# print(np.shape(first_block))
# print(first_block != 47)


game_continue = True

while game_continue:
    pyboy.send_input(WindowEvent.PRESS_ARROW_LEFT)
    pyboy.tick()
    pyboy.send_input(WindowEvent.RELEASE_ARROW_LEFT)
    pyboy.tick()

    if tetris.game_over():
        game_continue = False


# find out current tetromino