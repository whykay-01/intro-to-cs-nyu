import os, random

path = os.getcwd() # get the current working directory of the folder this file is stored in
NUM_ROWS = 4
NUM_COLS = 4
RESOLUTION = 800
TILE_WIDTH = RESOLUTION/NUM_COLS
TILE_HEIGHT = RESOLUTION/NUM_ROWS
NEIGHBORS = [[-1,0], [0,-1], [1,0], [0,1]]

class Tile:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.v = r * NUM_COLS + c
        self.img = loadImage(path + "/images/" + str(self.v) + ".png")
    
    def display(self):
        if self.v != 15:
            image(self.img, self.c * TILE_WIDTH, self.r * TILE_HEIGHT)
            noFill()
            stroke(0,0,0)
            strokeWeight(5)
            rect(self.c * TILE_WIDTH, self.r * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
    
    def swap(self, other):
        tmp_v = self.v
        self.v = other.v
        other.v = tmp_v
        
        tmp_img = self.img
        self.img = other.img
        other.img = tmp_img

class Puzzle(list):
    def __init__(self):
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                self.append(Tile(r,c))
        self.shuffle()
        
    def show_tiles(self):
        for tile in self:
            tile.display()
    
        r = mouseY//TILE_WIDTH
        c = mouseX//TILE_HEIGHT
        noFill()
        stroke(255,0,0)
        strokeWeight(5)
        rect(c * TILE_WIDTH, r * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
    
    def get_tile(self, r, c):
        for tile in self:
            if tile.r == r and tile.c == c:
                return tile
        return None
    
    def clicked(self):
        r = mouseY//TILE_WIDTH
        c = mouseX//TILE_HEIGHT
        tile = self.get_tile(r, c)
        for n in NEIGHBORS:
            neighbor_tile = self.get_tile(r + n[0], c + n[1])
            if neighbor_tile != None and neighbor_tile.v == 15:
                tile.swap(neighbor_tile)
    
    def check_win(self):
        for tile in self:
            if tile.r * NUM_COLS + tile.c != tile.v:
                return False
        return True
     
    def shuffle(self):
        empty_tile = self.get_tile(NUM_ROWS-1, NUM_COLS-1)
        
        for i in range(20):
            neighbor_tile = None
            while neighbor_tile == None:
                neighbor = NEIGHBORS[random.randint(0,len(NEIGHBORS)-1)]
                neighbor_tile = self.get_tile(empty_tile.r + neighbor[0], empty_tile.c + neighbor[1])
            
            empty_tile.swap(neighbor_tile)
            empty_tile = neighbor_tile
        
puzzle = Puzzle()

def setup():
    size(RESOLUTION, RESOLUTION)
    background(0,0,0)

def draw():
    background(0,0,0)
    puzzle.show_tiles()

def mouseClicked():
    puzzle.clicked()
    if puzzle.check_win() == True:
        print("GAME WON")




    
    
