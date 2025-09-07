from sqlite3 import SQLITE_CREATE_INDEX
import pygame
from gameOver import *
from displayTime import *
from sys import exit
from time import sleep

def goose_running(): # animate running or display jumping
    global goose_sur, goose_index

    if goose_rect.bottom < 290: # if goose is in the air, display goose as jumping
        goose_sur = goose_jump
    else: # alternate between 2 goose animations
        goose_index += .1
        if goose_index >= len(goose_run): goose_index = 0
        goose_sur = goose_run[int(goose_index)]

# starts pygame
pygame.init() 
screen = pygame.display.set_mode((1000, 500)) # make a screen
pygame.display.set_caption('Go Go Goose!') # name window
clock = pygame.time.Clock() # make clock object

# make font sizes
my_font = pygame.font.Font('font/Pixeltype.ttf', 40)
score_font = pygame.font.Font('font/Pixeltype.ttf', 30)
big_font = pygame.font.Font('font/Pixeltype.ttf', 60)

# default settings
game_running = True
alive = True
score = 0
start_time = 0

# play background music
music = pygame.mixer.Sound('audio/BG_music.mp3') 
music.set_volume(.95) #between 0 and 1
music.play(loops = -1) # loop this sound forever!

# display background 
sky_sur = pygame.image.load('graphics/Sky.png')
ground_sur = pygame.image.load('graphics/Dirtt.png')
ground_rect = ground_sur.get_rect(bottomleft = (0, 500))
ground2_rect = ground_sur.get_rect(bottomleft = (1000, 500))
text_sur = my_font.render("Go Go Goose! :D", False, "Black")
text_rect = text_sur.get_rect(midtop = (500, 30))

# display both enemies (on top of e/o at start)
enemy_sur = pygame.image.load('graphics/enemy.png')
enemy_rect = enemy_sur.get_rect(bottomright = (1000, 360))
enemy_x = 1100
enemy2_sur = pygame.image.load('graphics/enemy.png')
enemy2_rect = enemy_sur.get_rect(bottomright = (1000, 360))
enemy2_x = 2000

# display goose, prep all animations
goose1_sur = pygame.image.load('graphics/GooseWithShoes.png').convert_alpha()
dead_sur = pygame.image.load('graphics/Deadgoose.png').convert_alpha()
goose_g = 0
goose2_sur = pygame.image.load('graphics/GooseWithShoes2.png').convert_alpha()
goose_run = [goose1_sur, goose2_sur]
goose_index = 0
goose_jump = goose2_sur = pygame.image.load('graphics/GooseWithShoes2.png').convert_alpha()

goose_sur = goose_run[goose_index]
goose_rect = goose_sur.get_rect(midbottom = (80, 350)) 
player_gravity = 0 # starts at 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if click exit button, exit game
            pygame.quit()
            exit()
        if game_running:
            if event.type == pygame.KEYDOWN: # make goose jump
                if event.key == pygame.K_SPACE and goose_rect.y == 290: # make sure goose not in air -- no flying
                    player_gravity = -23
                    score += 1
                    jump_sound = pygame.mixer.Sound("audio/jump.mp3")
                    jump_sound.set_volume(.5) #between 0 and 1
                    jump_sound.play()
                    
        else: # player has died :(
            if event.type == pygame.KEYDOWN: # and event.key == pygame.K_SPACE:
                game_running = True
                alive = True
                score = 0
                enemy_rect = enemy_sur.get_rect(bottomright = (1000, 360))
                enemy_x = 1100
                enemy2_rect = enemy2_sur.get_rect(bottomright = (1000, 360))
                enemy2_x = 2000
                goose_rect = goose_sur.get_rect(midbottom = (80, 350))
                goose_g = 0
                start_time = pygame.time.get_ticks()

    if game_running: # display all surfaces
        screen.blit(sky_sur,(0,0))
        screen.blit(ground_sur, ground_rect)
        screen.blit(ground_sur, ground2_rect)
        screen.blit(text_sur, text_rect)
        score_sur = score_font.render("Jumps: " + str(score), False, "Black")
        score_rect = score_sur.get_rect(midtop = (500, 80))
        screen.blit(score_sur, score_rect)
        cur_time = pygame.time.get_ticks() - start_time
        t_sur = score_font.render("Score: " + str(cur_time), False, "Black")
        t_rect = t_sur.get_rect(midtop = (500, 60))
        screen.blit(t_sur, t_rect)

        jump_sur = big_font.render("Press space to jump!", False, "Black")
        jump_rect = jump_sur.get_rect(midtop = (500, 120))
        if score == 0: screen.blit(jump_sur, jump_rect)

        enemy_rect.x -= 5 # move enemy to the right
        if enemy_rect.right <= 0:enemy_rect.left = 1000 # once off screen, move back

        enemy2_rect.x -= 5
        if enemy2_rect.right <= 0:enemy2_rect.left = 1333

        ground_rect.x -= 2 # first ground, moving 
        if ground_rect.left <= -1000: ground_rect.left = 1000 # once ground at end, move back
        ground2_rect.x -= 2
        if ground2_rect.left <= -1000: ground2_rect.left = 1000

        goose_rect.y += player_gravity  # player goes down
        if goose_rect.y < 290: player_gravity += 1
        if goose_rect.y > 290: goose_rect.y = 290
        goose_running()

        if alive ==  True: #display things
            screen.blit(goose_sur, goose_rect)
            screen.blit(enemy_sur, (enemy_rect))
            screen.blit(enemy2_sur, (enemy2_rect))

        if goose_rect.colliderect(enemy_rect) or goose_rect.colliderect(enemy2_rect): #player has died :(
            death_sound = pygame.mixer.Sound("audio/death.mp3")
            death_sound.set_volume(.5) #between 0 and 1
            death_sound.play()
            game_running = False
            alive = False
            screen.blit(sky_sur, (0, 0))
            screen.blit(ground_sur, ground_rect)
            screen.blit(ground_sur, ground2_rect)
            screen.blit(text_sur, text_rect)
            screen.blit(enemy_sur, (enemy_rect))
            screen.blit(enemy2_sur, (enemy2_rect))
            screen.blit(dead_sur, goose_rect)
            screen.blit(score_sur, score_rect)
            screen.blit(t_sur, t_rect)
            key_sur = big_font.render("Rip :( Press any key to play again", False, "Black")
            key_rect = key_sur.get_rect(midtop = (500, 120))
            screen.blit(key_sur, key_rect)

    pygame.display.update()
    clock.tick(50) # no faster than 50 fps