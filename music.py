import pygame

def sleigh():
    pygame.mixer.init()
    pygame.mixer.music.load("sleigh.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
