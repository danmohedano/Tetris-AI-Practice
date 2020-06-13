# import the pygame module, so you can use it
import pygame
import time
from classes.Grid import Grid
from classes.Piece import Piece

GRAVITY_SPEEDS = [48, 43, 38, 33, 28, 23, 18, 13, 8, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FRAMES = 0
MAIN_LEVEL = 0

# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("Tetris")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    # define a variable to control the main loop
    running = True
    
    game = Grid(MAIN_LEVEL) 

    # main loop
    while running:
        if (game.GAME_OVER == 0 and game.PAUSE == 0):
            time.sleep(0.025)
            FRAMES = (FRAMES + 1) % GRAVITY_SPEEDS[game.getLevel()]
            if (FRAMES == 0):
                game.gravity()
            game.draw()
        elif (PAUSE == 1):
            textsurface = game.font.render("PAUSE", False, pygame.Color("white"))
            screen.blit(textsurface, (Grid.OFFSET + (Grid.BLOCK_DIM*(Grid.GW/2 - 2)), Grid.OFFSET + (Grid.BLOCK_DIM*Grid.GH/2)))


        pygame.display.flip()
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
