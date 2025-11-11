import pygame, random

# Initialize pygame
pygame.init()

# Set display window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
display_surface = pygame.display.set_mode(size)
pygame.display.set_caption("~~SNEKE~~")

# Set FSP and clock
# todo: make a variable (constant) called FPS and initialize to 20
FPS = 20
clock = pygame.time.Clock()

# Set game values
# TODO: make a variable (constant) named SNAKE_SIZE and initialize to 20
SNAKE_SIZE = 20

# TODO: make a variable named head_x and assignment half of the WINDOW_WIDTH to it. use integer division // (i.e. 11/ 2 is 5.5, 11//2 is 5
head_x = WINDOW_WIDTH / 2
# TODO: make a variable named head_y and assign half og the WINDOW_HEIGHT + 100 to it. use integer division //
head_y = WINDOW_HEIGHT / 2 + 100

# TODO: make a variable named snake_dx and assign 0 to it
snake_dx = 0
# TODO: repeat for a variable named snake_dy
snake_dy = 0

#TODO: make a variable named score and assign 0 to it
score = 0

# Set colors
GREEN = (0, 255, 0) # (r, g , b)
# TODO: make a DARKGREEN color with rgb (10,50,10)
DARKGREEN = (10, 150, 10)
#TODO make a RED
RED = (255, 0, 0)
# TODO: make a DARKGREEN with rgb of (150, 0, 0)
DARKRED = (150, 0, 0)
# TODO: make a WHITE
WHITE = (255, 255, 255)

# Set fonts
font = pygame.font.SysFont('gabriola', 48)
# Set text
title_text = font.render("~~Snake~~", True, GREEN, DARKRED) #make a text object
title_rect = title_text.get_rect() # gets the box containing the text object
title_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2) # places the box containing the text object's center to the middle of the screen.

score_text = font.render("Score: 0 " + str(score), True, GREEN, DARKRED)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

game_over_text = font.render("GAMEOVER", True, GREEN, DARKRED)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to play again", True, RED, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

# Set sounds and music
pick_up_sound = pygame.mixer.Sound("pickup_sound.wav")
# Set images (in this case, use simple rects...so just create their coordinates)
# For a rectangle you need (top-left x, top-left y, width, height)
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)


head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)
# The main game loop
running = True
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move the snake

    # Add the head coordinate to the first index of the body coordinate list
    # This will essentially move all the snakes body by one position in the list

    # Update the x,y position of the snakes head and make a new coordinate

    # Check for game over

    # Check for collisions

    # Update HUD

    # Fill the surface

    # Blit HUD

    # Blit assets

    # Update display and tick clock

# End the game
pygame.quit()
