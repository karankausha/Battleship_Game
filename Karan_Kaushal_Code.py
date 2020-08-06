"""
Python code for Battleship Game using Pygame Library.

Game Control Keys::
Right Key :: Right Movement of ship
Left Key :: Left Movement of ship
SpaceBar :: To fire Bullets
"""

"""
##importing libraries like Pygame, random, math.##

"""
import pygame  # Python Game Library
import random  # Library for random enemies
import math
from pygame import mixer  # for adding sound into game

pygame.font.init()  # Initializing python font
pygame.mixer.init()

"""
Creating window for game display
"""

window = pygame.display.set_mode((800, 600))  # Window Size

"""
Creating enemy and storing it in a list for multiple enemies on screen using for loop.
"""

enemy_image_list = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 20

for i in range(num_of_enemies):  # Loop for shoiwng random enemies on screen
    enemy_image_list.append(pygame.image.load("ufo.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)
""""
Defining bullets variable.
When bullet_state="OFF" Bullet is not active i.e Initially it is OFF
"""
bulletX = 0
bulletY_change = 10  ##Speed of bullet
bulletY = 480
bullet_state = "OFF"  ## Bullet is not fired i.e. it is not active

"""
Creating Game Class in which i have defined all the images for background, spaceship, enemies, bullets, background music.
"""


class Images():  # Game Class
    def __init__(self):
        self.title = pygame.display.set_caption("Battleship")  # Game Title
        self.icon = pygame.image.load('icon.png')  # Game Icon
        self.background = pygame.image.load('background.png')  # Background Image
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption("Battleship")
        mixer.music.load('background_music.wav')  # Background Music
        mixer.music.play(-1)  # playing continuously


"""
Creating ship class in which i have defined all the ship coordinates.
shipX = value of X Coordinate of screen
shipY= Value of Y Coordinate of screen
"""


class Ship():  # Ship Class
    def __init__(self, shipX, shipY):
        self.shipX = shipX
        self.shipY = shipY
        self.shipX_change = 0
        self.ship_image = pygame.image.load("Ship.png")  # ship image
        window.blit(self.ship_image, (self.shipX, self.shipY))


"""
Bullets function to display bullets on screen. 
"""


def Bullets(x, y):
    global bullet_state  # making bullet_state global variable to call inside the function
    bullet_image = pygame.image.load("bullet.png")
    bullet_state = "ON"  # bullet_state= Active
    window.blit(bullet_image, (x + 16, y + 10))


def enemy(x, y, i):  # enemy functin to show enemies on screen
    window.blit(enemy_image_list[i], (x, y))


"""
creating Hit function
It will tell when the collision between bullet and enemy happens.
so using math library applying square root function to find the distance between enemy and bullet.
and if distance is less that 27 pixels it will return True and bullet will hit the enemy.
"""


def Hit(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(
        (math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))  # to find distance between bullet and enemy
    if distance < 27:
        return True
    else:
        return False


"""
creating score class to show scores on the screen for the player.
Here we are showing score on top top left of window.
"""


class Score():
    def __init__(self, scoreX, scoreY, score_value):
        self.score_value = score_value
        self.scoreX = scoreX  # Score position window coordinates
        self.scoreY = scoreY
        self.font = pygame.font.Font(None, 32)
        self.text = self.font.render("SCORE :" + str(self.score_value), True, (255, 255, 255))  # Typecasting for score
        window.blit(self.text, (self.scoreX, self.scoreY))


"""
creating Game_Over class to define when the Game will get over.
Game gets over when the enemy reaches on the player side. and as result it will show GAMEOVER written on the screen.
"""


class Game_Over():          #GameOver Class
    def __init__(self):
        game_over_font = pygame.font.Font(None, 100)
        over_text = game_over_font.render("GAME OVER", True, (0, 0, 0))
        window.blit(over_text, (250, 250))


"""
Here i have created main function where all the game classes are called and working of game is done.
"""


# mainloop
def main():
    root = Images()  # calling Game class
    root2 = Ship(385, 480)  # Ship class to show ship on screen with X and Y coordinates
    score = Score(10, 10, 0)  # Score class to show score on the screen
    over = Game_Over()  # Game Over class

    """
    Declaring Global variables so that i can call them inside Main function.
    """
    global enemyX_change
    global enemyY
    global enemyX
    global window
    global bulletY_change
    global bullet_state
    global bulletY
    global bulletX

    """
    To show everything continuously on screen i have created while which will run infinitely till the Game Window remains open. 
    """
    running = True
    while running:
        window.fill((255, 0, 0))  # To add colour to background
        window.blit(root.background, (0, 0))  # Adding Background image
        for event in pygame.event.get():  # For pygame Window
            if event.type == pygame.QUIT:  ## if loop for Quit if we close the window Game Stops
                running = False
            """
            Game controls
            Pressing Right Arrow key moves Ship towards Right.
            Pressing Left Arrow key moves ship to Left
            Pressing SpaceBar fires the bullets.
            """
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # Pressing Left arrow key on keyboard
                    root2.shipX_change = -5
                if event.key == pygame.K_RIGHT:  # Pressing Right Arrow Key on key board
                    root2.shipX_change = 5
                if event.key == pygame.K_SPACE: # Pressing SpaceBar Key on Keyboard
                    bulletX = root2.shipX
                    Bullets(bulletX, bulletY)   # Calling Bullets Function to fire Bullets
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    root2.shipX_change = 0
        """
        Creating Boundary for the spaceship so that it does not go out of screen when we move it to left or right.
        """
        root2.shipX += root2.shipX_change
        if root2.shipX <= 0:  # creating boundry for ship on screen
            root2.shipX = 0
        elif root2.shipX >= 736:
            root2.shipX = 736
        """
        Calling GameOver class under for and IF loop. I.e when enemies comes in the spaceship region or when spaceship
        is hit by enemy Game will get over. Displaying Game Over on the screen.
        """

        for i in range(num_of_enemies):
            if enemyY[i] >= 480:   # when enemy reaches 480 pixels on screen Game gets over.
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                Game_Over()       # GameOver class being called
                break             # Break from the enemy loop and show GameOver on the screen
            """
            Creating Boundary for Enemies on the screen. So that they don't go off the screen when they move around.
            """


            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 4
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -4
                enemyY[i] += enemyY_change[i]

            collision = Hit(enemyX[i], enemyY[i], bulletX, bulletY)  # calling hit function using a variable collision
            if collision:  # loop if collision occurs
                collison_sound = mixer.Sound('died_music.wav')      # sound for collision between enemy and bullet
                collison_sound.play()
                bulletY = 480               # reset the bullet to starting point
                bullet_state = "OFF"
                score.score_value += 1  # increment the score by 1
                #print(score.score_value)
                enemyX[i] = random.randint(0, 735)  # enemy will reset to random location after hit
                enemyY[i] = random.randint(50, 150)
            enemy(enemyX[i], enemyY[i], i)

        """
        Bullet Movement dynamics so that bullet is fired from top of the space ship only.
        """
        if bulletY <= 0:  # for bullet movement
            bulletY = 490
            bullet_state = "OFF"    # bullet is not fired
        if bullet_state is "ON":    # when bullet is fired i.e. SpaceBar is pressed
            sound_bullet = mixer.Sound('laser_music.wav') # bullet sound
            sound_bullet.play()
            Bullets(bulletX, bulletY)           # calling bullet function
            bulletY -= bulletY_change
        Score(score.scoreX, score.scoreY, score.score_value)        #calling score class
        Ship(root2.shipX, root2.shipY)          # calling ship class
        pygame.display.update()  # To keep update screen window
if __name__ == '__main__':
    main()