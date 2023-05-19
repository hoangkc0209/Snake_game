"""Module chứa đối tượng Wall, là tập hợp các ô vuông mà khi Snake chạm vào, game sẽ kết thúc"""
import pygame, sys, random
from pygame.locals import *
import setting as st

class Wall:
    def __init__(self, map):
        self.position = []
        if map == 1:
            for i in range(0, st.SCREEN_HEIGHT, st.UNIT):
                for j in range(0, st.SCREEN_WIDTH, st.UNIT):
                    if i == 0 or i == st.SCREEN_HEIGHT-st.UNIT:
                        self.position.append([j, i])
                    else:
                        if j == 0 or j == st.SCREEN_WIDTH-st.UNIT:
                            self.position.append([j, i])
        elif map == 2:
            for i in range(0, st.SCREEN_HEIGHT, st.UNIT):
                if i < st.SCREEN_HEIGHT*7//20 or i >= st.SCREEN_HEIGHT*13//20:
                    for j in range(0,st.SCREEN_WIDTH, st.UNIT):
                        if i == st.SCREEN_HEIGHT*7//20-st.UNIT or i == st.SCREEN_HEIGHT*13//20:
                            if j >= st.SCREEN_WIDTH//3 and j < st.SCREEN_WIDTH*2//3:
                                self.position.append([j, i])
                        elif i == 0 or i == st.SCREEN_HEIGHT-st.UNIT:
                            if j < st.SCREEN_WIDTH//3 or j >= st.SCREEN_WIDTH*2//3:
                                self.position.append([j, i])
                        else:
                            if j == 0 or j == st.SCREEN_WIDTH-st.UNIT:
                                self.position.append([j, i])
        elif map == 3:
            for i in range(0, st.SCREEN_HEIGHT, st.UNIT):
                for j in range(0, st.SCREEN_WIDTH, st.UNIT):
                    if i <= st.SCREEN_HEIGHT - st.SCREEN_HEIGHT//5 - st.UNIT and j == st.SCREEN_WIDTH//3 + st.UNIT:
                        self.position.append([j, i])
                    if i >= st.SCREEN_HEIGHT//5 and j == st.SCREEN_WIDTH - st.SCREEN_WIDTH//3 - 2 * st.UNIT:
                        self.position.append([j, i])
                    if i == st.SCREEN_HEIGHT//5 and j <= st.SCREEN_WIDTH//3 - 2 * st.UNIT:
                        self.position.append([j, i])
                    if i == st.SCREEN_HEIGHT - st.SCREEN_HEIGHT//5 - st.UNIT and j >= st.SCREEN_WIDTH - st.SCREEN_WIDTH//3 + st.UNIT:
                        self.position.append([j, i])
        elif map == 4:
            for i in range(0, st.SCREEN_HEIGHT, st.UNIT):
                for j in range(0, st.SCREEN_WIDTH, st.UNIT):
                    if i == 0 or i == st.SCREEN_HEIGHT-st.UNIT:
                        self.position.append([j, i])
                    if i <= st.SCREEN_HEIGHT//5 or i >= st.SCREEN_HEIGHT - st.SCREEN_HEIGHT//5 - st.UNIT:
                        if j == 0 or j == st.SCREEN_WIDTH-st.UNIT:
                            self.position.append([j, i])
                    if i == st.SCREEN_HEIGHT//5 + st.UNIT or i == st.SCREEN_HEIGHT - st.SCREEN_HEIGHT//5 - 2 * st.UNIT:
                        if j > st.SCREEN_HEIGHT//5 and j < st.SCREEN_WIDTH - st.SCREEN_HEIGHT//5 - st.UNIT:
                            self.position.append([j, i])
        elif map == 5:
            for i in range(0, st.SCREEN_HEIGHT, st.UNIT):
                for j in range(0, st.SCREEN_WIDTH, st.UNIT):
                    if i == st.SCREEN_HEIGHT//2 - st.UNIT:
                        if j <= st.SCREEN_WIDTH//2 - 4 * st.UNIT or j >= st.SCREEN_WIDTH//2:
                            self.position.append([j, i])
                    if i == st.SCREEN_HEIGHT - st.SCREEN_HEIGHT//4 - st.UNIT:
                        self.position.append([j, i])
                    if i <= st.SCREEN_HEIGHT//2 - 5 * st.UNIT:
                        if j == st.SCREEN_WIDTH//2:
                            self.position.append([j, i])
                    if i >= st.SCREEN_HEIGHT - st.SCREEN_HEIGHT//4 - st.UNIT:
                        if j == st.SCREEN_WIDTH//2:
                            self.position.append([j, i])


    def draw(self, surface):
        for point in self.position:
            img = pygame.image.load("assets/images/wall.png")
            img = pygame.transform.scale(img, (st.UNIT, st.UNIT))
            surface.blit(img, point)