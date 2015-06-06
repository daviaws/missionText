class Input_handler():

    KEY_UP = 'UP'
    KEY_DOWN = 'DOWN'
    KEY_RIGHT = 'RIGHT'
    KEY_LEFT = 'LEFT'
    
    KEY = {}
    KEY[111] = KEY_UP 
    KEY[116] = KEY_DOWN
    KEY[113] = KEY_LEFT
    KEY[114] = KEY_RIGHT
    KEY[36] = 'ENTER'
    KEY[9] = 'ESC' 
    
    def __init__(self):
    
        self.key_pressed = []
        self.listeners = []
        
    
    def add_listener(self,listener):
        self.listeners.append(listener)
    
    def notify(self):
        for listener in self.listeners:
            listener.update()
    
    def pressed_key(self,key):
        if len(self.key_pressed) == 0:
            try:
                if self.KEY[key]:
                    self.key_pressed.insert(0,self.KEY[key])
            except KeyError:
                pass
        
        self.notify()
    
    def pop_key(self):
        if len(self.key_pressed) > 0:
            return self.key_pressed.pop(0)

class Output_handler():
        
        def __init__(self):
            self.visual_output = ''
            self.sound_output = None
            self.listeners = []
            
        def add_char(self,char):
            self.character = char
            char.add_listener(self)
            
        def add_listener(self,listener):
            self.listeners.append(listener)
    
        def notify(self):
            for listener in self.listeners:
                listener.update()
        
        def update(self):
            self.generate_grid()
            self.sound_output = self.character.map.audio_file
            self.notify()
            
        def generate_grid(self):
            char_x,char_y = self.character.position()
            map = self.character.map
            map_x,map_y= map.limits()
            output = ''
            for y in range(0,map_y):
                for x in range(0,map_x):
                    if char_x == x and char_y == y:
                        output = output + self.character.SIMBOL
                    else:
                        position = map.position(x,y)
                        if position:
                            output = output + position 
                output = output + '\n'
            self.visual_output = output