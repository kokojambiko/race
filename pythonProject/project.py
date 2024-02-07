import pygame
import random
import time

WIDTH = 840  # ширина экрана
HEIGHT = 750  # длина экрана
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)







cool_car=pygame.image.load("cool_car.png")
cool_car= pygame.transform.scale(cool_car, (70, 100))
menu_back=pygame.image.load("menu_back.png")
menu_back=pygame.transform.scale(menu_back,(840,750))
background = pygame.image.load("background.png")
background=pygame.transform.scale(background,(840,750))
background1 = pygame.image.load("background.png")
background1=pygame.transform.scale(background1,(840,750))
blue_car=pygame.image.load("blue_car.png")
blue_car = pygame.transform.scale(blue_car, (70, 100))
red_car=pygame.image.load("red_car.png")
red_car = pygame.transform.scale(red_car, (70, 100))
green_car=pygame.image.load("green_car.png")
green_car = pygame.transform.scale(green_car, (70, 100))
main_car=pygame.image.load("car.png")
main_car = pygame.transform.scale(main_car, (70, 100))

cool_car_up=pygame.image.load("cool_car_up.png")
cool_car_up= pygame.transform.scale(cool_car_up, (75, 100))
blue_car_up=pygame.image.load("blue_car_up.png")
blue_car_up = pygame.transform.scale(blue_car_up, (74, 100))
red_car_up=pygame.image.load("red_car_up.png")
red_car_up = pygame.transform.scale(red_car_up, (73, 100))
green_car_up=pygame.image.load("green_car_up.png")
green_car_up = pygame.transform.scale(green_car_up, (72, 100))
main_car=pygame.image.load("car.png")
main_car = pygame.transform.scale(main_car, (71, 100))
mon_car=pygame.image.load("mon_car_up.png")
mon_car = pygame.transform.scale(mon_car, (70, 100))


arrow_right=pygame.image.load("arrow_right.png")
arrow_right = pygame.transform.scale(arrow_right, (110, 120))
arrow_left=pygame.image.load("arrow_left.png")
arrow_left = pygame.transform.scale(arrow_left, (110, 120))
arrow_right_rect = arrow_right.get_rect(topleft=(460, 300))
arrow_left_rect = arrow_left.get_rect(topleft=(270, 300))
x=pygame.image.load("x.png")
x = pygame.transform.scale(x, (50, 50))
ok=pygame.image.load("ok.png")
ok = pygame.transform.scale(ok, (60, 60))
x_rect = x.get_rect(topleft=(20, 20))
ok_rect = ok.get_rect(topleft=(385, 450))

lose_img=pygame.image.load("game_over.png")
lose_img=pygame.transform.scale(lose_img,(200,200))




mon_img =pygame.image.load("mon_car.png")
mon_img = pygame.transform.scale(mon_img, (70, 100))
mon_img2 =pygame.image.load("mon_car.png")
mon_img2 = pygame.transform.scale(mon_img2, (70, 100))
mon_img3 =pygame.image.load("mon_car.png")
mon_img3 = pygame.transform.scale(mon_img3, (70, 100))
cars = [blue_car,mon_img,red_car,green_car,cool_car]
cars2=[main_car, blue_car_up,red_car_up,green_car_up,cool_car_up,mon_car]
# Создаем игру и окно
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")  # заголовок окна
clock = pygame.time.Clock()

label = pygame.font.SysFont('Verdana', 24)
label1 = pygame.font.SysFont('arial', 24)
play_label = pygame.image.load("play_button.png")
play_label = pygame.transform.scale(play_label, (120, 90))

play_label_rect = play_label.get_rect(topleft=(360,250))
restart_label = label1.render('Играть заново!', False, (255, 255, 255))
restart_label_rect = restart_label.get_rect(topleft=(300, 450))
skin_label = pygame.image.load("skin_button.png")
skin_label= pygame.transform.scale(skin_label, (120, 90))
skin_label_rect = skin_label.get_rect(topleft=(360, 400))
ekip_label=label1.render('Экипирован', False, (0, 0, 0))
menu_label=label1.render('Меню', False, (255, 255, 255))
menu_label_rect = menu_label.get_rect(topleft=(350, 550))


game_over= pygame.mixer.Sound("game-overm.mp3")
waiting_menu= pygame.mixer.Sound("waitin_time.mp3")

cnt=0
rec_cnt= 0
skin_cnt=0


cr_rand = [180, 310, 435, 570]
cr_rand2 = [180, 310, 435, 570]
cr_rand3 = [180, 310, 435, 570]




car1=blue_car
car2=random.choice(cars)
car3=random.choice(cars)
car4=random.choice(cars)

