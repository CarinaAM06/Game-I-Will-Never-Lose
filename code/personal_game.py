# Game I Will Never Lose
# Carina Almeida Marques

#=======================================================================================

# Creating initial game structure
import pygame
pygame.init()

#=======================================================================================


# Creating game window
Screen_width = 1000
Screen_height = 600

screen = pygame.display.set_mode((Screen_width, Screen_height))
pygame.display.set_caption("Fighter")

# load background image
bg_image = pygame.image.load("C:/game/code/photos/america_dog.jpg").convert_alpha()

# function for drawing background
def draw_bg():
    screen.blit(bg_image,(0,0))
#=======================================================================================


# Creatig game loop
run = True
while run:

    # draw background
    draw_bg()

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update display
    pygame.display.update()
#=======================================================================================



# Exiting the game
pygame.quit()

#=======================================================================================


