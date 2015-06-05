#!/usr/bin/python3

from UI import *
from iohandler import *
from model import *

GAME_WIDTH = 150
GAME_HEIGHT = 20

inh = Input_handler()
outh = Output_handler()
t1 = Terrain(GAME_WIDTH,GAME_HEIGHT)
char = Character(t1)
char.add_handler(inh)
outh.add_char(char)

gui = UI(inh,outh)
gui.start()