cry1=-100
cry2=-50
cry3=-150
cry4=-200
crx1=180
crx2=310
crx3=435
crx4=570

bg_y = 0
cr_x = 310
cr_y = 440
cr_speed = 10



mon_x = random.choice(cr_rand)
mon_y = -100
mon_x2 = random.choice(cr_rand2)
mon_y2 = -200
mon_x3 = random.choice(cr_rand3)
mon_y3 = -100

cool=False
red=False
green=False
blue=False
mon=False
main=True
car_false=[cool,red,green,blue,mon,main]

cr_cnt=0
skin=False
lose=False
menu=True
gameplay =False
running = True
spd =2
spd2= 7
spdcr1=random.randrange(5,20)
spdcr2=random.randrange(5,20)
spdcr3=random.randrange(5,20)
spdcr4=random.randrange(5,20)
car_img=main_car



while running:



    if menu:
        waiting_menu.play()
        screen.blit(background1,(0,0))
        screen.blit(car1,(crx1,cry1))
        screen.blit(car2, (crx2,cry2))
        screen.blit(car3, (crx3, cry3))
        screen.blit(car4, (crx4, cry4))
        screen.blit(play_label,(play_label_rect))
        screen.blit(skin_label,(skin_label_rect))
        clock.tick(FPS)
        cry1 +=spdcr1
        cry2 += spdcr2
        cry3 += spdcr3
        cry4 += spdcr4
        value1 = label.render("Ваш рекорд: " + str(rec_cnt), True, (0, 0, 0))
        screen.blit(value1,(20,20))
        if cry1 >750:
            cry1=-50
            car1 = random.choice(cars)
            spdcr1 = random.randrange(5, 15)
        if cry2 >750:
            cry2=-200
            car2 = random.choice(cars)
            spdcr2 = random.randrange(5, 15)
        if cry3 >750:
            cry3=-100
            car3 = random.choice(cars)
            spdcr3 = random.randrange(5, 15)
        if cry4 >750:
            cry4=-150
            car4 = random.choice(cars)
            spdcr4 = random.randrange(5, 15)
        # Ввод процесса (события)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
            mouse=pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_label_rect.collidepoint(event.pos):
                    gameplay=True
                    cr_y = 440
                    cr_x=random.choice(cr_rand)
                    mon_y=-200
                    cnt =0
                    mon_y2 = -200
                    mon_y3 = -200
                    mon_x=random.choice(cr_rand)
                    menu=False
                    spd =2
                    spd2=7



                    waiting_menu.stop()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if skin_label_rect.collidepoint(event.pos):
                    gameplay=False
                    lose=False
                    skin=True
                    menu=False
        pygame.display.flip()
    if skin:

        lose = False
        screen.blit(background1,(0,0))
        screen.blit(cars2[skin_cnt],(385,300))
        screen.blit(arrow_right,(arrow_right_rect))
        screen.blit(arrow_left,(arrow_left_rect))
        screen.blit(x,(x_rect))
        screen.blit(ok,(ok_rect))
        clock.tick(FPS)
        if car_false[5] == True and skin_cnt == 0:
            car_img = main_car
            screen.blit(ekip_label, (350, 250))
        if car_false[0] == True and skin_cnt == 4:
            car_img = cool_car_up
            screen.blit(ekip_label, (350, 250))
        if car_false[4] == True and skin_cnt == 5:
            car_img = mon_car
            screen.blit(ekip_label, (350, 250))
        if car_false[1] == True and skin_cnt == 2:
            car_img = red_car_up
            screen.blit(ekip_label, (350, 250))
        if car_false[2] == True and skin_cnt == 3:
            car_img = green_car_up
            screen.blit(ekip_label, (350, 250))
        if car_false[3] == True and skin_cnt == 1:
            car_img = blue_car_up
            screen.blit(ekip_label, (350, 250))
        # Ввод процесса (события)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
            mouse=pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if arrow_right_rect.collidepoint(event.pos):
                    if skin_cnt <5:
                        skin_cnt+=1
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if arrow_left_rect.collidepoint(event.pos):
                    if skin_cnt >0:
                        skin_cnt-=1
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if x_rect.collidepoint(event.pos):
                    menu=True
                    skin=False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if ok_rect.collidepoint(event.pos):
                    if skin_cnt==5 and car_false[4] ==False:
                        for i in range(len(car_false)):
                            if car_false[i] == True:
                                car_false[i] = False
                        car_false[4] = True
                    elif skin_cnt == 4 and car_false[0]==False:
                        for i in range(len(car_false)):
                            if car_false[i] == True:
                                car_false[i] = False
                        car_false[0] = True
                    elif skin_cnt==3 and car_false[2]==False:
                        for i in range(len(car_false)):
                            if car_false[i] == True:
                                car_false[i] = False
                        car_false[2] = True
                    elif skin_cnt==2 and car_false[1]==False:
                        for i in range(len(car_false)):
                            if car_false[i] == True:
                                car_false[i] = False
                        car_false[1] = True
                    elif skin_cnt==1 and car_false[3]==False:
                        for i in range(len(car_false)):
                            if car_false[i] == True:
                                car_false[i] = False
                        car_false[3] = True
                    elif skin_cnt==0 and car_false[5]==False:
                        for i in range(len(car_false)):
                            if car_false[i] == True:
                                car_false[i] = False
                        car_false[5] = True
                pygame.display.flip()


        pygame.display.flip()



    if gameplay:
        car_rect = car_img.get_rect(topleft=(cr_x, cr_y))
        mon_rect = mon_img.get_rect(topleft=(mon_x, mon_y))
        mon_rect2 = mon_img2.get_rect(topleft=(mon_x2, mon_y2))
        mon_rect3 = mon_img3.get_rect(topleft=(mon_x3, mon_y3))
        screen.blit(background, (0, bg_y))
        screen.blit(background, (0, bg_y - 750))
        screen.blit(car_img,(cr_x,cr_y))
        screen.blit(mon_img, (mon_x, mon_y))
        bg_y += spd
        mon_y += spd2
        if cnt > rec_cnt:
            rec_cnt= cnt
        if cnt > 0:
            mon_y2 += spd2
            screen.blit(mon_img2 ,(mon_x2, mon_y2))
        if cnt > 5:
            screen.blit(mon_img3 ,(mon_x3, mon_y3))
            mon_y3 += spd2
        if bg_y >= 750:
            if spd < 40:
                if spd <20:
                    spd2 += 0.8
                    spd += 0.5
                elif spd >20 :
                    spd +=0.2
                    spd2 += 0.5
                elif spd< 10:
                    spd +=1
                    spd2+=2
            bg_y = 0
        if mon_y >= 750:
            mon_x=  random.choice(cr_rand)
            mon_y = -100
            mon_img=random.choice(cars)
            cnt +=1

        if mon_y2 >= 750:
            mon_x2=  random.choice(cr_rand2)
            mon_y2 = -200
            mon_img2=random.choice(cars)

        if mon_y3 >= 750:
            mon_x3=  random.choice(cr_rand)
            mon_y3 = -150
            mon_img3=random.choice(cars)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and cr_x > 130:
            cr_x -= cr_speed
        if keys[pygame.K_RIGHT] and cr_x < 630:
            cr_x += cr_speed
        if keys[pygame.K_UP] and cr_y > 0:
            cr_y -= cr_speed
        if keys[pygame.K_DOWN] and cr_y< 650:
            cr_y += cr_speed

            # Держим цикл на правильной скорости
        clock.tick(FPS)
        # Ввод процесса (события)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False


        value = label.render("Ваш счёт: " + str(cnt), True, (0, 0, 0))
        screen.blit(value,(20,20))
        value1 = label.render("Ваш рекорд: " + str(rec_cnt), True, (0, 0, 0))
        screen.blit(value1,(20,70))
        if car_rect.colliderect(mon_rect) or car_rect.colliderect(mon_rect2) or car_rect.colliderect(mon_rect3):
            game_over.play()

            cr_y = 440
            mon_y= -100
            mon_y2= -100
            mon_y3 = -100
            gameplay=False

            time.sleep(1)
            lose=True
        pygame.display.flip()


    if lose:

        # screen.fill((87, 88, 89))
        # screen.blit(lose_img, (280, 150))
        # screen.blit(restart_label, (restart_label_rect))
        # screen.blit(menu_label,(menu_label_rect))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if restart_label_rect.collidepoint(event.pos):
                    lose=False
                    cr_y = 440
                    cr_x = random.choice(cr_rand)
                    mon_y = -100
                    mon_y2 = -100
                    mon_y3 = -100
                    mon_x = random.choice(cr_rand)

                    gameplay=True
                    spd =2
                    spd2=7
                    cnt=0
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if menu_label_rect.collidepoint(event.pos):
                    skin= False
                    lose=False
                    gameplay=False
                    menu=True

        screen.fill((87, 88, 89))
        screen.blit(lose_img, (280, 150))
        screen.blit(restart_label, (restart_label_rect))
        screen.blit(menu_label,(menu_label_rect))


        pygame.display.flip()

    # Обновление экрана
    pygame.display.flip()

pygame.quit()