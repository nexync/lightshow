import pygame

def sleigh(starttime):
    pygame.mixer.init()
    pygame.mixer.music.load("sleigh.mp3")
    pygame.mixer.music.play(loops = 1, start = starttime)
