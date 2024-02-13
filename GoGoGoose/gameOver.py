import pygame
from displayTime import *

def gameOver(score, screen):
    # cur_time = pygame.time.get_ticks()
    # goal_time = cur_time + 750
    
    # while cur_time <= goal_time:
    #     cur_time = pygame.time.get_ticks()
   
    # if cur_time > goal_time: 
    
    big_font = pygame.font.Font('font/Pixeltype.ttf', 80)
    big_sur = big_font.render("Game Over", False, "Black")
    big_rect = big_sur.get_rect(midtop = (500, 100))
    tiny_font = pygame.font.Font('font/Pixeltype.ttf', 40)
    scoreView = "Score: " + str(score)
    tiny_sur = tiny_font.render(scoreView, False, "Black")
    tiny_rect = tiny_sur.get_rect(midtop = (500, 300))

    home_sur = pygame.image.load('graphics/Home.png')
        
    screen.blit(home_sur, (0, 0))
    screen.blit(tiny_sur, tiny_rect)
    screen.blit(big_sur, big_rect)

        # print game over screen 
        # print score