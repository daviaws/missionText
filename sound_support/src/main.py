#!/usr/bin/python3

from UI import *
from iohandler import *
from Model import *
from Audio import Audio_Output

GAME_WIDTH = 100
GAME_HEIGHT = 20
SOUND = 'resources/sounds/BGM/To_Far_Away_Times.mp3'

inh = Input_handler()
outh = Output_handler()
t1 = Terrain(GAME_WIDTH,GAME_HEIGHT,SOUND)
char = Character(t1)
char.add_handler(inh)
outh.add_char(char)
sound = Audio_Output()
sound.add_handler(outh)

gui = UI(inh,outh)
gui.start()