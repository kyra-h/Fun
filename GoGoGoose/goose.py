from sqlite3 import SQLITE_CREATE_INDEX
import pygame
from gameOver import *
from displayTime import *
from sys import exit
from time import sleep

class Character:
    def __init__(self, s1 = 0, s2 = 0, r = 0, x = 0, y = 0):
        self.sur1 = s1
        self.sur2 = s2

    def getSur1(self):
        return self.sur1

    def getSur2(self):
        return self.sur2

    def getGif(self, index):
        gif = [self.sur1, self.sur2]
        self.index = index
        return gif[self.index]

    def getRect(self, index):
        self.rect = self.getGif(self, index).get_rect(bottomright = (self.x, self.y))
        return self.rect

class Goose(Character):
    def __init__(self, s1 = 0, s2 = 0, r = 0, x = 0, y = 0, a = True, g = 0):
        self.alive = a
        self.gravity = g
    
    def getSur1(self):
        return self.sur1

    def getSur2(self):
        return self.sur2

    def getGif(self, index):
        gif = [self.sur1, self.sur2]
        self.index = index
        return gif[self.index]

    def getRect(self, index):
        self.rect = self.getGif(self, index).get_rect(bottomright = (self.x, self.y))
        return self.rect

    def setAlive(self, a):
        self.alive = a
    
    def getAlive(self):
        return self.alive

    def jump(self, score):
        self.gravity = -23
        score += 1
        jump_sound = pygame.mixer.Sound("audio/jump.mp3")
        jump_sound.set_volume(.5) #between 0 and 1
        jump_sound.play()
        return score
