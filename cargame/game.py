import pygame
import time
import random
pygame.init()
gray=(119,118,110)
black=(0,0,0)
red=(255,0,0)
green=(0,200,0)
blue=(0,0,200)
bright_red=(255,0,0)
bright_green=(0,255,0)
bright_blue=(0,0,255)


display_width=770
display_height=600
gamedisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Car Game")
clock=pygame.time.Clock()
carimg=pygame.image.load('car1.jpg')
background=pygame.image.load('grass1.jpg')
yellow=pygame.image.load('road.jpg')
white=pygame.image.load('white1.jpg')
car_width=68
intro_back=pygame.image.load('intro2.jpg')
instruct=pygame.image.load('instruction.jpg')


def intro_loop():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplay.blit(intro_back,(0,0))
        largetext = pygame.font.Font("freesansbold.ttf", 115)
        Textsurf, Textrect = text_objects("CAR GAME", largetext)
        Textrect.center = (400,100)
        gamedisplay.blit(Textsurf, Textrect)
        button("START",150,520,100,50,green,bright_green,"play")
        button("QUIT",550,520,100,50,red,bright_red,"quit")
        button("INSTRUCTIONS",300,520,200,50,blue,bright_blue,"intro")
        pygame.display.update()
        clock.tick(50)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gamedisplay,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action=="play":
                countdown()
            elif action=="quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action=="intro":
                introduction()
            elif action=="menu":
                intro_loop()
    else:
        pygame.draw.rect(gamedisplay,ic,(x,y,w,h))
        smalltext = pygame.font.Font("freesansbold.ttf", 20)
        textsurf, textrect = text_objects(msg,smalltext)
        textrect.center = ((x+w/2),(y+h/2))
        gamedisplay.blit(textsurf, textrect)


