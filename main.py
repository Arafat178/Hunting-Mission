import pygame
from pygame import mixer
import asyncio
async def main():
    pygame.init()

    screen = pygame.display.set_mode((750,670))
    backgp=pygame.image.load('assets/images/background.png')
    coverbg = pygame.image.load('assets/images/coverbgf.png')
    mission_complete_img = pygame.image.load('assets/images/MissionComplete.png')

    mixer.music.load('assets/sounds/warb.ogg')
    mixer.music.play(-1)

    #valueChange
    clock = pygame.time.Clock()
    jet_change = 3
    v_change = 2
    bomb_change = 4
    mi_change = 6
    jDrop_change = 2
    jet1 = pygame.image.load('assets/images/jet1.png')
    jet2 = pygame.image.load('assets/images/jet2.png')

    jetX=20
    jetY=40

    def jet1XY(x,y):
        screen.blit(jet1,(x,y))
    def jet2XY(x,y):
        screen.blit(jet2,(x,y))

    #jetVariable
    jet1vis = False
    jet2vis = True
    X_value= jet_change #change
    Y_value= jet_change #change

    #bomb
    bomb=pygame.image.load('assets/images/horizontal_bomb.png')
    bombX=jetX+40
    bombY=jetY

    def bombXY(x,y):
        screen.blit(bomb,(x,y))

    #bombVariable
    bombDrop=0

    #explsn
    exp1=pygame.image.load('assets/images/explo-1.png')
    exp2=pygame.image.load('assets/images/explo-2.png')
    exp3=pygame.image.load('assets/images/explo-3.png')
    exp4=pygame.image.load('assets/images/explo-4.png')
    exp5=pygame.image.load('assets/images/explo-5.png')
    exp6=pygame.image.load('assets/images/explo-6.png')
    exp7=pygame.image.load('assets/images/explo-7.png')

    exploX=bombX-150
    exploY=200

    def exp1XY(x,y):
        screen.blit(exp1,(x,y))
    def exp2XY(x,y):
        screen.blit(exp2,(x,y))
    def exp3XY(x,y):
        screen.blit(exp3,(x,y))
    def exp4XY(x,y):
        screen.blit(exp4,(x,y))
    def exp5XY(x,y):
        screen.blit(exp5,(x,y))
    def exp6XY(x,y):
        screen.blit(exp6,(x,y))
    def exp7XY(x,y):
        screen.blit(exp7,(x,y))

    #exploVariable
    exploVi = False
    exploC = 0

    #vhe
    mcar=pygame.image.load('assets/images/Dibba.png')
    mcarX=-100
    mcarY=505
    def mcarXY(x,y):
        screen.blit(mcar,(x,y))

    #trk
    trk=pygame.image.load('assets/images/DiplomaMilk.png')
    trkX=-1200
    trkY=495
    def trkXY(x,y):
        screen.blit(trk,(x,y))

    mtrk=pygame.image.load('assets/images/illigalf.png')
    mtrkX=-600
    mtrkY=415
    def mtrkXY(x,y):
        screen.blit(mtrk,(x,y))

    missi=pygame.image.load('assets/images/missile.png')
    missiX=mtrkX
    missiY=mtrkY
    def missiXY(x,y):
        screen.blit(missi,(x,y))

    #missiVari
    missi_lnc = 0
    missi_So = 0

    #jetFire and destroy
    jetfire=pygame.image.load('assets/images/jetfire.png')
    fireX=jetX+10
    fireY= jetY-40
    def fireXY(x,y):
        screen.blit(jetfire,(x,y))

    #fireVariable
    fireVi = 0

    #score
    sfont=pygame.font.SysFont('freesansbold.tff',40)
    scoreX=10
    scoreY=10
    score_value=0
    def scoreXY(x,y):
        score=sfont.render('SCORE:'+str(score_value),True,(0,0,0))
        screen.blit(score,(x,y))

    #game over
    gfont = pygame.font.SysFont('freesansbold.tff',80)
    def gameOverXY(x,y):
        gameOver=gfont.render('MISSION FAILED',True,(0,0,0))
        screen.blit(gameOver,(x,y))

    # ---------------- UI Buttons ----------------
    button_up = pygame.Rect(575, 555, 80, 50)
    button_down = pygame.Rect(575, 610, 80, 50)
    button_left = pygame.Rect(490, 585, 80, 50)
    button_right = pygame.Rect(660, 585, 80, 50)
    button_fire = pygame.Rect(20, 560, 80, 80)
    button_start = pygame.Rect(280, 600, 150, 40)
    button_background = pygame.Rect(0,550,750,120)
    font_btn = pygame.font.SysFont('freesansbold.ttf', 25)
    font_start = pygame.font.SysFont('freesansbold.ttf', 32)
    font_continue = pygame.font.SysFont('freesansbold.ttf', 32)
    button_continue = pygame.Rect(280, 600, 150, 40)

    def draw_buttons():
        pygame.draw.rect(screen, (205, 205, 205), button_background)
        pygame.draw.rect(screen, (200, 200, 20), button_up)
        pygame.draw.rect(screen, (200, 200, 20), button_down)
        pygame.draw.rect(screen, (200, 200, 20), button_left)
        pygame.draw.rect(screen, (200, 200, 20), button_right)
        pygame.draw.rect(screen, (255, 0, 0), button_fire)
        screen.blit(font_btn.render('UP', True, (0, 0, 0)), (590, 565))
        screen.blit(font_btn.render('DOWN', True, (0, 0, 0)), (585, 625))
        screen.blit(font_btn.render('Left', True, (0, 0, 0)), (500, 600))
        screen.blit(font_btn.render('Right', True, (0, 0, 0)), (670, 595))
        screen.blit(font_btn.render('FIRE', True, (255, 255, 255)), (35, 595))

    def draw_start_button():
        pygame.draw.rect(screen, (10, 180, 10), button_start, border_radius=15)
        text = font_start.render("START", True, (0, 0, 0))
        screen.blit(text, (button_start.x + 30, button_start.y + 10))
    def draw_continue_button():
        pygame.draw.rect(screen, (10, 180, 10), button_continue, border_radius=15)
        text = font_start.render("Continue", True, (0, 0, 0))
        screen.blit(text, (button_continue.x + 30, button_continue.y + 10))

    running = True
    gameStart = False
    mission_complete = False

    while running :
        screen.fill((0,0,0))
        screen.blit(backgp,(0,0))
        pygame.draw.line(screen,(0,0,0),(0,545),(750,545),8)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and gameStart==False:
                    gameStart = True
                    mixer.music.set_volume(0.2)
                    jetSo = mixer.Sound('assets/sounds/jet s.ogg')
                    jetSo.play(-1)
                    jetSo.set_volume(0.6)
                    score_value=0
                if event.key == pygame.K_RIGHT:
                    X_value=jet_change  #change
                    jet1vis = False
                    jet2vis = True
                if event.key == pygame.K_LEFT:
                    X_value = -jet_change   #change
                    jet2vis = False
                    jet1vis = True
                if event.key == pygame.K_UP:
                    Y_value=-jet_change
                if event.key == pygame.K_DOWN:
                    Y_value=jet_change
                if event.key == pygame.K_s and bombDrop==0:
                    bombDrop=2

            if event.type == pygame.KEYUP:
                Y_value = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if button_down.collidepoint(x, y):
                    Y_value=jet_change
                if button_up.collidepoint(x, y):
                    Y_value=-jet_change
                if button_left.collidepoint(x,y):
                    X_value = -jet_change  # change
                    jet2vis = False
                    jet1vis = True
                if button_right.collidepoint(x, y):
                    X_value = jet_change  # change
                    jet1vis = False
                    jet2vis = True
                if button_start.collidepoint(x, y) and gameStart==False:
                    gameStart = True
                    mixer.music.set_volume(0.2)
                    jetSo = mixer.Sound('assets/sounds/jet s.ogg')
                    jetSo.play(-1)
                    jetSo.set_volume(0.6)
                    score_value=0
                if button_fire.collidepoint(x, y) and bombDrop==0:
                    bombDrop = 2
                if button_continue.collidepoint(x,y):
                    gameStart = True
                    mission_complete = False
                    mixer.music.set_volume(0.2)
                    jetSo = mixer.Sound('assets/sounds/jet s.ogg')
                    jetSo.play(-1)
                    jetSo.set_volume(0.6)
                    score_value = 0

            if event.type == pygame.MOUSEBUTTONUP:
                Y_value = 0




        #gamestart
        if gameStart == True and mission_complete == False:
            #bomb
            if bombDrop == 0:
                bombX = jetX + 40
                bombY = jetY+20
            if bombDrop ==  2:
                bombX = bombX
                bombY +=bomb_change #change


            bombXY(bombX,bombY)

            #militaryVeh

            #mcar
            mcarX+=v_change*2 #change
            if mcarX>=900:
                mcarX=-200
            if exploX-20 <=mcarX<=exploX+200 and exploVi==True: #vehi_blst_conditn
                mcarX=-200
                score_value+=10
            mcarXY(mcarX,mcarY)

            #trk
            trkX += v_change*2  # change
            if trkX >= 1200:
                trkX = -1200
            if exploX - 20 <= trkX <= exploX + 200 and exploVi == True: #vehi_blst_conditn
                trkX = -1200
                score_value += 10
            trkXY(trkX, trkY)

            #mtrk
            mtrkX+=v_change  #change
            if mtrkX>=1000:
                mtrkX=-600
            if exploX-10 <=mtrkX<=exploX+200 and exploVi==True: #vehi_blst_conditn
                mtrkX=-600
                score_value += 30

            mtrkXY(mtrkX,mtrkY)

            if score_value >= 120:
                mission_complete = True
                mixer.music.set_volume(0.4)
                jetSo = mixer.Sound('assets/sounds/jet s.ogg')
                jetSo.stop()

            #missile
            if 10<=missiX<=750:
                missi_lnc=2
            if missi_lnc==0:
                missiX=mtrkX
                missiY=mtrkY
            if missi_lnc==2:
                missiX=missiX
                missiY-=mi_change #change
                if missiY<=mtrkY and missi_So==0:
                    missi_So=2
                    if missi_So==2:
                        missiS=mixer.Sound('assets/sounds/missile s.ogg')
                        missiS.play()
                        missiS.set_volume(0.4)
            if missiY<=-100:
                missiX = mtrkX
                missiY = mtrkY
                missi_So=0
                missi_lnc=0
            if fireVi==2:
                missiY =-99 #missilie stop when jetDEstry

            missiXY(missiX,missiY)

            #jetshow
            if jet1vis == True:
                jet1XY(jetX,jetY)
            if jet2vis == True:
                jet2XY(jetX,jetY)
            if fireVi ==2 :
                fireXY(fireX,fireY)

            #explo
            exploX = bombX - 150
            if bombY>= 525:
                exploVi = True
            if exploVi == True :
                exploC+=10
            if exploC>=1 and exploC<=100 and exploVi == True:
                exp1XY(exploX,exploY)
                if exploC==1:
                    expS=mixer.Sound('assets/sounds/explosion s.ogg')
                    expS.play()
            if exploC>=101 and exploC<=200 and exploVi == True:
                exp2XY(exploX,exploY)
            if exploC>=201 and exploC<=300 and exploVi == True:
                exp3XY(exploX,exploY)
            if exploC>=301 and exploC<=400 and exploVi == True:
                exp4XY(exploX,exploY)
            if exploC>=401 and exploC<=500 and exploVi == True:
                exp5XY(exploX,exploY)
            if exploC>=501 and exploC<=600 and exploVi == True:
                exp6XY(exploX,exploY)
            if exploC>=601 and exploC<=700 and exploVi == True:
                exp7XY(exploX,exploY)
                exploVi = False #renewExplo
                exploC = 0
                bombDrop = 0 #renewBomb
                if jetY>=750:
                    gameStart=False



            #jet
            if fireVi==0:
                jetX += X_value
                if jetX<=-150:
                    X_value = jet_change   # change
                    jet1vis = False
                    jet2vis = True
                if jetX>=850 :
                    X_value = -jet_change   # change
                    jet2vis = False
                    jet1vis = True

                jetY+=Y_value
                if jetY <= 10:
                    jetY = 10
                if jetY >= 250:
                    jetY = 250

            if jetX<=missiX<=jetX+90 and jetY>=missiY and fireVi==0:
                fireVi=2
                jetSo.stop()
                expS = mixer.Sound('assets/sounds/explosion s.ogg')
                expS.play()
            if fireVi==2: #jetblst
                jetX=jetX
                jetY+=jDrop_change #change
            fireX = jetX + 10
            fireY = jetY - 20
            if fireVi==2:
                gameOverXY(100,200)


            #scoreBoard
            scoreXY(scoreX,scoreY)

            draw_buttons()
        if gameStart == True and mission_complete == True:
            draw_continue_button()
            screen.blit(mission_complete_img, (0, 0))
            scoreXY(scoreX+20, scoreY+30)


        if gameStart == False and mission_complete == False:
            screen.blit(coverbg,(-50,0)) #cover page
            draw_start_button()
            scoreXY(10,10)
            jetX = 20
            jetY = 40
            jet1vis = False
            jet2vis = True
            fireX = jetX + 10
            fireY = jetY - 20
            fireVi = 0
            bombX = jetX + 40
            bombY = jetY
            bombDrop = 0
            exploX = bombX - 150
            exploY = 200
            exploVi = False
            exploC = 0
            missiX = mtrkX
            missiY = mtrkY
            missi_lnc = 0
            missi_So = 0
            mtrkX = -600
            mtrkY = 415
            trkX = -1200
            trkY = 495
            mcarX = -100
            mcarY = 505

        # --- frame end ---
        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)
if __name__ == "__main__":
    asyncio.run(main())