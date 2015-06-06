class Terrain():
    
    SIDE_LIMIT = '|'
    HORIZON_LIMIT = '-'
    MIDDLE = ' '
    
    def generate(self,x,y):
        map = {}
        for trow in range(0,y):
            col = {}
            for tcol in range(0,x):
                if trow == 0 or trow == y-1:
                    col[tcol] = self.HORIZON_LIMIT
                else:
                    if tcol == 0 or tcol == x-1:
                        col[tcol] = self.SIDE_LIMIT
                    else:
                        col[tcol] = self.MIDDLE
            map[trow] = col
        return map
    
    
    def __init__(self,x,y,audio_file):
        self.x = x
        self.y = y
        self.audio_file = audio_file
        self.map = self.generate(x,y)
    
    def limits(self):
        return self.x, self.y
    
    def valid_position(self,new_x,new_y):
        if self.map[new_y][new_x] == self.SIDE_LIMIT or self.map[new_y][new_x] == self.HORIZON_LIMIT:
            return False
        return True
    
    def position(self,x,y):
        if x >= 0 and y >= 0:
            if x <= self.x and y <= self.y:
                return self.map[y][x]
        return False
    
class Character():
    
    SIMBOL = '@'
    
    def __init__(self,map):
            
        self.x = int((map.x-1)/2)
        self.y = int((map.y-1)/2)
        self.map = map
        self.listeners = []
    
    def add_handler(self,handler):
        self.ioh = handler
        self.ioh.add_listener(self)
    
    def position(self):
        return self.x, self.y
        
    def move(self):
        move = self.ioh.pop_key()
        if move == self.ioh.KEY_UP:
            if self.map.valid_position(self.x,self.y - 1):
                self.y = self.y - 1
        elif move == self.ioh.KEY_DOWN:
            if self.map.valid_position(self.x,self.y + 1):
                self.y = self.y + 1
        elif move == self.ioh.KEY_RIGHT:
            if self.map.valid_position(self.x + 1,self.y):
                self.x = self.x + 1
        elif move == self.ioh.KEY_LEFT:
            if self.map.valid_position(self.x - 1,self.y):
                self.x = self.x - 1
                
    def update(self):
        self.move()
        self.notify()
                
    def add_listener(self,listener):
        self.listeners.append(listener)
    
    def notify(self):
        for listener in self.listeners:
            listener.update()