def introduction():
    introduction=True
    while introduction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplay.blit(instruct,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',80)
        smalltext=pygame.font.Font('freesansbold.ttf',20)
        mediumtext=pygame.font.Font('freesansbold.ttf',40)
        textSurf,textRect=text_objects("This is an car game in which you need dodge the coming cars",smalltext)
        textRect.center=((350),(200))
        TextSurf,TextRect=text_objects("INSTRUCTION",largetext)
        TextRect.center=((400),(100))
        gamedisplay.blit(TextSurf,TextRect)
        gamedisplay.blit(textSurf,textRect)
        stextSurf,stextRect=text_objects("ARROW LEFT : LEFT TURN",smalltext)
        stextRect.center=((150),(400))
        hTextSurf,hTextRect=text_objects("ARROW RIGHT : RIGHT TURN" ,smalltext)
        hTextRect.center=((150),(450))
        atextSurf,atextRect=text_objects("A : ACCELERATOR",smalltext)
        atextRect.center=((150),(500))
        rtextSurf,rtextRect=text_objects("B : BRAKE ",smalltext)
        rtextRect.center=((150),(550))
        sTextSurf,sTextRect=text_objects("CONTROLS",mediumtext)
        sTextRect.center=((350),(300))
        gamedisplay.blit(sTextSurf,sTextRect)
        gamedisplay.blit(stextSurf,stextRect)
        gamedisplay.blit(hTextSurf,hTextRect)
        gamedisplay.blit(atextSurf,atextRect)
        gamedisplay.blit(rtextSurf,rtextRect)
        button("BACK",600,450,100,50,blue,bright_blue,"menu")
        pygame.display.update()
        clock.tick(30)

def countdown_background():
    font=pygame.font.SysFont(None,25)
    x=(display_width*0.45)
    y=(display_height*0.8)
    gamedisplay.blit(background,(0,0))
    gamedisplay.blit(background,(0,200))
    gamedisplay.blit(background,(0,400))
    gamedisplay.blit(background,(700,0))
    gamedisplay.blit(background,(700,200))
    gamedisplay.blit(background,(700,400))
    gamedisplay.blit(yellow,(400,100))
    gamedisplay.blit(yellow,(400,200))
    gamedisplay.blit(yellow,(400,300))
    gamedisplay.blit(yellow,(400,400))
    gamedisplay.blit(yellow,(400,100))
    gamedisplay.blit(yellow,(400,500))
    gamedisplay.blit(yellow,(400,0))
    gamedisplay.blit(yellow,(400,600))
    gamedisplay.blit(white,(120,200))
    gamedisplay.blit(white,(120,0))
    gamedisplay.blit(white,(120,100))
    gamedisplay.blit(white,(680,100))
    gamedisplay.blit(white,(680,0))
    gamedisplay.blit(white,(680,200))
    gamedisplay.blit(carimg,(x,y))
    text=font.render("DODGED: 0",True, black)
    score=font.render("SCORE: 0",True,red)
    gamedisplay.blit(text,(0,50))
    gamedisplay.blit(score,(0,30))




def countdown():
    countdown=True

    while countdown:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gamedisplay.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("3",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplay.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplay.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("2",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplay.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplay.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("1",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplay.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplay.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("GO!!!",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplay.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            game_loop()






def obstacle(obs_startx,obs_starty,obs):
    if obs==0:
        obs_pic=pygame.image.load("car2.jpg")
    elif obs==1:
        obs_pic = pygame.image.load("car3.jpg")
    elif obs==2:
        obs_pic = pygame.image.load("car4.jpg")
    elif obs==3:
        obs_pic = pygame.image.load("car5.jpg")
    elif obs==4:
        obs_pic = pygame.image.load("car6.jpg")
    gamedisplay.blit(obs_pic,(obs_startx,obs_starty))


def score_system(passed,score):
    font=pygame.font.SysFont(None,25)
    text=font.render("Passed"+str(passed),True,black)
    score = font.render("Score" + str(score), True, red)
    gamedisplay.blit(text,(0,50))
    gamedisplay.blit(score,(0,30))


def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()

def message_display(text):
    largetext=pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((display_width/2),(display_height/2))
    gamedisplay.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

def crash():
    message_display("YOU CRASHED!")



def back():
    gamedisplay.blit(background,(0,0))
    gamedisplay.blit(background,(0,200))
    gamedisplay.blit(background,(0,400))
    gamedisplay.blit(background,(700,0))
    gamedisplay.blit(background, (700, 200))
    gamedisplay.blit(background, (700, 400))
    gamedisplay.blit(yellow,(400,0))
    gamedisplay.blit(yellow, (400, 100))
    gamedisplay.blit(yellow, (400, 200))
    gamedisplay.blit(yellow, (400, 300))
    gamedisplay.blit(yellow, (400, 400))
    gamedisplay.blit(yellow, (400, 500))
    gamedisplay.blit(white, (120,0))
    gamedisplay.blit(white, (120, 100))
    gamedisplay.blit(white, (120, 200))
    gamedisplay.blit(white, (120, 300))
    gamedisplay.blit(white, (650, 0))
    gamedisplay.blit(white, (650, 100))
    gamedisplay.blit(white, (650, 200))
    gamedisplay.blit(white, (650, 300))





def car(x,y):
    gamedisplay.blit(carimg,(x,y))

def game_loop():
    x=display_width*0.42
    y=display_height*0.72
    x_change=0
    obstacle_speed=9
    obs=0
    y_change=0
    obs_startx=random.randrange(200,(display_width-200))
    obs_starty=-750
    obs_width=70
    obs_height=168
    passed=0
    level=0
    score=0
    y2 = 7
    fps = 120

    bumped=False
    while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x_change=-5
            if event.key==pygame.K_RIGHT:
                x_change=5
            if event.key==pygame.K_a:
                obstacle_speed+=2
            if event.key==pygame.K_b:
                obstacle_speed-=2
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                x_change=0
        x+=x_change
        gamedisplay.fill(gray)


        rel_y = y2 % background.get_rect().width
        gamedisplay.blit(background, (0, rel_y - background.get_rect().width))
        gamedisplay.blit(background, (700, rel_y - background.get_rect().width))
        if rel_y < 800:
            gamedisplay.blit(background, (0, rel_y))
            gamedisplay.blit(background, (700, rel_y))
            gamedisplay.blit(yellow, (400, rel_y))
            gamedisplay.blit(yellow, (400, rel_y + 100))
            gamedisplay.blit(yellow, (400, rel_y + 200))
            gamedisplay.blit(yellow, (400, rel_y + 300))
            gamedisplay.blit(yellow, (400, rel_y + 400))
            gamedisplay.blit(yellow, (400, rel_y + 500))
            gamedisplay.blit(yellow, (400, rel_y - 100))
            gamedisplay.blit(white, (120, rel_y - 200))
            gamedisplay.blit(white, (120, rel_y + 20))
            gamedisplay.blit(white, (120, rel_y + 30))
            gamedisplay.blit(white, (680, rel_y - 100))
            gamedisplay.blit(white, (680, rel_y + 20))
            gamedisplay.blit(white, (680, rel_y + 30))

        y2 += obstacle_speed

        obs_starty-=(obstacle_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+=obstacle_speed
        car(x,y)
        score_system(passed,score)
        if x>650-car_width or x<110:
            crash()
        if x>display_width-(car_width+110) or x<110:
            crash()
        if obs_starty>display_height:
            obs_starty=0-obs_height
            obs_startx=random.randrange(170,(display_width-170))
            obs=random.randrange(0,5)
            passed=passed+1
            score=score+10
            if int(passed)%10==0:
                level=level+1
                obstacle_speed+2
                largetext = pygame.font.Font("freesansbold.ttf", 80)
                textsurf, textrect = text_objects("LEVEL"+str(level), largetext)
                textrect.center = ((display_width / 2), (display_height / 2))
                gamedisplay.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(3)

        if y<obs_starty+obs_height:
            if x>obs_startx and x<obs_startx+obs_width or x+car_width>obs_startx and x+car_width<obs_startx+obs_width:
                crash()
        pygame.display.update()
        clock.tick(60)
intro_loop()
game_loop()
pygame.quit()
quit()
