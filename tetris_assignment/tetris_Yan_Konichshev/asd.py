# Yan Konichshev / Intro to CS / Third homework assignment

import os, random

NUM_ROWS = 20
NUM_COLS = NUM_ROWS / 2
BLOCK_WIDTH = 20
BLOCK_HEIGHT = BLOCK_WIDTH
RESOLUTION = NUM_ROWS * BLOCK_WIDTH
COLORS = [(255, 51, 52), (12, 150, 228), (30, 183, 66), (246, 187, 0), (76, 0, 153), (255, 255, 255), (0,0,0)]
STEP = 1



class Block:
    def __init__(self, row_coordinate, col_coordinate, color_1):
        self.row_coordinate = row_coordinate
        self.col_coordinate = col_coordinate
        self.color_1 = color_1
        self.move = 0 #this is the attribute that is responsible for the block movement in the horizontal axis
    
    # function that calls the     
    
    def movement(self):
        if self.move and self.col_coordinate + self.move >= 0 and self.col_coordinate + self.move < \
            NUM_COLS:
            self.col_coordinate += self.move
    
    # checks whether the movement is OK to implement (with taking into the consideration the barriers)    
    
    def update(self, allow_move):
        if allow_move:
            self.movement()
        self.row_coordinate = self.row_coordinate + STEP
    
    def display(self):
        fill(self.color_1[0], self.color_1[1], self.color_1[2])
        stroke(180,180,180)
        strokeWeight(1)
        rect(self.col_coordinate * BLOCK_WIDTH, self.row_coordinate * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)
        

class Game(list):
    def __init__(self, speed = 0):
        self.blocks = []
        self.last_block = Block(0, random.randint(0, NUM_COLS - 1), COLORS[random.randint(0, 6)]) ####################
        self.speed = speed
        self.unfilled_cols = []
        self.game_over = False
        self.score = 0
        
        for i in range(0, NUM_COLS):
            self.unfilled_cols.append(i)
        
   
   # checks whether 4 blocks are on top of each other
   
    def inc_score(self):
        count = 0
 #       global score
        blocks = []
    
        for index in range(len(self.blocks)):
            block = self.blocks[index]
            for i in range(1,4):
                if block.row_coordinate == self.last_block.row_coordinate+i and self.last_block.col_coordinate == block.col_coordinate:
                    if self.last_block.color_1 == block.color_1:
                        blocks.append(block)
                        count += 1

        if count == 3:
            count = 0
            temp_array = []
            for block in self.blocks:
                if block in blocks:
                    continue
                temp_array.append(block)
            del temp_array[temp_array.index(self.last_block)]    
            self.blocks = temp_array
            self.speed = 0
            self.score += 1
            print(self.score)   
            print("win")
      
          
   
    # check the free column
    
    # checks whether the there is a lower block or the board restriction there
    
    def check_next(self):
        for block in self.blocks[::-1]:
            if block.col_coordinate == self.last_block.col_coordinate and block.row_coordinate <= self.last_block.row_coordinate + STEP:
                return False
        return True
    
    # prevents from the accidental replacement of the block from the right or the left (or even diagonally)
    
    def check_horizontal(self):
        for block in self.blocks[::-1]:
            if block.row_coordinate == self.last_block.row_coordinate or block.row_coordinate == self.last_block.row_coordinate + 1 \
                and self.last_block.col_coordinate + self.last_block.move == block.col_coordinate:
                return False
        return True
    

    
        
            
        
                         
    def display(self):
        
    # checks whether the board is full, so the game is over
    
        if len(self.blocks) == NUM_ROWS * NUM_COLS:
        
            self.game_over = True
        
        for c in range(1, NUM_COLS):
                stroke(180,180,180)
                line(c * BLOCK_WIDTH, 0, c * BLOCK_WIDTH, RESOLUTION)
        for r in range(1, NUM_ROWS):
                stroke(180,180,180)
                line(0, r * BLOCK_HEIGHT, RESOLUTION // 2, r * BLOCK_HEIGHT)
        
        if self.last_block.row_coordinate + STEP < NUM_ROWS and self.check_next():
            self.last_block.update(self.check_horizontal())
            
    # increasing the speed of the game

        else:
            self.speed += 0.25
            self.blocks.append(self.last_block)
            self.inc_score()
            
            if self.last_block.row_coordinate == 0:
                self.unfilled_cols.remove(self.last_block.col_coordinate)
            
            if len(self.unfilled_cols) == 0:
                self.game_over = True
            else:
                self.last_block = Block(0, random.choice(self.unfilled_cols), COLORS[random.randint(0, 6)]) ###############
        self.last_block.display()
        
        for block in self.blocks:
            block.display()
        

game = Game()

                
def setup():
    size(RESOLUTION/2, RESOLUTION)
    background(210,210,210)
    
    
def draw():
    if game.game_over == True: 
        textSize(15)
        fill(180, 180, 180)
        text("GAME OVER", 60, 200)
        textAlign(LEFT)
        text("Score: "+ str(game.score), (0.66 * NUM_COLS) * BLOCK_WIDTH , 15)
        textAlign(LEFT)
        
        
        
    else:    
        if frameCount % (max(1, int(8 - game.speed))) == 0 or frameCount == 1:
            background(210,210,210)
            game.display()
            textSize(15)
            fill(0, 0, 0)
            text("Score: "+ str(game.score), (0.66 * NUM_COLS) * BLOCK_WIDTH , 15)
    

def keyPressed():
    if keyCode == LEFT:
        game.last_block.move = -1
    elif keyCode == RIGHT:
        game.last_block.move = 1

        
def keyReleased():
    if keyCode == LEFT:
        game.last_block.move = 0
    elif keyCode == RIGHT:
        game.last_block.move = 0

def mouseClicked():
    global game
    if game.game_over == True:
        print("mouseClicked")
        game = Game()
        
     
        


# create the algorithm that checks for the win (take one from my previous assignment)
# implement the score in the upper right corner of the board
# implement the condition for the termination of the game (when the board is full)

    
