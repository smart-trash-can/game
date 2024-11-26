import pygame
import random
import time as t

win = pygame.display.set_mode((600,700))
pygame.display.set_caption('game')

pygame.font.init()
font=pygame.font.SysFont('Arial',50)
font2=pygame.font.SysFont('Arial',20)
img1 = pygame.image.load('1.png')
img2 = pygame.image.load('2.png')

clock=pygame.time.Clock()

def game():
    position_list=[]
    time=0
    time_game=0
    line=2
    sped=4
    run = True
    while run:
        time+=1/40
        time_game+=1/40
        win.fill((30,30,30))
        for i in range(len(position_list)):
            try:
                win.blit(img2,(position_list[i][0]-45,position_list[i][1]))
                if position_list[i][1] >= 700:
                    del position_list[i]
                else:
                    position_list[i][1]+=sped
            except:
                win.blit(img2,(position_list[i-1][0]-45,position_list[i-1][1]))
        for i in range(len(position_list)):
            if 680>position_list[i][1]>440:
                if line == position_list[i][2]:
                    text=font.render('GAME OVER',False,(255,0,0))
                    text2=font.render(str(int(time_game)),False,(255,255,0))
                    print(str(int(time_game)))
                    win.blit(text,(200,250))
                    win.blit(text2,(200,300))
                    pygame.display.update()
                    t.sleep(2)
                    run=False
        win.blit(img1,(line*200-130,550))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not line == 1:
                        line-=1 
                if event.key == pygame.K_RIGHT:
                    if not line == 3:
                        line+=1
        if int(time) >= 2:
            time=0
            r=random.randint(1,3)
            position_list.append([r*200-150,-200,r])
            sped+=0.2
        clock.tick(40)
        pygame.display.update()
game()
