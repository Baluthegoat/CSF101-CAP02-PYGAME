# importing all modules from pygame 
import pygame,sys
from pygame.locals import *
import random
import math
import time

# initialzing the pygame 
pygame.init()
screen = pygame.display.set_mode((840,600))
# initialzing the pygame mixer
pygame.mixer.init()
pygame.display.set_caption('Button Interaction')
button1 = pygame.Rect(60,440,175,50)
button2 = pygame.Rect(265,440,300,50)
click = False
clock = pygame.time.Clock()

# changing the title of the game
pygame.display.set_caption('Racing Monster')
# changing the logo
logo = pygame.image.load('/home/balutheg.o.a.t/Desktop/CAP2_Pygame/Background/Logo.jpg')
pygame.display.set_icon(logo)

# creating a main menu

IntroFont = pygame.font.Font("freesansbold.ttf", 38)
def introImg(x,y):
    intro = pygame.image.load("/home/balutheg.o.a.t/Desktop/CAP2_Pygame/Background/m.png")

    screen.blit(intro,(x,y))

def instructionIMG(x,y):
    instruct = pygame.image.load("/home/balutheg.o.a.t/Desktop/CAP2_Pygame/Background/i.jpg")
    run = True
    while run:
        screen.blit(instruct,(x,y))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
def play(x,y):
    playtext = IntroFont.render("PLAY", True,(255,0,0))
    screen.blit(playtext,(x,y))
def instruction(x,y):
    instructionText = IntroFont.render("INSTRUCTION", True,(255,0,0))
    screen.blit(instructionText,(x,y))

def introscreen():
    global click
    run = True
    pygame.mixer.music.load('/home/balutheg.o.a.t/Desktop/CAP2_Pygame/Gamesound/intro.mp3')
    pygame.mixer.music.play()
    while run:
        screen.fill((0,0,0))
        introImg(0,0)
        play(100,450)
        instruction(280,450)
        
        # # creating mouse cursor
        x,y = pygame.mouse.get_pos()

        button1 = pygame.Rect(60,440,175,50)
        button2 = pygame.Rect(265,440,300,50)

        if button1.collidepoint(x,y):
            pygame.draw.rect(screen,(155,0,0), button1,6)
            if click:
                    countdown()

        if button2.collidepoint(x,y):
            pygame.draw.rect(screen,(155,0,0), button2,6)
            if click:
                instructionIMG(0,0)

        click = False    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()   

# setting count down 
def countdown():
    font2 = pygame.font.Font('freesansbold.ttf', 85)
    countdownBackground = pygame.image.load('/home/balutheg.o.a.t/Desktop/CAP2_Pygame/Background/track1.jpg')
    three = font2.render('3', True,(187,30,16))
    two = font2.render('2', True,(255,255,0))
    one = font2.render('1', True,(51,165,50))
    go = font2.render('GO!!!', True,(0,255,0))


    # displaying blank background ##
    screen.blit(countdownBackground, (0,0))
    pygame.display.update()

    # displaying three 
    screen.blit(three, (350,250))
    pygame.display.update()
    time.sleep(1)

    # displaying blank background 
    screen.blit(countdownBackground, (0,0))
    pygame.display.update()
    time.sleep(1)

    # displaying two
    screen.blit(two, (350,250))
    pygame.display.update()
    time.sleep(1)

     # displaying blank background 
    screen.blit(countdownBackground, (0,0))
    pygame.display.update()
    time.sleep(1)

     # displaying one
    screen.blit(one, (350,250))
    pygame.display.update()
    time.sleep(1)

    # displaying blank background 
    screen.blit(countdownBackground, (0,0))
    pygame.display.update()
    time.sleep(1)

    # displaying GO!!
    screen.blit(go, (350,250))
    pygame.display.update()
    time.sleep(1)
    print('before game loop')
    # gameloop()
    print('Called2 after game loop')
    pygame.display.update()

