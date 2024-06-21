import pygame
from pygame.locals import *
from time import *
from random import *

pygame.init()
screen=pygame.display.set_mode((600,600))
def show_text(msg,x,y,color,size):
        fontobj=pygame.font.SysFont("freesans",size,False,False)
        msgobj=fontobj.render(msg,False,color)
        screen.blit(    msgobj,(x,y))
def Tiles():
    from TileTemplates import templates

    pygame.init()
    screen=pygame.display.set_mode((800,640))
    pygame.display.set_caption('Platformer Game')
    tile=pygame.image.load('C:/Python/Python311/Sprites/Tileset/png/Tiles/2.png')
    tile=pygame.transform.scale(tile,(40,40))
    coin=pygame.image.load('C:/Python/Python311/Sprites/Tileset/png/Object/Mushroom_2.png')
    portal=pygame.image.load('C:/Python/Python311/Sprites/Tileset/png/Object/Sign_1.png')
    portal=pygame.transform.scale(portal,(40,40))
    ninja_idle=[]
    ninja_run=[]

    game = 0
    level = templates[game]
    move=0
    count=0
    tilex=[0]
    tiley=[0]
    x=80
    y=550
    xchange=0
    ychange=0
    jump=0
    right=0
    left=0
    point=0
    end=0
    def show_text(msg,x,y,color,size):
            fontobj=pygame.font.SysFont("freesans",size,False,False)
            msgobj=fontobj.render(msg,False,color)
            screen.blit(msgobj,(x,y))
    dino=[]
    dinoc=1
    for k in range(1,11):
            for l in range(5):
                d=pygame.image.load('C:/Python/Python311/Sprites/Dino/Idle ('+str(k)+').png')
                dino.append(pygame.transform.scale(d,(60,45)))
    dino.append(50)
    for i in range(10):
        for j in range(5):
            a=pygame.image.load('C:/Python/Python311/Sprites/Ninja/Idle__00'+str(i)+'.png')
            ninja_idle.append(pygame.transform.scale(a,(20,40)))
            b=pygame.image.load('C:/Python/Python311/Sprites/Ninja/Run__00'+str(i)+'.png')
            ninja_run.append(pygame.transform.scale(b,(30,40)))
    ninja_idle.append(50)
    ninja_run.append(50)

    GAME = 0
    while True:
        if GAME == 1:
            break
        screen.fill([0,0,0])
        sleep(.01)
        if end == 2:
            screen.fill([0,0,0])
            show_text('Game Completed!',20,80,(255,255,255),95)
            show_text('Points: '+str(point),280,250,(255,255,255),60)
            pygame.draw.rect(screen,(255,0,0),(225,375,375,150))
            show_text("Quit",262.5,367.5,(255,255,255), 150)
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.pos[0]>=225 and event.pos[0]<=600 and event.pos[1]>=375 and event.pos[1]<=525:
                        break
                if event.type==QUIT:
                    pygame.quit()
                    exit()
            pygame.display.update()
            continue
        elif end==1:
            screen.fill([0,0,0])
            show_text('Level Complete',50,80,(255,255,255),100)
            show_text('Points: '+str(point),300,400,(255,255,255),40)
            pygame.draw.rect(screen,(255,0,0),(75,475,250,100))
            show_text("Quit",92.5,467.5,(255,255,255), 100)
            pygame.draw.rect(screen,(0,255,0),(450,475,250,100))
            show_text("Next",517.5,467.5,(255,255,255), 55)
            show_text("Level",507.5,517.5,(255,255,255), 55)
            for event in pygame.event.get():
                if event.type==MOUSEBUTTONDOWN:
                    if event.pos[0]>=75 and event.pos[0]<=325 and event.pos[1]>=475 and event.pos[1]<=575:
                        GAME=1
                    elif event.pos[0]>=450 and event.pos[0]<=700 and event.pos[1]>=475 and event.pos[1]<=575:
                        game+=1
                        level=templates[game]
                        x=80
                        y=550
                        end=0
                        break
                if event.type==QUIT:
                    pygame.quit()
                    exit()
            pygame.display.update()
            continue
        for i in level:
            for j in i:
                if j==4:
                        screen.blit(dino[dinoc],(tilex[-1],tiley[-1]))
                        if tilex[-1]<=x<=tilex[-1]+35 and tiley[-1]<=y<=tiley[-1]+40:
                            point-=1
                            level[tiley[-1]//40][tilex[-1]//40]=0
                if j==3:
                    screen.blit(portal,(tilex[-1],tiley[-1]))
                    if tilex[-1]<=x<=tilex[-1]+50 and tiley[-1]<=y<=tiley[-1]+30:
                        if game >= len(templates)-1:
                            end=2
                        else:
                            end=1
                if j==2:
                        screen.blit(coin,(tilex[-1],tiley[-1]))
                        if tilex[-1]<=x<=tilex[-1]+50 and tiley[-1]<=y<=tiley[-1]+30:
                            point+=1
                            level[tiley[-1]//40][tilex[-1]//40]=0
                            
                if j==1:
                    screen.blit(tile,(tilex[-1],tiley[-1]))
                tilex.append(tilex[-1]+40)
            tilex=[0]
            tiley.append(tiley[-1]+40)
        tiley=[0]
        if level[(y//40) +1][x//40]==1 or level[(y//40)+1][(x+20)//40]==1:
            ychange=0
        elif jump<=0:
            ychange=1
        if level[(y//40)][x//40]==1 or level[y//40][(x+20)//40]==1:
            jump=0
        if right==1:
            xchange=1
        elif left==1:
            xchange=-1
        if level[(y//40)][((x-10)//40)+1]==1 and right==1 or level[((y+10)//40)][((x-1)//40)]==1 and left==1:
            xchange=0
        if y>640:
            break
        if x+xchange<0 or x+xchange>760:
            xchange=0
        if jump>0:
            ychange=-1
        
        x+=xchange*5
        y+=ychange*5
        if move==0:
            current=ninja_idle[-1]
            screen.blit(ninja_idle[count],(x,y))
        if move==1:
            current=ninja_run[-1]
            screen.blit(ninja_run[count],(x,y))

        pygame.draw.ellipse(screen,(200,10,0),(680,5,100,35))
        show_text('Quit',700,5,(255,255,255),30)

        for event in pygame.event.get():
            if event.type==MOUSEBUTTONDOWN:
                if 680<event.pos[0]<780 and 5<event.pos[1]<40:
                    GAME=1
            if event.type==KEYDOWN:
                if event.key==K_RIGHT:
                    move=1
                    right=1
                    xchange=1
                elif event.key==K_LEFT:
                    move=1
                    left=1
                    xchange=-1
                elif event.key==K_UP:
                    if ychange==0:
                        jump=40
            if event.type==KEYUP:
                if event.key==K_RIGHT:
                    right=0
                elif event.key==K_LEFT:
                    left=0
                if event.key==K_RIGHT or event.key==K_LEFT:
                    move=0
                    xchange=0
            if event.type==QUIT:
                pygame.quit()
                exit()
        if count>=current-1:
            count=0
        else:
            count+=1
        if dinoc>=dino[-1]-1:
            dinoc=0
        else:
            dinoc+=1
        show_text(str(point),400,35,(255,255,255),50)
        pygame.display.update()
        jump-=1
def Ninja():
    screen=pygame.display.set_mode((800,600))
    pygame.display.set_caption('Throwing game')
    ninja_idle=[]
    ninja_throw=[]
    dino_idle=[]
    dino_dead=[]
    dino_list=[(randint(-80,620),randint(-15,440))]
    pos=0
    for i in range(10):
        x=pygame.image.load('C:/Python/Python311/Sprites/Ninja/Idle__00'+str(i)+'.png')
        ninja_idle.append(pygame.transform.scale(x,(100,180)))
        z=pygame.image.load('C:/Python/Python311/Sprites/Ninja/Throw__00'+str(i)+'.png')
        ninja_throw.append(pygame.transform.scale(z,(165,180)))
    ninja_idle.append(9)
    ninja_throw.append(9)
    for i in range(1,11):
        a=pygame.image.load('C:/Python/Python311/Sprites/Dino/Idle ('+str(i)+').png')
        a=pygame.transform.flip(a,True,False)
        dino_idle.append(pygame.transform.scale(a,(180,180)))
    dino_idle.append(10)
    for i in range(1,9):
        b=pygame.image.load('C:/Python/Python311/Sprites/Dino/Dead ('+str(i)+').png')
        b=pygame.transform.flip(b,True,False)
        dino_dead.append(pygame.transform.scale(b,(180,180)))
    dino_dead.append(8)
    kunai=pygame.image.load('C:/Python/Python311/Sprites/Ninja/Kunai.png')
    kunai=pygame.transform.scale(kunai,(17,70))
    kunai=pygame.transform.rotate(kunai,-90)
    klist=[] #list of all the kunai thrown
    count=0 #variable for showing the sprite
    move=0 #variable to check if ninja is moving, 0 is idle, else is moving
    check=0
    alivedino=1 #variable for if dino is alive
    dino_count=1 #variable for dino sprite
    deaddino=0 #checks if dino has been killed
    score=0
    GAME=0
    while True:
        if GAME==1:
            break
        screen.fill([0,0,0])
        sleep(.05)
        show_text(str(score),400,500,(255,255,255),100)
        if move==0:
            current=ninja_idle[-1]#tells what count should go to
            screen.blit(ninja_idle[count],(100,100))
        if move==1:
            if check==0:
                count=0
                check=1
            current=ninja_idle[-1]#tells what count should go to
            screen.blit(ninja_throw[count],(63,103))
            if count>current-1:
                move=0
        for i in klist:
            if len(i)>3:
                klist.remove(i) #removes the kunai if it passes the end
                continue
            screen.blit(kunai,(i[0],i[1]))
            if i[0]+10>800:
                i[0]=100 
                i.append(1)     # increases/changes position of the kunai
            i[0]+=i[2][1]/20       #adds x to the kunai's x coor. 20 is how many times it will update untill it reaches the pos
            i[1]+=i[2][0]/20       #adds y to the kunai's y coor. Same as above
        if deaddino==1:
            dino_current=dino_dead[-1]#tells what dino count should go to
            alivedino=0
            if dino_count < dino_current-1:
                screen.blit(dino_dead[dino_count],dino_list[0])
            else:
                deaddino=0
                alivedino=1
                x=randint(-80,620)
                y=randint(-15,440)
                dino_list.pop(0)
                dino_list.append((x,y))
                score+=1
        if alivedino==1:
            dino_current=dino_idle[-1]#tells what dino cout should go to
            for i in klist:
                if dino_list[0][0]+180>=i[0]+65>=dino_list[0][0]+85 and dino_list[0][1]+180>=i[1]+9>=dino_list[0][1]+20:
                    deaddino=1
            screen.blit(dino_idle[dino_count], dino_list[0]) #-80,620 is x   -15,440 is y
        if dino_count>=dino_current-1:
            dino_count=1
        else:
            dino_count+=1
        if count>current-1:
            count=0
        else:
            count+=1
        pygame.draw.ellipse(screen,(200,10,0),(680,5,100,35))
        show_text('Quit',700,5,(255,255,255),30)
        for event in pygame.event.get():
            if event.type==MOUSEBUTTONDOWN:
                if 680<event.pos[0]<780 and 5<event.pos[1]<40:
                    GAME=1
                slope=[(event.pos[1]-180),(event.pos[0]-203)]
                klist.append([203,180,slope])#adds the coor of kunai and endpoint
                move=1
                check=0
            if event.type==QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
def Balloon():
    screen=pygame.display.set_mode((600,600))
    pygame.display.set_caption('Balloon')
    y=570
    coor=[]
    score=0
    for i in range(10):
        x=(i*60)+30
        y=randint(500,570)
        letter=randint(97,122)
        coor.append([x,y,letter])
    end=0
    GAME=0
    while True:
        if GAME==1:
            break
        for i in coor:
            if i[1]<-30:
                screen.fill([0,100,200])
                show_text("Game Over",50,50,(255,255,255),100)
                show_text("Score: "+str(score),100,300,(255,255,255),100)
                pygame.display.update()
                end=1
        if end==1:
            break
        sleep(.01)
        screen.fill([0,100,200])
        show_text(str(score),290,50,(255,255,255),70)
        for i in range(len(coor)):
            pygame.draw.circle(screen,(200,20,40),(coor[i][0],coor[i][1]),30)
            show_text(chr(coor[i][2]),(coor[i][0])-10,(coor[i][1])-20,(255,255,255),30)
            coor[i][1]-=1
        pygame.draw.ellipse(screen,(200,10,0),(480,5,100,35))
        show_text('Quit',500,5,(255,255,255),30)
        for event in pygame.event.get():
            if event.type==MOUSEBUTTONDOWN:
                if 480<event.pos[0]<580 and 5<event.pos[1]<40:
                    GAME=1
            if event.type==KEYDOWN:
                for i in range(len(coor)):
                    if event.key == coor[i][2]:
                        coor.pop(i)
                        score+=2
                        break
                coor.append([randint(30,570),650,randint(97,122)])
                score-=1
            if event.type==QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
def Hangman():
    screen=pygame.display.set_mode((600,600))
    pygame.display.set_caption('Hangman')
    def show_text(msg,x,y,color,size):
            fontobj=pygame.font.SysFont("freesans",size,False,False)
            msgobj=fontobj.render(msg,False,color)
            screen.blit(msgobj,(x,y))
    l=['concession','hay','remind','freight','seat','factor','jet','colony','cafe','welcome','mother','father']
    x=0
    wrong=[]
    word=choice(l)
    correct=['']*len(word)
    lword=list(word)
    GAME=0
    while True:
        if GAME==1:
            break
        c=0
        if ''.join(correct)==word:
            sleep(.5)
            show_text("You Won",30,5,(0,0,0),100)
            pygame.display.update()
            break
        elif len(wrong)==6:
            sleep(.5)
            show_text("You Lost",30,5,(0,0,0),100)
            show_text("The word was "+word,5,100,(0,0,0),40)
            pygame.display.update()
            break
        screen.fill([255,255,255])
        pygame.draw.ellipse(screen,(200,10,0),(480,5,100,35))
        show_text('Quit',500,5,(255,255,255),30)
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if chr(event.key) in lword:
                    for i in range(len(lword)):
                        if lword[i]==chr(event.key):
                            correct[i]=chr(event.key)
                            lword[i]=''
                else:
                    if chr(event.key) not in wrong and chr(event.key) not in correct:
                        wrong.append(chr(event.key))
            if event.type==MOUSEBUTTONDOWN:
                if 480<event.pos[0]<580 and 5<event.pos[1]<40:
                    GAME=1
            if event.type==QUIT:
                pygame.quit()
                exit()
        for i in word:
            pygame.draw.rect(screen,(0,0,0),(c+10,500,50,5))
            c+=60
        c=0
        for i in correct:
            if i.isalpha():
                show_text(i,c+10,450,(0,0,0),40)
            c+=60
        c=0
        for i in wrong:
            show_text(i,c+10,500,(0,0,0),40)
            c+=60
        c=0
        pygame.draw.rect(screen,(0,0,0),(430,420,150,10))
        pygame.draw.rect(screen,(0,0,0),(500,100,10,320))
        pygame.draw.rect(screen,(0,0,0),(400,100,100,10))
        pygame.draw.rect(screen,(0,0,0),(415,110,5,30))
         
        for i in range(len(wrong)):
            if i==0:
                pygame.draw.circle(screen,(0,0,0),(417.5,165),30,5)
            if i==1:
                pygame.draw.rect(screen,(0,0,0),(415,195,5,100))
            if i==2:
                pygame.draw.line(screen,(0,0,0),(385,410),(417.5,295),5)
            if i==3:
                pygame.draw.line(screen,(0,0,0),(445,410),(417.5,295),5)
            if i==4:
                pygame.draw.line(screen,(0,0,0),(375,310),(417.5,225),5)
            if i==5:
                pygame.draw.line(screen,(0,0,0),(458,310),(417.5,225),5)
        pygame.display.update()
def FB():
    screen=pygame.display.set_mode((600,600))
    pygame.display.set_caption('Flappy Bird')
    def pipe(x,y):
        pygame.draw.rect(screen,(0,200,20),(x,y,100,50))
        pygame.draw.rect(screen,(0,200,20),(x+15,0,70,y))
        pygame.draw.rect(screen,(0,200,20),(x,y+150,100,50))
        pygame.draw.rect(screen,(0,200,20),(x+15,y+200,70,600-y))
    def show_text(msg,x,y,color,size):
        fontobj=pygame.font.SysFont("freesans",size,False,False)
        msgobj=fontobj.render(msg,False,color)
        screen.blit(msgobj,(x,y))
    pipelist=[]
    count=0
    birdy=300
    var=0
    points=0
    pcount=0
    check=0
    GAME=0
    while True:
        if GAME==1:
            break
        sleep(.004)
        screen.fill([5,150,200])
        if pcount==1:
            points+=1
            pcount=0
        if birdy>590 or birdy<10:
            break
        if count%500==0:
            x=600
            y=randint(70,400)
            pipelist.append([x,y])
        for i in pipelist:
            pipe(i[0],i[1])
            i[0]-=1
            if i[0]<=-100:
                pipelist.remove(i)
                check=0
        if 50<pipelist[0][0]<=150 and birdy-10<pipelist[0][1] or 50<pipelist[0][0]<150 and birdy+10>pipelist[0][1]+150 or 50<pipelist[0][0]<150 and birdy-10<=pipelist[0][1]+50:
            break
        elif pipelist[0][0]+100<50 and check!=1:
            pcount=1
            check=1
        pygame.draw.circle(screen,(0,0,0),(150,birdy),10)
        pygame.draw.ellipse(screen,(200,10,0),(480,5,100,35))
        show_text('Quit',500,5,(255,255,255),30)
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key==32:
                    birdy-=30
                    var=70
            if event.type==MOUSEBUTTONDOWN:
                if 480<event.pos[0]<580 and 5<event.pos[1]<40:
                    GAME=1
            if event.type==QUIT:
                pygame.quit()
                exit()
        show_text(str(points),250,150,(255,255,255),100)
        pygame.display.update()
        count+=1
        if var>0:
            var-=1
        else:
            birdy+=1
def Snake():
    screen=pygame.display.set_mode((600,600))
    pygame.display.set_caption('Snake Game')
    x=300
    y=300
    xchange=1
    ychange=0
    count=0
    flist=[]
    snakelen=[1]
    coor=[[x,y]]
    end=0
    points=0
    speed=1
    segment=0
    barriers=1
    GAME=0
    while barriers==1:
        show_text("Barriers?",105,200,(255,255,255),100)
        pygame.draw.rect(screen,(0,200,10),(35,75,250,100))
        show_text("Yes",90,85,(250,255,255), 70)
        pygame.draw.rect(screen,(200,10,0),(315,75,250,100))
        show_text("No",370,85,(255,255,255), 70)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==MOUSEBUTTONDOWN:
                if 35<event.pos[0]<285 and 75<event.pos[1]<175:
                        barriers='yes'
                elif 315<event.pos[0]<565 and 75<event.pos[1]<175:
                        barriers='no'
    while True:
            if GAME==1:
                break
            screen.fill([0,0,0])
            color=(randint(0,255),randint(0,255),randint(0,255))
            a,b=0,0
            sleep(.005)
            if barriers=='yes':
                if x+15>=600 or x-15<=0 or y+15>=600 or y-15<=0:
                    screen.fill([0,0,0])
                    show_text("Game Over",50,100,(255,255,255),100)
                    pygame.display.update()
                    break
            else:
                if x-15>=600:
                    x=-15
                elif x+15<=0:
                    x=615
                elif y-15>=600:
                    y=-15
                elif y+15<=0:
                    y=615
            if segment==10:
                segment=0
                snakelen=[1]
                speed+=.1
                
            if end==1:
                screen.fill([0,0,0])
                show_text("Game Over",50,100,(255,255,255),100)
                pygame.display.update()
                break
            if count%500==0:
                c1,c2=randint(10,590),randint(10,590)
                flist.append((c1,c2))
            if count%2000==0:
                flist.pop(0)
            for i in flist:
                pygame.draw.circle(screen,color,i,10)
            for i in flist:
                if x+15>i[0]>x-15 and y+15>i[1]>y-15:
                    flist.remove(i)
                    points+=1
                    segment+=1
                    for i in range(10):
                        snakelen.append(1)
            for i in range(len(snakelen)):
                pygame.draw.circle(screen,(0,100,200),(coor[i][0],coor[i][1]),20)
                pygame.draw.circle(screen,(255,255,255),(coor[0][0]+xchange*5,coor[0][1]+ychange*5),10)
            for i in range(len(snakelen)):
                if len(snakelen)>2:
                    if coor[0][0]+15>coor[i+30][0]>coor[0][0]-15 and coor[0][1]+15>coor[i+30][1]>coor[0][1]-15:
                        end=1
                        break
            pygame.draw.ellipse(screen,(200,10,0),(480,5,100,35))
            show_text('Quit',500,5,(255,255,255),30)
            for event in pygame.event.get():
                if event.type==KEYDOWN and 1073741903<=event.key<=1073741906:
                    a,b=xchange,ychange
                    xchange,ychange=0,0
                    if event.key==K_RIGHT:
                        if a==-1:
                            xchange=-1
                        else:
                            xchange=1
                    if event.key==K_LEFT:
                        if a==1:
                            xchange=1
                        else:
                            xchange=-1
                    if event.key==K_UP:
                        if b==1:
                            ychange=1
                        else:
                            ychange=-1
                    if event.key==K_DOWN:
                        if b==-1:
                            ychange=-1
                        else:
                            ychange=1
                if event.type==MOUSEBUTTONDOWN:
                    if 480<event.pos[0]<580 and 5<event.pos[1]<40:
                        GAME=1
                if event.type==QUIT:
                    pygame.quit()
                    exit()
            x+=xchange*speed
            y+=ychange*speed
            coor.insert(0,[x,y])
            show_text(str(points),280,100,(255,255,255),100)
            pygame.display.update()
            count+=1
def TTT():
    screen=pygame.display.set_mode((600,600))
    pygame.display.set_caption('Tic Tac Toe')
    count=0
    w=-1
    ttt={1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    GAME=0
    while True:
        if GAME==1:
            break
        pygame.draw.line(screen,(255,0,0),(200,0),(200,600),5)
        pygame.draw.line(screen,(255,0,0),(400,0),(400,600),5)
        pygame.draw.line(screen,(255,0,0),(0,200),(600,200),5)
        pygame.draw.line(screen,(255,0,0),(0,400),(600,400),5)
        if ttt[1]==ttt[2]==ttt[3]!=0:
            pygame.draw.line(screen,(255,255,255),(100,25),(100,575),5)
            pygame.display.update()
            w=ttt[1]
        elif ttt[4]==ttt[5]==ttt[6]!=0:
            pygame.draw.line(screen,(255,255,255),(300,25),(300,575),5)
            pygame.display.update()
            w=ttt[6]
        elif ttt[7]==ttt[8]==ttt[9]!=0:
            pygame.draw.line(screen,(255,255,255),(500,25),(500,575),5)
            pygame.display.update()
            w=ttt[7]
        elif ttt[1]==ttt[4]==ttt[7]!=0:
            pygame.draw.line(screen,(255,255,255),(25,100),(575,100),5)
            pygame.display.update()
            w=ttt[7]
        elif ttt[2]==ttt[5]==ttt[8]!=0:
            pygame.draw.line(screen,(255,255,255),(25,300),(575,300),5)
            pygame.display.update()
            w=ttt[2]
        elif ttt[3]==ttt[6]==ttt[9]!=0:
            pygame.draw.line(screen,(255,255,255),(25,500),(575,500),5)
            pygame.display.update()
            w=ttt[6]
        elif ttt[1]==ttt[5]==ttt[9]!=0:
            pygame.draw.line(screen,(255,255,255),(25,25),(575,575),5)
            pygame.display.update()
            w=ttt[1]
        elif ttt[7]==ttt[5]==ttt[3]!=0:
            pygame.draw.line(screen,(255,255,255),(25,575),(575,25),5)
            pygame.display.update()
            w=ttt[7]
        if w>0:
            sleep(1)
            screen.fill([0,0,0])
            show_text('Player '+str(w)+' Wins!!',45,150,(0,100,200),80)
            pygame.display.update()
            break
        elif 0 not in ttt.values():
            sleep(1)
            screen.fill([0,0,0])
            show_text('Draw!!',200,250,(0,200,100),80)
            pygame.display.update()
            break
        pygame.draw.ellipse(screen,(200,10,0),(480,5,100,35))
        show_text('Quit',500,5,(255,255,255),30)
        for event in pygame.event.get():
            if event.type==MOUSEBUTTONDOWN:
                if 480<event.pos[0]<580 and 5<event.pos[1]<40:
                    GAME=1
                if 200 in event.pos or 400 in event.pos:
                    break
                if event.pos[0]<200 and event.pos[1]<200:
                    if ttt[1]!=0:
                        continue
                    else:
                        if count%2==0:
                            event.pos=(25,25)
                            ttt[1]=1
                        else:
                            event.pos=(100,100)
                            ttt[1]=2
                elif event.pos[0]<200 and 200<event.pos[1]<400:
                    if ttt[2]!=0:
                        continue
                    else:
                        if count%2==0:
                            event.pos=(25,225)
                            ttt[2]=1
                        else:
                            event.pos=(100,300)
                            ttt[2]=2
                elif event.pos[0]<200 and event.pos[1]>400:
                    if ttt[3]!=0:
                        continue
                    else:
                        if count%2==0:
                            event.pos=(25,425)
                            ttt[3]=1
                        else:
                            event.pos=(100,500)
                            ttt[3]=2
                elif 200<event.pos[0]<400 and event.pos[1]<200:
                    if ttt[4]!=0:
                        continue
                    else:
                        if event.pos[1]<200:
                            if count%2==0:
                                event.pos=(225,25)
                                ttt[4]=1
                            else:
                                event.pos=(300,100)
                                ttt[4]=2
                elif 200<event.pos[0]<400 and 200<event.pos[1]<400:
                    if ttt[5]!=0:
                        continue
                    else:
                        if count%2==0:
                            event.pos=(225,225)
                            ttt[5]=1
                        else:
                            event.pos=(300,300)
                            ttt[5]=2
                elif 200<event.pos[0]<400 and event.pos[1]>400:
                    if ttt[6]!=0:
                        continue
                    else:
                        if count%2==0:
                            event.pos=(225,425)
                            ttt[6]=1
                        else:
                            event.pos=(300,500)
                            ttt[6]=2
                elif event.pos[0]>400 and event.pos[1]<200:
                    if ttt[7]!=0:
                        continue
                    else:
                        if event.pos[1]<200:
                            if count%2==0:
                                event.pos=(425,25)
                                ttt[7]=1
                            else:
                                event.pos=(500,100)
                                ttt[7]=2
                elif event.pos[0]>400 and 200<event.pos[1]<400:
                    if ttt[8]!=0:
                        continue
                    else:
                        if count%2==0:
                            event.pos=(425,225)
                            ttt[8]=1
                        else:
                            event.pos=(500,300)
                            ttt[8]=2
                elif event.pos[0]>400 and event.pos[1]>400:
                    if ttt[9]!=0:
                        continue
                    else:
                        if count%2==0:
                            event.pos=(425,425)
                            ttt[9]=1
                        else:
                            event.pos=(500,500)
                            ttt[9]=2
                if count%2==0:
                    pygame.draw.line(screen,(100,0,0),event.pos,(event.pos[0]+150,event.pos[1]+150),5)
                    pygame.draw.line(screen,(100,0,0),(event.pos[0]+150,event.pos[1]),(event.pos[0],event.pos[1]+150),5)
                else:
                    pygame.draw.circle(screen,(100,0,0),event.pos,75,5)
                count+=1
            if event.type==QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
def Pong():
    screen=pygame.display.set_mode((600,600))
    pygame.display.set_caption('Pong')
    y1,y2=100,100
    y1change,y2change=0,0
    cx,cy=300,300
    p1,p2=0,0
    time=18000
    p=0
    cxchange,cychange=choice([-1,1]),uniform(-1,1)
    GAME=0
    while True:
        if GAME==1:
            break
        sleep(.002)
        screen.fill([0,0,0])
        if time<=0:
            screen.fill([0,0,0])
            show_text('Times Up!',100,150,(255,255,255),75)
            if p1>p2:
                show_text('Player 1 Wins!!',45,250,(0,200,100),75)
            elif p1==p2:
                show_text("It's a tie!",140,250,(255,255,255),75)
            else:
                show_text('Player 2 Wins!!',45,250,(0,100,200),75)
            pygame.display.update()
            break
        if p1==10:
            show_text('Player 1 Wins!!',45,200,(0,200,100),75)
            pygame.display.update()
            break
        elif p2==10:
            show_text('Player 2 Wins!!',45,200,(0,100,200),75)
            pygame.display.update()
            break
        show_text(str(time//300),260,20,(255,255,255),40)
        show_text('Player 1: '+str(p1),20,25,(0,200,100),40)
        show_text('Player 2: '+str(p2),360,25,(0,100,200),40)
        pygame.draw.line(screen,(184,115,51),(0,97.5),(600,97.5),5)
        pygame.draw.circle(screen,(255,255,255),(cx,cy),20)
        pygame.draw.rect(screen,(0,200,50),(20,y1,10,200))
        pygame.draw.rect(screen,(0,50,200),(530,y2,10,200))
        if y1+y1change>400 or y1+y1change<100:
            y1change=0
        if y2+y2change>400 or y2+y2change<100:
            y2change=0
        y2+=y2change
        y1+=y1change
        if cx+20==530 and cy-20<y2+200 and cy+20>y2 or  cx-20==30 and cy-20<y1+200 and cy+20>y1:
            cxchange=-cxchange
        cx+=cxchange
        cy+=cychange
        if cx>620:
            cx,cy=300,300
            cychange,cxchange=uniform(-1,1),choice([-1,1])
            p1+=1
            p=1
        elif cx<-20:
            sleep(.01)
            cx,cy=300,300
            cychange,cxchange=uniform(-1,1),choice([-1,1])
            p2+=1
            p=1
        if cy<120:
            cychange=1
        elif cy>580:
            cychange=-1
        pygame.draw.ellipse(screen,(200,10,0),(480,5,100,35))
        show_text('Quit',500,5,(255,255,255),30)
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key==K_DOWN:
                    y2change=1
                elif event.key==K_UP:
                    y2change=-1
                if event.key==K_s:
                    y1change=1
                elif event.key==K_w:
                    y1change=-1
            if event.type==KEYUP:
                y1change,y2change=0,0
            if event.type==MOUSEBUTTONDOWN:
                if 480<event.pos[0]<580 and 5<event.pos[1]<40:
                    GAME=1
            if event.type==QUIT:
                pygame.quit()
                exit()
        
        pygame.display.update()
        time-=1
