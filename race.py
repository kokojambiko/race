import pygame 
import random 
 
WIDTH = 840  # ширина экрана 
HEIGHT = 650  # длина экрана 
FPS = 60 
 
# Задаем цвета 
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0) 
RED = (255, 0, 0) 
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 
  
background=pygame.image.load("D:/python/aad/background.png") 
car_img = pygame.image.load("D:/python/aad/car.png") 
 
car_img=pygame.transform.scale(car_img,(90,140)) 

mon_img = pygame.image.load("D:/python/aad/mon_car.png") 
mon_img=pygame.transform.scale(mon_img,(100,150)) 

# Создаем игру и окно 
pygame.init() 
pygame.mixer.init()  # для звука 
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("My Game")  # заголовок окна 
clock = pygame.time.Clock() 
 
 
bg_y=0 
cr_x=310 
cr_y = 440 
cr_speed=10 
 

mon_list=[]
mon_x= 100
mon_y=300
mon_timer= pygame.USEREVENT + 1
pygame.time.set_timer(mon_timer,1000)

spd = 5.0 
# Цикл игры 
 
 
gameplay = True 
running = True 
while running: 
     
    car_rect=car_img.get_rect(topleft= (cr_x,cr_y)) 
    mon_rect=mon_img.get_rect(topleft= (mon_x,mon_y)) 
 
 
         
 
    screen.blit(background,(0,bg_y)) 
    screen.blit(background,(0,bg_y-650)) 
    screen.blit(car_img,(cr_x,cr_y)) 
 
 

    # if gameplay== False:
    #     if keys[pygame.K_q]:

            # running=False        
    if gameplay: 
        bg_y = bg_y + spd  
        mon_y += 10 
        
        if bg_y == 650: 
            bg_y=0 
        if mon_y == 650: 
            mon_y=-100 

        if mon_list:
            for el in mon_list:
                screen.blit(mon_img,el)
                el.y += 10
 
 
            if car_rect.colliderect(mon_rect): 
                print(1)
                # running=False
            # gameplay= False 
            # if keys[pygame.K_q] :
            #     gameplay=True
            #     running=True
 
        keys= pygame.key.get_pressed() 
        if keys[pygame.K_LEFT] and cr_x >150: 
            cr_x -= cr_speed 
        if keys[pygame.K_RIGHT] and cr_x < 600: 
            cr_x += cr_speed 
        if keys[pygame.K_UP] and cr_y > -100 : 
            cr_y -= cr_speed 
        if keys[pygame.K_DOWN] and cr_y <500: 
            cr_y += cr_speed 
        if keys[pygame.K_q] :
            running=False
        
            
 
        # Держим цикл на правильной скорости 
        clock.tick(FPS) 
        # Ввод процесса (события) 
        for event in pygame.event.get(): 
            # check for closing window 
            if event.type == pygame.QUIT: 
                running = False 
            if event.type == mon_timer:
                mon_list.append(mon_img.get_rect(topleft=(mon_y,mon_x)))

    else: 
        screen.fill((87,88,89)) 

    # Рендеринг 
     
    # Обновление экрана 
    pygame.display.flip() 
 
pygame.quit()