# defining our gameloop function 
def gameloop():
    print('Inside game loop')
    ### game background music##
    pygame.mixer.music.load('/home/balutheg.o.a.t/Desktop/CAP2_Pygame/Gamesound/toyota.mp3')
    pygame.mixer.music.play()
    ### sound effect for collision ###
    crash_sound = pygame.mixer.Sound('/home/balutheg.o.a.t/Desktop/CAP2_Pygame/Gamesound/carcrashing.mp3')
    
    # scoring part 
    score_value = 0
    font1 = pygame.font.Font("freesansbold.ttf",25)
    def show_score(x,y):
        score = font1.render("SCORE:"+str(score_value), True, (255,255,255))
        screen.blit(score,(x,y))
    
    
    # creating the gameover function 
    def gameover():
        gameoverimg = pygame.image.load('/home/balutheg.o.a.t/Desktop/CAP2_Pygame/Background/OVER1.jpg')
        run = True
        while run:
            screen.blit(gameoverimg,(0,0))
            
            time.sleep(0.5)
            show_score(330,400)
            time.sleep(0.5)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        countdown()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        # sys.exit()


    # setting background image
    bg = pygame.image.load('/home/balutheg.o.a.t/Desktop/CAP2_Pygame/Background/track1.jpg')
    
    # setting the game loop
    maincar = pygame.image.load('/home/balutheg.o.a.t/Desktop/CAP2_Pygame/Topdown_vehicle_sprites_pack/Car1.png')
    maincarX = 20
    maincarY = 30
    maincarX_change = 0
    maincarY_change = 0
    

    # importing the enemy car
    car1 = pygame.image.load('/home/balutheg.o.a.t/Desktop/CAP2_Pygame/Topdown_vehicle_sprites_pack/car1.png')
    car1X = random.randint(178,490)
    car1Y = -800
    car1Ychange = 10

    car2 = pygame.image.load('/home/balutheg.o.a.t/Desktop/CAP2_Pygame/Topdown_vehicle_sprites_pack/car2.png')
    car2X = random.randint(178,490)
    car2Y = -300
    car2Ychange = 10

    car3 = pygame.image.load('/home/balutheg.o.a.t/Desktop/CAP2_Pygame/Topdown_vehicle_sprites_pack/car3.png')
    car3X = random.randint(178,490)
    car3Y = -500
    car3Ychange = 10
    pygame.display.update()  

   
    # print('before running')
    run = True
    print('before')
    # reset_counter = 0
    while run:
        fps = str(int(clock.get_fps()))
        # print("FPS:", fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            
            # setting the key 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # if maincarX < 600:
                    maincarX_change += 10

                if event.key == pygame.K_LEFT:
                    maincarX_change -= 10

                if event.key == pygame.K_UP:
                    maincarY_change -= 10

                if event.key == pygame.K_DOWN:
                    maincarY_change += 10

            # checking if the key has been lifted up
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    maincarX_change = 0

                if event.key == pygame.K_LEFT:
                    maincarX_change = 0

                if event.key == pygame.K_UP:
                    maincarY_change = 0

                if event.key == pygame.K_DOWN:
                    maincarY_change = 0

        # changing color with RBG value
        screen.fill((0,0,0))
        
        #displaying the background image
        screen.blit(bg,(0,0))
        # displaying our main car
        screen.blit(maincar,(maincarX,maincarY))

        # displaying enemy car
        screen.blit(car1,(car1X,car1Y))
        screen.blit(car2,(car2X,car2Y))
        screen.blit(car3,(car3X,car3Y))

        # show the score
        show_score(570, 280)
        
        # updating the values 
        maincarX += maincarX_change
        maincarY += maincarY_change

         # setting boundary for the mamin car
        # print('Reset', reset_counter)
        # reset_counter += 1
        if maincarX <= 100:
            maincarX = 100
        elif maincarX >= 500:
            maincarX = 500

        if maincarY <= 100:
            maincarY = 100
        elif maincarY > 500:
            maincarY = 500
        

        # updating the values 
        car1Y += car1Ychange 
        car2Y += car2Ychange
        car3Y += car3Ychange
        

        # mmoving enemies 
       

            # Detecting the collision between the cars
        def iscollision(carX,carY,maincarX,maincarY):
            distance = math.sqrt(math.pow(carX-maincarX,2) + math.pow(carY - maincarY,2))

            # calculating theh sum of the radius(100 pixels)
            # raduis_sum = 100 + 100
            # checking if distance is smaller then 50 after then collision will occur
            if distance < 100:
                return True
            else:
                return False
        pygame.display.update()

        # print('here')
        if car1Y > 600:
            car1Y = -50
            car1X = random.randint(178,490)
            score_value += 1
        if car2Y > 670:
            car2Y = -150
            car2X = random.randint(178,490)
            score_value += 1
        if car3Y > 700:
            car3Y = -300
            car3X = random.randint(178,490)
            score_value += 1 
                    # giving collision a variable

                    # collision between maincar and cars
        coll1 = iscollision(car1X,car1Y,maincarX,maincarY)
        coll2 = iscollision(car1X,car1Y,maincarX,maincarY)
        coll3 = iscollision(car2X,car2Y,maincarX,maincarY)


                # if collision 1 occur
        if coll1 or coll2 or coll3:
            screen.fill((200,215,250))
            car1Ychange = 0
            car2Ychange = 0
            car3Ychange = 0
            maincarX_change = 0
            maincarY_change = 0
            pygame.mixer.music.stop()
            crash_sound.play()
                    
                    # gameover function 
            time.sleep(1)
            # gameover()
            pygame.display.update()

        if car1Ychange == 0 and car2Ychange == 0 and car3Ychange == 0:
            pass
       
    pygame.display.update()
    clock.tick(60)
    introscreen()        
