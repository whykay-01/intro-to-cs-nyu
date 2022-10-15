import random
import os

#global variables
RESOLUTION_X = 1280
RESOLUTION_Y = 720
path = os.getcwd()
BG = loadImage(path+"/assets/background.png")
BOSS_LEVEL = 4

# health kit class


class HealthKit():
    def __init__(self):
        self.x = random.randint(0, RESOLUTION_X/2 - 50)
        self.y = random.randint(0, RESOLUTION_Y - 50)
        self.r = 25
        self.img = loadImage(path + '/assets/health_kit.png')

    def display(self):
        image(self.img, self.x, self.y)

# laser class


class Laser():
    def __init__(self, x, y, img, xvel, yvel=0):
        self.x = x
        self.y = y
        self.r = 15
        self.img = img
        self.xvel = xvel
        self.yvel = yvel

# function to check whether laser has hit the enemy
    def hit(self):
        for enemy in game.enemies:
            if self.distance(enemy) <= self.r + enemy.r:
                game.enemies.remove(enemy)
                return True
# function to calculate the distance between laser and other object

    def distance(self, target):
        return ((self.x - target.x)**2 + (self.y - target.y)**2)**0.5

    def display(self):
        self.move()
        image(self.img, self.x, self.y)

    def move(self):
        self.x += self.xvel
        self.y += self.yvel
# method to track whether laser is off-screen

    def off_screen(self):
        if self.x >= RESOLUTION_X or self. x <= 0:
            return True

# Parent ship class


class Ship():
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.r = 0
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cooldown = 20
        self.cooldown_counter = 0
        self.laser_power = 0
        self.overheated = False

    def display(self):
        self.move()
        image(self.ship_img, self.x-20, self.y-20)
# shoot method with cooldown to not allow spamming

    def shoot(self, vel):
        if self.cooldown_counter >= self.cooldown and not self.overheated:
            laser = Laser(self.x+self.r, self.y+self.r, self.laser_img, vel)
            self.lasers.append(laser)
            self.cooldown_counter = 0
            self.laser_power+=30
# method to handle lasers' movement

    def move_lasers(self):
        for laser in self.lasers:
            laser.display()
        if laser.off_screen():
            self.lasers.remove(laser)

# player class, which inherits from Ship


class Player(Ship):
    def __init__(self, x, y, health=100):
        Ship.__init__(self, x, y, health)
        self.r = 45
        self.ship_img = loadImage(path + '/assets/player_ship.png')
        self.laser_img = loadImage(path + '/assets/player_laser.png')
        self.key_handler = {LEFT: False, RIGHT: False,
                            UP: False, DOWN: False, CONTROL: False}
        

# move method using up, down, right, left keys and ctrl for shooting
# player cannot move off-screen
    def move(self):
        if self.key_handler[UP]:
            self.y -= 10
        if self.key_handler[DOWN]:
            self.y += 10
        if self.key_handler[RIGHT]:
            self.x += 10
        if self.key_handler[LEFT]:
            self.x -= 10

        if self.key_handler[CONTROL]:
            self.shoot(20)

        if self.x < 0:
            self.x = 0
        elif self.x > RESOLUTION_X - 90:
            self.x = RESOLUTION_X - 90

        if self.y < 0:
            self.y = 0
        elif self.y > RESOLUTION_Y - 90:
            self.y = RESOLUTION_Y - 90
# update method to track whether player crashed into an enemy ship, if yes, then player loses 10hp

    def update(self):
        for enemy in game.enemies:
            if self.distance(enemy) <= self.r + enemy.r:
                game.enemies.remove(enemy)
                game.score += 50
                game.combo = 1
                self.health -= 10
# method to get the distance between player and other objects

    def distance(self, target):
        return ((self.x - target.x)**2 + (self.y - target.y)**2)**0.5

    def display(self):
        self.move()
        self.update()
        image(self.ship_img, self.x, self.y)


