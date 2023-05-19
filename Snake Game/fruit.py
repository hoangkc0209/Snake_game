"""Module chứa đối tượng Fruit, là một ô vuông được sinh ngẫu nhiên (không trùng với các ô có Wall và Snake), khi chạm vào Fruit, Snake được tăng 1 điểm và 1 chiều dài"""
import pygame, sys, random
from pygame.locals import *
import setting as st

class Fruit:
    def __init__(self, wall, snake):
        self.position = random.choice([p for p in st.GRID if (p not in wall) and (p not in snake)])
        img = pygame.image.load(random.choice(["assets/images/apple.png", "assets/images/banana.png", "assets/images/grape.png"])).convert_alpha()
        self.img = pygame.transform.scale(img, (st.UNIT, st.UNIT))

    def draw(self, surface):
        surface.blit(self.img, (self.position[0] , self.position[1]))