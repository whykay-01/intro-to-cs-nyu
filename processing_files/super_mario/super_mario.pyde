add_library('minim')
import os, random

path = os.getcwd()
player = Minim(this)

class Creature:
    def __init__(self, x, y, r, g, img, img_w, img_h, slices):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.vy = 1
        self.vx = 0
        self.img = loadImage(path + "/images/" + img)
        self.img_w = img_w
        self.img_h = img_h
        self.slices = slices
        self.slice = 0
        self.dir = RIGHT
        
    def gravity(self):
        if self.y + self.r >= self.g: 
            self.vy = 0
        else:
            self.vy = self.vy + 0.4
            if self.y + self.r + self.vy > self.g:
                self.vy = self.g - (self.y + self.r)
        
        for platform in game.platforms:
            if self.y + self.r <= platform.y and self.x + self.r >= platform.x and self.x - self.r <= platform.x + platform.w:
                self.g = platform.y
                break
            else:
                self.g = game.g
                
    def update(self):
        self.gravity()
        self.y = self.y + self.vy
        self.x = self.x + self.vx
        
    def display(self):
        self.update()
        strokeWeight(0)
        fill(255, 0, 0)
        # ellipse(self.x, self.y, self.r*2, self.r*2)
        if self.dir == RIGHT:
            image(self.img, self.x-self.img_w//2 - game.x_shift, self.y-self.img_h//2, self.img_w, self.img_h, self.slice * self.img_w, 0, (self.slice + 1) * self.img_w, self.img_h)
        elif self.dir == LEFT:
            image(self.img, self.x-self.img_w//2 - game.x_shift, self.y-self.img_h//2, self.img_w, self.img_h, (self.slice + 1) * self.img_w, 0, self.slice * self.img_w, self.img_h)

class Mario(Creature):
    def __init__(self, x, y, r, g):
        Creature.__init__(self, x, y, r, g, "mario.png", 100, 70, 11) #super().__init__(x, y, r, g)
        self.key_handler = {LEFT:False, RIGHT:False, UP:False}
        self.jump_sound = player.loadFile(path + "/sounds/jump.mp3")
        self.alive = True
        
    def update(self):
        self.gravity()
        
        if self.key_handler[LEFT] == True:
            self.vx = -10
            self.dir = LEFT
        elif self.key_handler[RIGHT] == True:
            self.vx = 10
            self.dir = RIGHT
        else:
            self.vx = 0
        
        if self.key_handler[UP] == True and self.y + self.r == self.g:
            self.vy = -10
            self.jump_sound.rewind()
            self.jump_sound.play()
        
        self.y = self.y + self.vy
        self.x = self.x + self.vx

        if frameCount % 6 == 0 and self.vx != 0 and self.vy == 0:
            self.slice = (self.slice + 1) % self.slices
        elif self.vx == 0:
            self.slice = 0
        
        for gomba in game.gombas:
            if self.distance(gomba) <= self.r + gomba.r:
                if self.vy > 0:
                    game.gombas.remove(gomba)
                    self.vy = -8
                else:
                    print("Game over")
                    game.gombas = []
                    game.platforms = []
                    self.vy = -15
                    self.g = 1000
                    self.alive = False
        
        if self.x-self.r < 0:
            self.x = self.r
            
        if self.x >= game.w//2:
            game.x_shift += self.vx
        elif self.x < game.w//2:
            game.x_shift = 0
            
    def distance(self, other):
        distance = ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
        return distance

class Gomba(Creature):
    def __init__(self, x, y, r, g, xl, xr):
        Creature.__init__(self, x, y, r, g, "gomba.png", 70, 70, 5)
        self.vx = random.randint(1, 7)
        self.xl = xl
        self.xr = xr
        
    def update(self):
        self.gravity()
        
        if frameCount % 6 == 0 and self.vy == 0:
            self.slice = (self.slice + 1) % self.slices
        
        if self.x < self.xl:
            self.vx = self.vx * -1
            self.dir = RIGHT
        elif self.x > self.xr:
            self.vx = self.vx * -1
            self.dir = LEFT
        
        self.y = self.y + self.vy
        self.x = self.x + self.vx

class Platform:
    def __init__(self, x, y, w, h, img):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = loadImage(path + "/images/" + img)
        
    def display(self):
        # fill(0, 125, 0)
        # rect(self.x, self.y, self.w, self.h)
        image(self.img, self.x - game.x_shift, self.y, self.w, self.h)
        
class Game:
    def __init__(self, w, h, g):
        self.w = w
        self.h = h
        self.g = g
        self.mario = Mario(100, 100, 35, self.g)
        self.x_shift = 0
        self.bg_sound = player.loadFile(path + "/sounds/background.mp3")
        self.bg_sound.loop()
        self.platforms = []
        self.platforms.append(Platform(200, 500, 200, 50, "platform.png"))
        self.platforms.append(Platform(500, 400, 200, 50, "platform.png"))
        self.platforms.append(Platform(800, 300, 200, 50, "platform.png"))
        
        self.platforms.append(Platform(1400, 500, 200, 50, "platform.png"))
        self.platforms.append(Platform(1700, 400, 200, 50, "platform.png"))
        self.platforms.append(Platform(2000, 300, 200, 50, "platform.png"))
        
        self.gombas = []
        for i in range(5):
            self.gombas.append(Gomba(random.randint(200, 800), 100, 35, self.g, 200, 800))
            self.gombas.append(Gomba(random.randint(1500, 2000), 100, 35, self.g, 1500, 2000))
        
        self.bg_imgs = []
        for i in range(5, 0, -1):
            self.bg_imgs.append((loadImage(path + "/images/layer_0" + str(i) + ".png")))
        
    def display(self):
        # fill(0,125,0)
        # rect(0, self.g, self.w, self.h)
        
        x = 0
        cnt = 0
        for bg in self.bg_imgs:
            if cnt == 0:
                x = self.x_shift//4
            elif cnt == 1:
                x = self.x_shift//3
            elif cnt == 2:
                x = self.x_shift//2
            elif cnt == 3:
                x = self.x_shift
            cnt += 1
            width_right = x % self.w
            width_left = self.w - width_right
            image(bg, 0, 0, width_left, self.h, width_right, 0, self.w, self.h)
            image(bg, width_left, 0, width_right, self.h, 0, 0, width_right, self.h)
        
        for platform in self.platforms:
            platform.display()
        
        for gomba in self.gombas:
            gomba.display()
        

        self.mario.display()

game = Game(1280, 720, 585)

def setup():
    size(game.w, game.h)
    background(255,255,255)

def draw():
    background(255,255,255)
    game.display()
    
def keyPressed():
    if keyCode == LEFT:
        game.mario.key_handler[LEFT] = True
    elif keyCode == RIGHT:
        game.mario.key_handler[RIGHT] = True
    elif keyCode == UP:
        game.mario.key_handler[UP] = True

def keyReleased():
    if keyCode == LEFT:
        game.mario.key_handler[LEFT] = False
    elif keyCode == RIGHT:
        game.mario.key_handler[RIGHT] = False
    elif keyCode == UP:
        game.mario.key_handler[UP] = False

def mouseClicked():
    global game
    if game.mario.alive == False:
        game.bg_sound.close()
        game = Game(1280, 720, 585)
    
    
