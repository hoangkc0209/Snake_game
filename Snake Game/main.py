"""Module chứa hàm main của game, hãy run file này để khởi động trò chơi"""
import pygame, sys, random, fruit, snake, wall, sound
from pygame.locals import *
import setting as st
       
def play(SCREEN, map):
    SCREEN.fill((255, 255, 255))
    pygame.mixer.Channel(1).play(random.choice([sound.background1, sound.background2]), -1)
    #Khoi tao doi tuong
    s = snake.Snake(map)
    w = wall.Wall(map)
    f = fruit.Fruit(w.position, s.body)
    
    #Khoi tao hinh anh
    background_game = pygame.transform.scale(pygame.image.load("assets/images/background_game.jpg").convert_alpha(), (st.SCREEN_WIDTH, st.SCREEN_HEIGHT))
    background_over = pygame.transform.scale( pygame.image.load("assets/images/gameover.jpg").convert_alpha(), (200, 200))
    replay = pygame.transform.scale(pygame.image.load("assets/images/replay.png").convert_alpha(), (40, 40))
    back1 = pygame.transform.scale(pygame.image.load("assets/images/quit.png").convert_alpha(), (40, 40))
    back2 = pygame.transform.scale(pygame.image.load("assets/images/quit.png").convert_alpha(), (150, 150))
    pause = pygame.transform.scale(pygame.image.load("assets/images/pause.png").convert_alpha(), (40, 40))
    unpause =  pygame.transform.scale(pygame.image.load("assets/images/unpause.png").convert_alpha(), (150, 150))
    
    #Vong lap game khi start
    while True:
        #Vong lap khi Snake con song
        while s.alive:
            SCREEN.blit(background_game, (0, 0))
            s.control()
            s.move(w.position)
            if s.body[0][:2] == f.position:
                pygame.mixer.Channel(0).play(sound.eat)
                f = fruit.Fruit(w.position, s.body)
                s.score += 1
                s.length += 1
            #Tam dung
            while s.pause:
                pygame.mixer.Channel(1).pause()
                w.draw(SCREEN)
                s.draw(SCREEN)
                f.draw(SCREEN)
                SCREEN.blit(unpause, (st.SCREEN_WIDTH/2-200, st.SCREEN_HEIGHT/2-100))
                SCREEN.blit(back2, (st.SCREEN_WIDTH/2+50, st.SCREEN_HEIGHT/2-100))
                SCREEN.blit(pygame.font.SysFont("times new roman", 20).render(f"Điểm: {s.score}", True, (255, 255, 0)), (10, 20))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pos = event.pos  
                        if pos[0] in range(250, 401) and pos [1] in range(200, 401):
                            pygame.mixer.Channel(0).play(sound.click)
                            pygame.mixer.Channel(1).unpause()
                            s.pause = False
                        if pos[0] in range(500, 651) and pos [1] in range(200, 401):
                            pygame.mixer.Channel(0).play(sound.click)
                            pygame.mixer.Channel(1).unpause()
                            main()
            w.draw(SCREEN)
            s.draw(SCREEN)
            f.draw(SCREEN)
            SCREEN.blit(pygame.font.SysFont("times new roman", 20).render(f"Điểm: {s.score}", True, (255, 255, 0)), (10, 20))
            SCREEN.blit(pause ,(840, 10))
            pygame.display.update()
            pygame.time.Clock().tick(st.FPS)
        
        #Gameover: hien modal thong bao
        SCREEN.blit(background_over, (st.SCREEN_WIDTH/2-100, st.SCREEN_HEIGHT/2-100))
        SCREEN.blit(pygame.font.SysFont("times new roman", 17).render(f"Thành tích: {s.score} điểm", True, (0, 0, 0)), (380, 320))
        SCREEN.blit(replay, (380, 350))
        SCREEN.blit(back1, (470, 350))
        for event in pygame.event.get():
            #Thoat game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                #Choi lai map nay
                if pos[0] in range(380, 421) and pos [1] in range(350, 391):      
                    pygame.mixer.Channel(0).play(sound.click)
                    play(SCREEN, map)
                #Thoat ra man hinh chon map
                if pos[0] in range(470, 511) and pos [1] in range(350, 391):
                    pygame.mixer.Channel(0).play(sound.click)
                    main()
        pygame.display.update()

