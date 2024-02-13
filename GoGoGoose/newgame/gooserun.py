import pygame

'''
# starts pygame / initializes pygame
pygame.init()

# make window (width, height), for one frame
screen = pygame.display.set_mode((800, 400))

while True:
    # event loop (check for player input)
    for event in pygame.event.get():

        #if player hits x button, quit game
        if event.type == pygame.QUIT:
            pygame.quit()

    # draw all elements & update everything
    pygame.display.update() # updates display surface
'''