# enemy ship class which inherits from Ship
class Enemy(Ship):
    # dictionary to store ships' ship and laser images according to their color
    COLOR_MAP = {
        'red': (loadImage(path + '/assets/red_ship.png'), loadImage(path + '/assets/red_laser.png')),
        'green': (loadImage(path + '/assets/green_ship.png'), loadImage(path + '/assets/green_laser.png')),
        'blue':  (loadImage(path + '/assets/blue_ship.png'), loadImage(path + '/assets/blue_laser.png'))
    }

    def __init__(self, x, y, color, health=100):
        Ship.__init__(self, x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.r = 25
        self.cooldown = 120
        self.laser_vel = 20
# method to make enemy shoot periodically

    def shoot(self):
        if self.cooldown_counter >= self.cooldown and self.x < RESOLUTION_X:
            laser = Laser(self.x-self.r-10, self.y-self.r -
                          10, self.laser_img, -self.laser_vel)
            self.lasers.append(laser)
            self.cooldown_counter = 0

    def move(self, vel=5):
        self.x -= vel
# method to check if enemy is off-screen

    def off_screen(self):
        if self.x <= 0:
            return True

# final boss class which inherits from Ship


class FinalBoss(Ship):
    def __init__(self, x, y, health=1000):
        Ship.__init__(self, x, y, health)
        self.x = x
        self.y = y
        self.ship_img = loadImage(path + '/assets/final_boss.png')
        self.laser_images = {0: loadImage(path + '/assets/red_laser.png'),
                             1: loadImage(path + '/assets/green_laser.png'),
                             2: loadImage(path + '/assets/blue_laser.png')}
        self.r = 160
        self.vel = 0
        self.cooldown_counter = 30

    def move(self):
        if self.x > 920:
            self.x -= 5

    def display(self):
        self.move()
        image(self.ship_img, self.x, self.y-320)
        # Final Boss' health bar
        fill(255, 255, 255)
        textSize(40)
        text('Final Boss: ', 300, 680)
        fill(255, 0, 0)
        rect(525, 655, 200, 20)
        fill(0, 255, 0)
        rect(525, 655, 2*(self.health/10), 20)

    def shoot(self):
        self.xvel = random.randint(-30, -5)
        self.yvel = random.randint(-20, 20)
        if self.cooldown_counter >= self.cooldown and self.x < RESOLUTION_X:
            for i in range(3):
                laser = Laser(self.x, self.y+i*250-300,
                              self.laser_images[i], random.randint(-30, -5), random.randint(-20, 20))
                self.lasers.append(laser)
            self.cooldown_counter = 0

# game class, where all the events are handled


class Game():
    def __init__(self):
        self.player = Player(155, 315)
        # score variable to store gamescore
        self.score = 0
        # list of all enemies
        self.enemies = []
        # level variable to track when it's time for final stage of the game
        self.level = 0
        #combo counter
        self.combo = 1
        # how many ships will be spawned
        self.wave_length = 5
        self.bossStop = True
        # list of all health kits
        self.health_kits = []
        self.check_win = False
# method to check if the game is over
# game is over when player's health is 0

    def check_lose(self):
        if self.player.health == 0:
            return True
# method to display all the objects of the game

    def display(self):
        fill(255, 255, 255)
        textSize(40)
        text('Score: ' + str(game.score), 1000, 40)
        if self.bossStop:
            text('Level: ' + str(self.level), 1000, 80)
            text('Combo: ' + str(self.combo), 1000, 120)
        textSize(20)
        text('Navigate with arrow keys. Shoot with ctrl',500,20)
        textSize(40)
        # player's health bar
        text('Health: ', 20, 40)
        fill(255, 0, 0)
        rect(200, 15, 200, 20)
        fill(0, 255, 0)
        rect(200, 15, 2*self.player.health, 20)
        fill(255)
        text('Power: ', 20, 80)
        fill(255, 0, 0)
        rect(200, 55, 200, 20)
        fill(0,0,255)
        if self.player.overheated:
            fill(255,255,0)
        rect(200, 55, 200 - 2*self.player.laser_power, 20)
        self.player.display()
        self.player.cooldown_counter += 3
        #laser overheat mechanic
        if not self.player.laser_power == 0:
            self.player.laser_power -= 2.5
        elif self.player.laser_power < 0:
            self.player.laser_power = 0
        if self.player.laser_power == 0:
            self.player.overheated = False
        if self.player.laser_power == 100:
            self.player.overheated = True

        # if player reached the BOSS_LEVELx, then instantiate FinalBoss object
        if self.level == BOSS_LEVEL and self.bossStop:
            self.bossStop = False
            self.final_boss = FinalBoss(RESOLUTION_X+50, RESOLUTION_Y/2)
            self.final_boss.display()
        elif not self.bossStop:
            self.final_boss.cooldown_counter += 3
            self.final_boss.display()
            self.final_boss.shoot()
            for laser in self.final_boss.lasers:
                laser.display()
                # if enemy laser hit the player, player loses 10 hp
                if self.player.distance(laser) <= self.player.r:
                    self.player.health -= 10
                    try:
                        self.final_boss.lasers.remove(laser)
                    except:
                        continue
                    # if laser is off-screen, it disappears
                if laser.off_screen():
                    try:
                        self.final_boss.lasers.remove(laser)
                    except:
                        continue
            if self.final_boss.health <= 0:
                self.check_win = True
                self.score = self.score * 2
            # kills player if player crashes into boss
            if self.player.x >= self.final_boss.x-100:
                self.player.health = 0

# if it's not game's final stage, then level +1.

        elif len(self.enemies) == 0 and self.bossStop:
            self.level += 1
            self.wave_length += 5
# if new level is not BOSS_LEVEL then generate new enemy ships with random colors and in random positions
            if self.level != BOSS_LEVEL:
                for i in range(self.wave_length):
                    enemy = Enemy(random.randint(RESOLUTION_X, RESOLUTION_X+1500), random.randint(
                        100, RESOLUTION_Y-100), random.choice(['red', 'green', 'blue']))
                    self.enemies.append(enemy)
# if it's level 2 or higher generate a health kit
            if self.level >= 2 and len(self.health_kits) == 0:
                self.health_kits.append(HealthKit())

# health kits will be spawned at the beginning of new level starting from level 2
        for health_kit in self.health_kits:
            health_kit.display()
            # to use health kit, player has to zcollide with it
            if self.player.distance(health_kit) <= self.player.r + health_kit.r:
              # remove health kit after player used it
                self.health_kits.remove(health_kit)
              # health kit adds 30 hp, but if player's health is >= 70, then fill it up to 100
                if self.player.health >= 70:
                    self.player.health = 100
                else:
                    self.player.health += 30

        for enemy in self.enemies:
            enemy.cooldown_counter += 3
            enemy.shoot()
            if self.player.distance(enemy) <= self.player.r + enemy.r:
                self.enemies.remove(enemy)
                self.score += 50
                self.combo = 1
                self.player.health -= 10
            # handle enemy laser events
            for laser in enemy.lasers:
                laser.display()
            # if enemy laser hit the player, player loses 10 hp
                if self.player.distance(laser) <= self.player.r:
                    self.player.health -= 10
                    self.combo = 1
                    try:
                        enemy.lasers.remove(laser)
                    except:
                        continue
                # if laser is off-screen, it disappears
                if laser.off_screen():
                    try:
                        enemy.lasers.remove(laser)
                    except:
                        continue
            # if enemy passed all the way to the left side of the screen, it disappears but player loses 25 score points
            if enemy.off_screen():
                self.combo = 1
                try:
                    self.enemies.remove(enemy)
                except:
                    continue
                self.score -= 25
            enemy.display()

        # handle player's laser events
        for laser in self.player.lasers:
            laser.display()
            # if laser hit the enemy, enemy is destroyed and 100 score point are added. adds to score combo
            if laser.hit():
                self.score += 100*self.combo
                self.combo +=1
                try:
                    self.player.lasers.remove(laser)
                except:
                    continue
            # if laser is off-screen, it disappears
            if laser.off_screen():
                try:
                    self.player.lasers.remove(laser)
                except:
                    continue
            # if laser hits the final boss it will give him damage of 25hp
            if not self.bossStop and laser.x >= self.final_boss.x:
                self.final_boss.health -= 30
                try:
                    self.player.lasers.remove(laser)
                except:
                    continue


# method for screen when game is lost and display player's score


    def display_lose(self):
        fill(255, 0, 0)
        textSize(60)
        text('Game Over', 320, 180)
        fill(255, 255, 255)
        textSize(40)
        text('Final score: ' + str(game.score), 320, 300)
# method for screen when game is won and display player's score

    def display_win(self):
        fill(0, 255, 0)
        textSize(60)
        text('You Win', 320, 180)
        fill(255, 255, 255)
        textSize(40)
        text('Final score: ' + str(game.score), 320, 300)


game = Game()


def setup():
    size(RESOLUTION_X, RESOLUTION_Y)
    background(0, 0, 0)


def draw():
    if frameCount % 3 == 0:
        image(BG, 0, 0)
        if game.check_lose():
            game.display_lose()
        elif game.check_win:
            game.display_win()
        else:
            game.display()

# function handling key press events


def keyPressed():
    if keyCode == LEFT:
        game.player.key_handler[LEFT] = True

    if keyCode == RIGHT:
        game.player.key_handler[RIGHT] = True

    if keyCode == UP:
        game.player.key_handler[UP] = True

    if keyCode == DOWN:
        game.player.key_handler[DOWN] = True

    if keyCode == CONTROL:
        game.player.key_handler[CONTROL] = True

# function handling key release events


def keyReleased():
    if keyCode == LEFT:
        game.player.key_handler[LEFT] = False

    if keyCode == RIGHT:
        game.player.key_handler[RIGHT] = False

    if keyCode == UP:
        game.player.key_handler[UP] = False

    if keyCode == DOWN:
        game.player.key_handler[DOWN] = False

    if keyCode == CONTROL:
        game.player.key_handler[CONTROL] = False

# if the mouse is clicked check if the game is over
# if game is over then restart the game after mouse click, ignore otherwise


def mouseClicked():
    if game.check_lose() or game.check_win:
        global game
        game = Game()
