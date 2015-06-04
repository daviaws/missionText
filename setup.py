#!/usr/bin/python3

from os import getcwd, chmod, path, getenv, remove
from sys import platform
from shutil import copy2

PLATFORM = platform

if PLATFORM == 'linux' or PLATFORM == 'linux2':

    WORKING_DIR = getcwd() + '/'
    HOME = getenv("HOME")+ '/'
    LOCAL_SHARE_APLICATION = HOME + '.local/share/applications/'
    if path.isdir(HOME+'Área de Trabalho/'): 
        DESKTOP = HOME+'Área de Trabalho/'
    elif path.isdir(HOME+'Desktop'):
        DESKTOP = HOME+'Desktop'
    else:
        DESKTOP = None
    INTERPRETER = 'python3'
    SOURCE = 'src/'
    RESOURCES = SOURCE + 'resources/'
    EXEC = INTERPRETER + ' ' + WORKING_DIR + SOURCE + 'main.py'
    ICON = WORKING_DIR + RESOURCES + 'icon.png'
    NAME = 'MissionText'
    FILE_NAME = NAME + '.desktop'
    FILE_PATH = WORKING_DIR + FILE_NAME
    COMMENT = 'A Great Journey Begins'
    TYPE = 'Application'
    TERMINAL = 'false'
    STARTUP_NOTIFY = 'true'
    CATEGORIES = 'Game;'
    

    PERMISSION = 0o755
    if not (path.isfile(FILE_PATH) or path.isfile(LOCAL_SHARE_APLICATION+FILE_NAME) or path.isfile(DESKTOP+FILE_NAME)): 
        print('Installing')
        file = open(FILE_PATH,'w')
        file.write('[Desktop Entry]\n')
        file.write('Encoding=UTF-8\n')
        file.write('Name='+NAME+'\n')
        file.write('Comment='+COMMENT+'\n')
        file.write('Type='+TYPE+'\n')
        file.write('Terminal='+TERMINAL+'\n')
        file.write('Exec='+EXEC+'\n')
        file.write('Icon='+ICON+'\n')
        file.write('StartupNotify='+STARTUP_NOTIFY+'\n')
        file.write('Categories='+CATEGORIES+'\n')
        file.close()

        chmod(FILE_PATH,PERMISSION)
    
        if path.isfile(FILE_PATH):
            copy2(FILE_PATH, LOCAL_SHARE_APLICATION)
        if DESKTOP:
            copy2(FILE_PATH, DESKTOP)
    else:
        print('Removing')
        if path.isfile(FILE_PATH):
            remove(FILE_PATH)
        if path.isfile(LOCAL_SHARE_APLICATION+FILE_NAME):
            remove(LOCAL_SHARE_APLICATION+FILE_NAME)
        if path.isfile(DESKTOP+FILE_NAME):
            remove(DESKTOP+FILE_NAME)