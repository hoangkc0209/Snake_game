"""Module chứa đối tượng Snake với các thuộc tích: màu sắc, độ dài,... và các phương thức: định hướng, di chuyển, tạo hình"""
import pygame, sys, random, sound
from pygame.locals import *
import setting as st

UP = (0, -st.UNIT, 270)
DOWN = (0, st.UNIT, 90)
RIGHT = (st.UNIT, 0, 180)
LEFT = (-st.UNIT, 0, 0)

class Snake:
    def __init__(self, map):
        self.color = (148, 57, 107)
        self.direction = RIGHT
        if map == 3:
            self.direction = UP
        self.body = [[st.SCREEN_WIDTH/2, st.SCREEN_HEIGHT/2]]
        self.saveDir = [self.direction[2]]
        self.length = 1
        self.score = 0
        self.alive = True
        self.pause = False
    
    def control(self):
        """Bắt các mũi tên nhập từ bàn phím, định hướng di chuyển cho Snake"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != DOWN:
                    self.direction = UP
                    break
                elif event.key == pygame.K_DOWN and self.direction != UP:
                    self.direction = DOWN
                    break
                elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                    self.direction = LEFT
                    break
                elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                    self.direction = RIGHT
                    break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos  
                if pos[0] in range(840, 881) and pos [1] in range(10, 511):
                    pygame.mixer.Channel(0).play(sound.click)
                    self.pause = True
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self, surface):
        """Hiện thị Snake trên surface"""
        flag = True
        for point, dir in zip(self.body, self.saveDir):
            img = pygame.Surface((st.UNIT, st.UNIT))
            if flag:
                img = pygame.image.load("assets/images/head_snake1.png")
                flag = False
            else:
                img = pygame.image.load("assets/images/body_snake.png")
            img = pygame.transform.scale(img, (st.UNIT, st.UNIT))
            img = pygame.transform.rotate(img, dir)
            surface.blit(img, (point[0], point[1]))

    def move(self, wall):
        """Cập nhật vị trí của Snake theo vị trí đầu của Snake, đồng thời kiểm tra Snake đã đâm vào tường hay tự đâm vao thân chưa"""
        old = self.body[0]
        new = [(old[0]+self.direction[0])%st.SCREEN_WIDTH, (old[1]+self.direction[1])%st.SCREEN_HEIGHT]
        if (new in wall) or (self.length > 2 and new in self.body[2:]):
            self.alive = False
            pygame.mixer.Channel(1).play(sound.gameover)
        else:
            self.saveDir.insert(0, self.direction[2])
            self.body.insert(0, new)
            if len(self.body) > self.length:
                self.body.pop()
