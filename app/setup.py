#!/usr/bin/python3

import os
import sys
from shutil import copy2

PLATFORM = sys.platform

if PLATFORM == 'linux' or PLATFORM == 'linux2':
    
    user = os.getenv("SUDO_USER")
    if user is None:
        print("This program need \'Superuser Privileges\'")
        exit()
        
    NAME = 'MissionText'
    FILE_NAME = NAME + '.desktop'
    BIN = '/usr/bin/' + NAME
    WORKING_DIR = os.getcwd() + '/'
    delimiter = '/'
    arguments = str(sys.argv[0]).split(delimiter)
    if len(arguments) > 1:
        del arguments[-1]
        if arguments[0] == '.':
            del arguments[0]
        relative_path = delimiter.join(arguments)
        WORKING_DIR = WORKING_DIR + relative_path + '/'
    HOME = os.getenv("HOME") + '/'
    LOCAL_SHARE_APLICATION = HOME + '.local/share/applications/'
    if os.path.isdir(HOME + 'Área de Trabalho/'): 
        DESKTOP = HOME + 'Área de Trabalho/'
    elif os.path.isdir(HOME + 'Desktop'):
        DESKTOP = HOME + 'Desktop'
    else:
        DESKTOP = None
    INTERPRETER = 'python3 '
    SOURCE = 'src/'
    RESOURCES = SOURCE + 'resources/'
    SH = WORKING_DIR + 'exec'
    EXEC = 'main.py'
    EXEC_PATH = WORKING_DIR + SOURCE + EXEC
    ICON = WORKING_DIR + RESOURCES + 'icon.png'
    BGM = WORKING_DIR + RESOURCES + 'sounds/BGM/'
    FILE_PATH = WORKING_DIR + FILE_NAME
    COMMENT = 'A Great Journey Begins'
    TYPE = 'Application'
    TERMINAL = 'false'
    STARTUP_NOTIFY = 'true'
    CATEGORIES = 'Game;'
    
    PERMISSION = 0o755
    
    if not (os.path.isfile(SH)): 
        file = open(SH, 'w')
        file.write('cd '+ WORKING_DIR + SOURCE + '\n')
        file.write('./' + EXEC)
        file.close
        
        file = open(FILE_PATH, 'w')
        file.write('[Desktop Entry]\n')
        file.write('Encoding=UTF-8\n')
        file.write('Name=' + NAME + '\n')
        file.write('Comment=' + COMMENT + '\n')
        file.write('Type=' + TYPE + '\n')
        file.write('Terminal=' + TERMINAL + '\n')
        file.write('Exec=' + SH + '\n')
        file.write('Icon=' + ICON + '\n')
        file.write('StartupNotify=' + STARTUP_NOTIFY + '\n')
        file.write('Categories=' + CATEGORIES + '\n')
        file.close()
	

        os.chmod(SH,PERMISSION)
        os.chmod(FILE_PATH, PERMISSION)

        os.symlink(SH, BIN)
    
        if os.path.isfile(FILE_PATH):
            copy2(FILE_PATH, LOCAL_SHARE_APLICATION)
        if DESKTOP:
            copy2(FILE_PATH, DESKTOP)
    else:
        if os.path.isfile(BIN):
            os.remove(BIN)
        if os.path.isfile(FILE_PATH):
            os.remove(FILE_PATH)
        if os.path.isfile(LOCAL_SHARE_APLICATION + FILE_NAME):
            os.remove(LOCAL_SHARE_APLICATION + FILE_NAME)
        if os.path.isfile(DESKTOP + FILE_NAME):
            os.remove(DESKTOP + FILE_NAME)
        if os.path.isfile(SH):
            os.remove(SH)