"""Module khởi tạo âm thanh"""
import pygame
import os

pygame.mixer.pre_init(frequency=44100 , size = -16 , channels = 2 , buffer = 512)
pygame.mixer.init()

# def get_sound(filename):
#     return pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "sound", filename))

background1 = pygame.mixer.Sound("assets/sound/background1.mp3")
background2 = pygame.mixer.Sound("assets/sound/background2.mp3")
background3 = pygame.mixer.Sound("assets/sound/background3.mp3")
click = pygame.mixer.Sound("assets/sound/click.mp3")
eat = pygame.mixer.Sound("assets/sound/eat_fruit.wav")
gameover = pygame.mixer.Sound("assets/sound/gameover.mp3")
print('ĐÃ KHỞI TẠO ÂM THANH')