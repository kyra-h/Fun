import pygame
from gameOver import *
from displayTime import *
from sys import exit


# starts pygame
pygame.init() 
screen = pygame.display.set_mode((1000, 500)) # make a screen
pygame.display.set_caption('Go Go Goose!') # name window
clock = pygame.time.Clock() # make clock object
my_font = pygame.font.Font('font/Pixeltype.ttf', 40)
score_font = pygame.font.Font('font/Pixeltype.ttf', 30)
game_running = True
alive = True
score = 0
start_time = 0

sky_sur = pygame.image.load('graphics/Sky.png')
ground_sur = pygame.image.load('graphics/Dirtt.png')
ground_rect = ground_sur.get_rect(bottomleft = (0, 500))
text_sur = my_font.render("Go Go Goose! :D", False, "Black")
text_rect = text_sur.get_rect(midtop = (500, 30))

enemy_sur = pygame.image.load('graphics/enemy.png')
enemy_rect = enemy_sur.get_rect(bottomright = (1000, 350))
enemy_x = 1100

goose_sur = pygame.image.load('graphics/GooseWithShoes.png').convert_alpha()
dead_sur = pygame.image.load('graphics/Deadgoose.png').convert_alpha()
goose_rect = goose_sur.get_rect(midbottom = (80, 350))
goose_g = 0

player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_running:
            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_SPACE and goose_rect.bottom < 350:
                    # player_gravity = -20
                if event.key == pygame.K_SPACE:
                    player_gravity = -25
                    score += 1
                    
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_running = True

    if game_running:
        screen.blit(sky_sur,(0,0))
        #screen.blit(ground_sur,(0, 150))
        screen.blit(ground_sur, ground_rect)
        screen.blit(text_sur, text_rect)
        score_sur = score_font.render("Jumps: " + str(score), False, "Black")
        score_rect = score_sur.get_rect(midtop = (500, 100))
        cur_time = pygame.time.get_ticks() - start
        t_sur = score_font.render("Score: " + str(cur_time), False, "Black")
        t_rect = t_sur.get_rect(midtop = (500, 70))
        screen.blit(t_sur, t_rect)
        screen.blit(score_sur, score_rect)

        displayTime()

        # enemy_x -= 5
        # if enemy_x < -200: enemy_x = 1100

        enemy_rect.x -= 5
        if enemy_rect.right <+ 0:enemy_rect.left = 1000

        goose_rect.y += player_gravity
        if goose_rect.y < 290: player_gravity += 1.1

        if goose_rect.y > 290: goose_rect.y = 290
        
        if alive ==  True:
            screen.blit(goose_sur, goose_rect)
            screen.blit(enemy_sur, (enemy_rect))


        if goose_rect.colliderect(enemy_rect):
            game_running = False
            alive = False
            screen.blit(sky_sur, (0, 0))
            screen.blit(ground_sur, ground_rect)
            screen.blit(enemy_sur, (enemy_rect))
            screen.blit(dead_sur, goose_rect)
            screen.blit(score_sur, score_rect)
            screen.blit(t_sur, t_rect)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_running = True
                    score = 0
                    alive = True
                    


        # if alive == False and game_running == False:
        #     cur_time = pygame.time.get_ticks()
        #     goal_time = cur_time + 10
    
        #     while cur_time <= goal_time:
        #         cur_time = pygame.time.get_ticks()

        #     if cur_time > goal_time:
        #         gameOver(score, screen)


    pygame.display.update()
    clock.tick(50) # no faster than 50 fps