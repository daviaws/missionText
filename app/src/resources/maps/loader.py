import os

class logger():
    
    def __init__(self):
        self.logging = False
        self.output = 'Log Initialized\n'
        
    def is_logging(self):
        return self.logging
        
    def logging(self,condition):
        if condition:
            self.loging = True
        self.loging = False
            
    def add_log(self,string):
        if self.logging:
            self.output += string + '\n'
    
    def print_log(self):
        print(self.output)
    
    def push(self):
        print(self.output)
        self.output = ''
        
    def save(self):
        self.add_log('Not implemmented')
        self.print_log()

class Tile():
    
    def __init__(self,printable,name,walkable=False,color='white'):
        self.printable = printable
        self.name = name
        self.walkable = walkable
        self.color = color
    
    def is_walkable(self):
        return self.walkable

class Tiles():
    
    def __init__(self):
        self.tiles = {}
        self.walkable_tiles = {}
        self.not_walkable_tiles = {}
    
    def add(self, tile):
        try:
            tiles = iter(tile)
        except TypeError:
            self.tiles[tile.printable] = tile
            if tile.is_walkable():
                self.walkable_tiles[tile.printable] = tile 
            else:
                self.not_walkable_tiles[tile.printable] = tile
        else:
            for tile in tiles:
                self.tiles[tile.printable] = tile
                if tile.is_walkable():
                    self.walkable_tiles[tile.printable] = tile 
                else:
                    self.not_walkable_tiles[tile.printable] = tile
        
    def get(self,char):
        if char in tiles.keys():
            return tiles[char]
        else:
            return None

class Loader():

    def __init__(self):
        
        self.tiles_file = None
        self.maps_file = None
        
        self.tiles = []
        self.maps = []
        
        self.log = None
    
    def add_logger(self,logger):
        self.log = logger
        self.log.logging(True)           
        
    def set_tiles_file(self,tiles_file):
        if os.path.isfile(tiles_file):
            self.tiles_file = tiles_file
            self.log.add_log('Tiles file is: {}'.format(self.tiles_file))
        else:
            self.log.add_log('Tiles file not exists')
    
    def set_maps_file(self,maps_file):
        if os.path.isfile(maps_file):
            self.maps_file = maps_file
            self.log.add_log('Maps file is: {}'.format(self.maps_file))
        else:
            self.log.add_log('Maps file not exists')
            
        
horizontal_limit = Tile('-', 'HORIZONTAL_LIMIT')
vertical_limit = Tile('|', 'VERTICAL_LIMIT') 
ground = Tile(' ', 'GROUND', True)
water = Tile('~','WATER', False, 'blue')
grass = Tile(',','GRASS',True,'green')

tile_list = [horizontal_limit,vertical_limit,ground,water,grass]
tiles = Tiles()
tiles.add(tile_list)


file = open('map1','r')
map = file.read()
map = map.split('\n')

#for line in range(0,len(map)):
#    print(map[line])
print ('All tiles: {}'.format(tiles.tiles.keys()))
print ('Walkable tiles: {}'.format(tiles.walkable_tiles.keys()))
print ('Not Walkable tiles: {}'.format(tiles.not_walkable_tiles.keys()))