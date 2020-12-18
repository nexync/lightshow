import pygame

def sleigh(starttime):
    pygame.mixer.init()
    pygame.mixer.music.load("sleigh.mp3")
    pygame.mixer.music.play(loops = 1, start = starttime)

def phantom(starttime):
    pygame.mixer.init()
    pygame.mixer.music.load("phant.mp3")
    pygame.mixer.music.play(loops = 1, start = starttime)