def main():
    #Khoi tao cua so game
    pygame.init()
    SCREEN = pygame.display.set_mode((st.SCREEN_WIDTH, st.SCREEN_HEIGHT))
    pygame.display.set_caption("SNAKE GAME")
    FONT = pygame.font.SysFont("times new roman", 20)

    #Hinh nen menu
    BACKGROUND = pygame.image.load("assets/images/background_menu.jpg").convert_alpha()
    BACKGROUND = pygame.transform.scale(BACKGROUND, (st.SCREEN_WIDTH, st.SCREEN_HEIGHT))
    SCREEN.blit(BACKGROUND, (0, 0))

    #Button play game
    BUTTON = pygame.image.load("assets/images/button_play.png").convert_alpha()
    BUTTON = pygame.transform.scale(BUTTON, (100, 50))
    possition_button = pygame.Rect(st.SCREEN_WIDTH/2-50, st.SCREEN_HEIGHT/2-25, 100, 50)
    SCREEN.blit(BUTTON, possition_button)

    #Hinh map
    map0 = pygame.transform.scale(pygame.image.load("assets/images/map0.png"), (120, 80))
    map1 = pygame.transform.scale(pygame.image.load("assets/images/map1.png"), (120, 80))
    map2 = pygame.transform.scale(pygame.image.load("assets/images/map2.png"), (120, 80))
    map3 = pygame.transform.scale(pygame.image.load("assets/images/map3.png"), (120, 80))
    map4 = pygame.transform.scale(pygame.image.load("assets/images/map4.png"), (120, 80))
    map5 = pygame.transform.scale(pygame.image.load("assets/images/map5.png"), (120, 80))

    #Nhac nen 
    pygame.mixer.Channel(1).play(sound.background3)
    pygame.mixer.Channel(0).set_volume(0.2)
    pygame.mixer.Channel(1).set_volume(0.2)

    start = False
    #Vong lap game
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            #Thoat game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                #Event: An vao nut start
                if pos[0] in range(possition_button.left, possition_button.right+1) and pos[1] in range(possition_button.top, possition_button.bottom+1):
                    pygame.mixer.Channel(0).play(sound.click)
                    SCREEN.blit(FONT.render(f"Chọn map:", True, (255, 0, 0)), (400, 330))
                    SCREEN.blit(map0, (250, 360))
                    SCREEN.blit(map1, (390, 360))
                    SCREEN.blit(map2, (530, 360))
                    SCREEN.blit(map3, (250, 450))
                    SCREEN.blit(map4, (390, 450))
                    SCREEN.blit(map5, (530, 450))
                    start = True
                #Event: An vao hinh map de chon map va choi game
                if start:
                    if pos[0] in range(250, 371) and pos[1] in range(360, 441):
                        pygame.mixer.Channel(0).play(sound.click)
                        play(SCREEN, 0)
                    if pos[0] in range(390, 511) and pos[1] in range(360, 441):
                        pygame.mixer.Channel(0).play(sound.click)
                        play(SCREEN, 1)                
                    if pos[0] in range(530, 651) and pos[1] in range(360, 441):
                        pygame.mixer.Channel(0).play(sound.click)
                        play(SCREEN, 2)
                    if pos[0] in range(250, 371) and pos[1] in range(450, 531):
                        pygame.mixer.Channel(0).play(sound.click)
                        play(SCREEN, 3)
                    if pos[0] in range(390, 511) and pos[1] in range(450, 531):
                        pygame.mixer.Channel(0).play(sound.click)
                        play(SCREEN, 4)                
                    if pos[0] in range(530, 651) and pos[1] in range(450, 531):
                        pygame.mixer.Channel(0).play(sound.click)
                        play(SCREEN, 5)               

main()