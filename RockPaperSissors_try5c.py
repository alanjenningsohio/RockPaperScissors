# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 01:38:27 2017

@author: JenningsFamily
"""
import pygame 
import random 
import pygame.time as pgtime  
pygame.init()

class ModelParamZ:
    def __init__(self):
        self.ProbRandStratagy = 0.2
        # this is the likelihood that the stratagy is departed from
        # Used to prevent models from making rigid predictions

class RPSParam:
    def __init__(self):
        self.CountGroup = 30; # number of counts per Rock, Paper, Sissors, Shoot
        self.FrameTime  = 50; # Delay time in msec for single frame
        self.MaxFrameRate = 50; # in fps
        # n.b. that long frame times will make program less responsive because sample relative to frame will be small

class ColorZ:
    def __init__(self):
        self.Aqua =( 0, 255, 255)
        self.Black= ( 0, 0, 0)
        self.Blue =( 0, 0, 255)
        self.Red =( 255, 0, 0)
        self.White =( 255, 255, 255)
        
class LayoutParam:
    def __init__(self):
        self.TopMargin = 25
        self.LeftMargin = 25
        self.ButtWidth = 100 # these are the clicking buttons
        self.ButtHeight = self.ButtWidth # make them square 
        self.MenuHeight = 30 # this is help, quit, start 
        self.MenuWidth = self.ButtWidth # match the buttons for pretty colums
        self.Spacing = 10
        self.FontSize = 20
        self.Width = 2*self.LeftMargin+4*self.ButtWidth+3*self.Spacing
        self.Height = 2*self.TopMargin+3*self.ButtHeight+3*self.Spacing+self.MenuHeight
        self.ButtonPixHelp = [self.LeftMargin,self.TopMargin,
                              self.MenuWidth,self.MenuHeight] # not yet used 
        self.ButtonPixQuit = [self.Width-self.LeftMargin-self.MenuWidth,self.TopMargin,
                              self.MenuWidth,self.MenuHeight]
        self.ButtonPixScore= [self.LeftMargin+self.MenuWidth+self.Spacing,self.TopMargin,
                              self.Width-2*self.LeftMargin-2*self.MenuWidth-2*self.Spacing,self.MenuHeight]
        self.ButtonPixCount= [self.Width/2,self.Height-self.TopMargin-self.MenuHeight/2] # n.b. this is a center
        self.ButtonPixStart= [self.Width/2-self.MenuWidth/2,
                              self.TopMargin+self.MenuHeight+self.Spacing,
                              self.MenuWidth,self.MenuHeight]
        self.ButtonPixRest= [self.Width/2-self.MenuWidth/2,
                              self.TopMargin+2*self.MenuHeight+2*self.Spacing,
                              self.MenuWidth,self.MenuHeight]
        self.ButtonPixL1 = [self.LeftMargin,self.TopMargin+self.MenuHeight+self.Spacing,
                              self.ButtWidth,self.ButtHeight]
        self.ButtonPixL2 = [self.LeftMargin,self.TopMargin+self.MenuHeight+2*self.Spacing+self.ButtHeight,
                            self.ButtWidth,self.ButtHeight]
        self.ButtonPixL3 = [self.LeftMargin,self.TopMargin+self.MenuHeight+3*self.Spacing+2*self.ButtHeight,
                            self.ButtWidth,self.ButtHeight]
        self.ButtonPixLP = [self.LeftMargin+self.ButtWidth+self.Spacing,
                            self.TopMargin+self.MenuHeight+2*self.Spacing+self.ButtHeight,
                            self.ButtWidth,self.ButtHeight]
        self.ButtonPixR1 = [self.Width-self.LeftMargin-self.ButtWidth,
                            self.TopMargin+self.MenuHeight+self.Spacing,
                            self.ButtWidth,self.ButtHeight]
        self.ButtonPixR2 = [self.Width-self.LeftMargin-self.ButtWidth,
                            self.TopMargin+self.MenuHeight+2*self.Spacing+self.ButtHeight,
                            self.ButtWidth,self.ButtHeight]
        self.ButtonPixR3 = [self.Width-self.LeftMargin-self.ButtWidth,
                            self.TopMargin+self.MenuHeight+3*self.Spacing+2*self.ButtHeight,
                            self.ButtWidth,self.ButtHeight]
        self.ButtonPixRP = [self.Width-self.LeftMargin-2*self.ButtWidth-self.Spacing,
                            self.TopMargin+self.MenuHeight+2*self.Spacing+self.ButtHeight,
                            self.ButtWidth,self.ButtHeight]
        self.WinnerImage = [self.Width/2-self.ButtWidth/2,
                            self.TopMargin+self.MenuHeight+3*self.Spacing+2*self.ButtHeight,
                            self.ButtWidth,self.ButtHeight]
        self.StartLogo = [self.Width/2-100,self.TopMargin+self.MenuHeight+self.Spacing,
                          200,100]
        self.PlayerChoiceL = [self.Width/3-50,self.TopMargin+self.MenuHeight+2*self.Spacing+100,
                              100, 50]
        self.PlayerChoiceR = [self.Width*2/3-50,self.TopMargin+self.MenuHeight+2*self.Spacing+100, 100, 50]

def loadImages(target_object):
        target_object.ImgB =pygame.image.load( 'Img_RPS.gif')
        target_object.ImgR =pygame.image.load( 'Img_Rock.gif')
        target_object.ImgP =pygame.image.load( 'Img_Paper.gif')
        target_object.ImgS =pygame.image.load( 'Img_Sissors.gif')
        target_object.ImgWL=pygame.image.load( 'Img_Win_L.gif')
        target_object.ImgWR=pygame.image.load( 'Img_Win_R.gif')
        target_object.ImgWN=pygame.image.load( 'Img_Win_Not.gif')


class RPSButtons(pygame.sprite.Sprite):
    def __init__(self,RPS,Loc):
        super().__init__()
        loadImages(self)
        self.LayoutParam = LayoutParam()
        if   (RPS==0):
            self.image=self.ImgR
            self.rect =self.image.get_rect()
            if Loc =='L':
                self.rect.x=self.LayoutParam.ButtonPixL1[0]
                self.rect.y=self.LayoutParam.ButtonPixL1[1]
            elif Loc == 'R':
                self.rect.x=self.LayoutParam.ButtonPixR1[0]
                self.rect.y=self.LayoutParam.ButtonPixR1[1]
        elif (RPS==1):
            self.image=self.ImgP
            self.rect =self.image.get_rect()
            if Loc =='L':
                self.rect.x=self.LayoutParam.ButtonPixL2[0]
                self.rect.y=self.LayoutParam.ButtonPixL2[1]
            elif Loc == 'R':
                self.rect.x=self.LayoutParam.ButtonPixR2[0]
                self.rect.y=self.LayoutParam.ButtonPixR2[1]
        elif (RPS==2):
            self.image=self.ImgS
            self.rect =self.image.get_rect()
            if Loc =='L':
                self.rect.x=self.LayoutParam.ButtonPixL3[0]
                self.rect.y=self.LayoutParam.ButtonPixL3[1]
            elif Loc == 'R':
                self.rect.x=self.LayoutParam.ButtonPixR3[0]
                self.rect.y=self.LayoutParam.ButtonPixR3[1]
        pygame.display.flip()

class RPSGame():
    def __init__(self):
        self.ColorZ = ColorZ()
        self.LayoutParam = LayoutParam()
        self.RPSParam = RPSParam()
        loadImages(self)
        self.screen=pygame.display.set_mode([
                self.LayoutParam.Width, self.LayoutParam.Height])
        pygame.display.set_caption("Rock, Paper, Sissors")
        self.clock=pgtime.Clock()
        self.Player_L_Type = 'Blank' # this is used to select a player version, e.g. human or computer
        self.Player_R_Type = 'Blank' 
        self.RunGame()

    
    def msg(self,txt,color,size,x,y):
        font=pygame.font.SysFont("bold",size)
        msgtxt=font.render(txt,True,color)
        msgrect=msgtxt.get_rect()
        msgrect.center=x,y
        self.screen.blit(msgtxt,msgrect)
        pygame.display.flip()

    def RunGame(self):
        # create the players for the game
        self.IntroScreen()
        self.AddObjects()
        # Start 
        while 1:
            self.RunRound()
            self.ProcessResult()
            pgtime.delay(50)
            self.RestartScreen()
        

    def IntroScreen(self):
        temp_boxL1 = list(self.LayoutParam.PlayerChoiceL)
        temp_boxL2 = list(self.LayoutParam.PlayerChoiceL)
        temp_boxL2[1]+=temp_boxL2[3]
        temp_boxL3 = list(self.LayoutParam.PlayerChoiceL)
        temp_boxL3[1]+=2*temp_boxL3[3]
        temp_boxR1 = list(self.LayoutParam.PlayerChoiceR)
        temp_boxR2 = list(self.LayoutParam.PlayerChoiceR)
        temp_boxR2[1]+=temp_boxR2[3]
        temp_boxR3 = list(self.LayoutParam.PlayerChoiceR)
        temp_boxR3[1]+=2*temp_boxR3[3]
        wait_L=1
        wait_R=1
        while wait_L or wait_R:
            self.clock.tick(50)
            #self.screen.fill(self.ColorZ.Black) # not required since buttons don't extend to blackness  
            #pygame.display.flip()
            cur=pygame.mouse.get_pos()
            click=pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
        
            temp_flag = self.HighlightPlayerBox(temp_boxL1,'Player',cur,click)
            if not temp_flag:
                wait_L = 0
                self.Player_L_Type = 'Human'
            temp_flag = self.HighlightPlayerBox(temp_boxL2,'Cmp: Nash',cur,click)
            if not temp_flag:
                wait_L = 0
                self.Player_L_Type = 'Cmp_Nash'
            temp_flag = self.HighlightPlayerBox(temp_boxL3,'Cmp: Beat Last',cur,click)
            if not temp_flag:
                wait_L = 0
                self.Player_L_Type = 'Cmp_BeatLast'

            temp_flag = self.HighlightPlayerBox(temp_boxR1,'Player',cur,click)
            if not temp_flag:
                wait_R = 0
                self.Player_R_Type = 'Human'
            temp_flag = self.HighlightPlayerBox(temp_boxR2,'Cmp: Nash',cur,click)
            if not temp_flag:
                wait_R = 0
                self.Player_R_Type = 'Cmp_Nash'
            temp_flag = self.HighlightPlayerBox(temp_boxR3,'Cmp: Beat Last',cur,click)
            if not temp_flag:
                wait_R = 0
                self.Player_R_Type = 'Cmp_BeatLast'


            # Check for exit 
            if (self.LayoutParam.ButtonPixQuit[0]+self.LayoutParam.ButtonPixQuit[2]>cur[0]>self.LayoutParam.ButtonPixQuit[0] and
                self.LayoutParam.ButtonPixQuit[1]+self.LayoutParam.ButtonPixQuit[3]>cur[1]>self.LayoutParam.ButtonPixQuit[1]): 
                pygame.draw.rect(self.screen,self.ColorZ.Blue,self.LayoutParam.ButtonPixQuit)
                self.msg("Quit",self.ColorZ.Red,self.LayoutParam.FontSize,
                    self.LayoutParam.ButtonPixQuit[0]+self.LayoutParam.ButtonPixQuit[2]/2,
                    self.LayoutParam.ButtonPixQuit[1]+self.LayoutParam.ButtonPixQuit[3]/2)
                pygame.display.flip()
                if click[0]==1:
                    pygame.quit()
                    quit()
            else: #Cursor not over the exit button
                pygame.draw.rect(self.screen,self.ColorZ.Aqua,self.LayoutParam.ButtonPixQuit)
                self.msg("Exit",self.ColorZ.Black,self.LayoutParam.FontSize,
                    self.LayoutParam.ButtonPixQuit[0]+self.LayoutParam.ButtonPixQuit[2]/2,
                    self.LayoutParam.ButtonPixQuit[1]+self.LayoutParam.ButtonPixQuit[3]/2)
                pygame.display.flip()
            # TODO Add help menu 

    def HighlightPlayerBox(self,box_in,Label,cur,click):
        if (box_in[0]+box_in[2]>cur[0]>box_in[0] and
            box_in[1]+box_in[3]>cur[1]>box_in[1]): 
                pygame.draw.rect(self.screen,self.ColorZ.Blue,box_in)
                self.msg(Label,self.ColorZ.Red,self.LayoutParam.FontSize,
                    box_in[0]+box_in[2]/2,
                    box_in[1]+box_in[3]/2)
                pygame.display.flip()
                if click[0]==1:
                    return 0 
        else: #Cursor not over the button 
                pygame.draw.rect(self.screen,self.ColorZ.Aqua,box_in)
                self.msg(Label,self.ColorZ.Black,self.LayoutParam.FontSize,
                    box_in[0]+box_in[2]/2,
                    box_in[1]+box_in[3]/2)
                pygame.display.flip()
        return 1 


    def AddObjects(self):
        if   self.Player_L_Type =='Human':
             self.Player_L = Player_Human("L")
        elif self.Player_L_Type =='Cmp_Nash':
             self.Player_L = Player_Comp_Nash("L")
        elif self.Player_L_Type =='Cmp_BeatLast':
             self.Player_L = Player_Comp_BeatLast("L")
        if   self.Player_R_Type =='Human':
             self.Player_R = Player_Human("R")
        elif self.Player_R_Type =='Cmp_Nash':
             self.Player_R = Player_Comp_Nash("R")
        elif self.Player_R_Type =='Cmp_BeatLast':
             self.Player_R = Player_Comp_BeatLast("R")
        self.ButtL0 = RPSButtons(0,'L')
        self.ButtL1 = RPSButtons(1,'L')
        self.ButtL2 = RPSButtons(2,'L')
        self.ButtR0 = RPSButtons(0,'R')
        self.ButtR1 = RPSButtons(1,'R')
        self.ButtR2 = RPSButtons(2,'R')
        self.Score  = pygame.sprite.Sprite()
        self.Score.Left  = 0 
        self.Score.Right = 0 
        self.Score.Tie   = 0 
        self.all_sprites=pygame.sprite.Group()
        self.all_sprites.add(self.Player_L)
        self.all_sprites.add(self.Player_R)
        self.all_sprites.add(self.ButtL0)
        self.all_sprites.add(self.ButtL1)
        self.all_sprites.add(self.ButtL2)
        self.all_sprites.add(self.ButtR0)
        self.all_sprites.add(self.ButtR1)
        self.all_sprites.add(self.ButtR2)
        


    def RunRound(self):
        tocker = 4*self.RPSParam.CountGroup 
        while tocker>0:
            self.all_sprites.update()
            self.screen.fill(self.ColorZ.Black)
            self.all_sprites.draw(self.screen)
            if tocker<=self.RPSParam.CountGroup:
                self.msg("SHOOT",self.ColorZ.White,self.LayoutParam.FontSize,
                    self.LayoutParam.ButtonPixCount[0],
                    self.LayoutParam.ButtonPixCount[1])
            elif tocker<=2*self.RPSParam.CountGroup:
                self.msg("SISSORS",self.ColorZ.White,self.LayoutParam.FontSize,
                    self.LayoutParam.ButtonPixCount[0],
                    self.LayoutParam.ButtonPixCount[1])
            elif tocker<=3*self.RPSParam.CountGroup:
                self.msg("PAPER",self.ColorZ.White,self.LayoutParam.FontSize,
                    self.LayoutParam.ButtonPixCount[0],
                    self.LayoutParam.ButtonPixCount[1])
            else:
                self.msg("ROCK",self.ColorZ.White,self.LayoutParam.FontSize,
                    self.LayoutParam.ButtonPixCount[0],
                    self.LayoutParam.ButtonPixCount[1])
            self.DrawScore()
            pygame.display.flip()
            tocker-=1
            self.clock.tick(self.RPSParam.MaxFrameRate) 

    def ProcessResult(self):
        Result = self.Test(self.Player_L.Choice,self.Player_R.Choice)
        self.Player_L.updateState(self.Player_R.Choice,self.Player_L.Choice)
        self.Player_R.updateState(self.Player_L.Choice,self.Player_R.Choice)
        Result_sprite = pygame.sprite.Sprite()
        Result_sprite_group = pygame.sprite.Group()
        Result_sprite_group.add(Result_sprite)
        if Result ==0:
            Result_sprite.image = self.ImgWN               
            Result_sprite.rect =Result_sprite.image.get_rect()
            Result_sprite.rect.x=self.LayoutParam.WinnerImage[0]
            Result_sprite.rect.y=self.LayoutParam.WinnerImage[1]
            self.Score.Tie +=1
        elif Result == 1:
            Result_sprite.image = self.ImgWL               
            Result_sprite.rect =Result_sprite.image.get_rect()
            Result_sprite.rect.x=self.LayoutParam.WinnerImage[0]
            Result_sprite.rect.y=self.LayoutParam.WinnerImage[1]
            self.Score.Left +=1
        elif Result ==-1:
            Result_sprite.image = self.ImgWR               
            Result_sprite.rect =Result_sprite.image.get_rect()
            Result_sprite.rect.x=self.LayoutParam.WinnerImage[0]
            Result_sprite.rect.y=self.LayoutParam.WinnerImage[1]
            self.Score.Right +=1
        self.DrawScore()
        Result_sprite_group.draw(self.screen)
        pygame.display.flip()

    def DrawScore(self):
        pygame.draw.rect(self.screen,self.ColorZ.Black,self.LayoutParam.ButtonPixScore)
        self.msg("Left: %d, Right: %d, Ties: %d, Total: %d" %
                 (self.Score.Left,self.Score.Right,self.Score.Tie,
                  self.Score.Left+self.Score.Right+self.Score.Tie),
                  self.ColorZ.White,20,
                  (self.LayoutParam.ButtonPixScore[0]+self.LayoutParam.ButtonPixScore[2]/2),
                  (self.LayoutParam.ButtonPixScore[1]+self.LayoutParam.ButtonPixScore[3]/2))
        

    def RestartScreen(self):
        wait=1
        temp_box = list(self.LayoutParam.ButtonPixStart)
        temp_box_R = list(self.LayoutParam.ButtonPixRest)
        while wait:
            self.clock.tick(50) # 50 for 50 fps 
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            cur=pygame.mouse.get_pos() # check after the event cue is cleared
            click=pygame.mouse.get_pressed()
            keys=pygame.key.get_pressed()
            # Check Start hover
            if (temp_box[0]+temp_box[2]>cur[0]>temp_box[0] and
                temp_box[1]+temp_box[3]>cur[1]>temp_box[1]): 
                pygame.draw.rect(self.screen,self.ColorZ.Blue,temp_box)
                self.msg("Start",self.ColorZ.Red,self.LayoutParam.FontSize,
                    temp_box[0]+temp_box[2]/2,
                    temp_box[1]+temp_box[3]/2)
                pygame.display.flip()
                if click[0]==1:
                    wait=0
                    pgtime.wait(100)
            else: #Cursor not over the button 
                pygame.draw.rect(self.screen,self.ColorZ.Aqua,temp_box)
                self.msg("Start",self.ColorZ.Black,self.LayoutParam.FontSize,
                    temp_box[0]+temp_box[2]/2,
                    temp_box[1]+temp_box[3]/2)
                pygame.display.flip()
            # Check Reset hover
            if (temp_box_R[0]+temp_box_R[2]>cur[0]>temp_box_R[0] and
                temp_box_R[1]+temp_box_R[3]>cur[1]>temp_box_R[1]): 
                pygame.draw.rect(self.screen,self.ColorZ.Blue,temp_box_R)
                self.msg("Reset",self.ColorZ.Red,self.LayoutParam.FontSize,
                    temp_box_R[0]+temp_box_R[2]/2,
                    temp_box_R[1]+temp_box_R[3]/2)
                pygame.display.flip()
                if click[0]==1:
                    self.Score.Left = 0
                    self.Score.Right = 0
                    self.Score.Tie = 0
                    self.DrawScore()
            else: #Cursor not over the button 
                pygame.draw.rect(self.screen,self.ColorZ.Aqua,temp_box_R)
                self.msg("Reset",self.ColorZ.Black,self.LayoutParam.FontSize,
                    temp_box_R[0]+temp_box_R[2]/2,
                    temp_box_R[1]+temp_box_R[3]/2)
                pygame.display.flip()
            # Check for exit 
            if (self.LayoutParam.ButtonPixQuit[0]+self.LayoutParam.ButtonPixQuit[2]>cur[0]>self.LayoutParam.ButtonPixQuit[0] and
                self.LayoutParam.ButtonPixQuit[1]+self.LayoutParam.ButtonPixQuit[3]>cur[1]>self.LayoutParam.ButtonPixQuit[1]): 
                pygame.draw.rect(self.screen,self.ColorZ.Blue,self.LayoutParam.ButtonPixQuit)
                self.msg("Quit",self.ColorZ.Red,self.LayoutParam.FontSize,
                    self.LayoutParam.ButtonPixQuit[0]+self.LayoutParam.ButtonPixQuit[2]/2,
                    self.LayoutParam.ButtonPixQuit[1]+self.LayoutParam.ButtonPixQuit[3]/2)
                pygame.display.flip()
                if click[0]==1:
                    pygame.quit()
                    quit()
            else: #Cursor not over the exit button
                pygame.draw.rect(self.screen,self.ColorZ.Aqua,self.LayoutParam.ButtonPixQuit)
                self.msg("Quit",self.ColorZ.Black,self.LayoutParam.FontSize,
                    self.LayoutParam.ButtonPixQuit[0]+self.LayoutParam.ButtonPixQuit[2]/2,
                    self.LayoutParam.ButtonPixQuit[1]+self.LayoutParam.ButtonPixQuit[3]/2)
                pygame.display.flip()
            if keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
                wait=0
                pgtime.wait(100)
            elif keys[pygame.K_ESCAPE]:
                pygame.quit()
                quit()
            # TODO Add help menu 

    def Test(self,Play_L,Play_R):
        # returns an integer to say who won
        # 0 tie, -1 Player_R, +1 Player_L
        if ((Play_L<0) or (Play_L>2)) and ((Play_R>=0) and (Play_R<=2)):
            return -1 # player 1 had bad input, the doof
        if ((Play_R<0) or (Play_R>2)) and ((Play_L>=0) and (Play_L<=2)):
            return  1 # player 1 had bad input, the doof
        if Play_R-Play_L==0:
            return 0
        if Play_L==2 and Play_R==0: 
            return -1
        if Play_L==0 and Play_R==2: 
            return  1
        return Play_L - Play_R



class PlayerClass(pygame.sprite.Sprite): # this is the abstract class that gives the interface to making an player
    def __init__(self,LorR):
        super().__init__()
        self.LayoutParam = LayoutParam()
        self.LorR = LorR
        loadImages(self)
        self.placeImages()
        self.State = []
        self.Choice =-1 # -1 for invalid, 0 for rock, 1 for paper, 2 for sissors 
        self.Prediction = [-1.0,-1.0,-1.0] # initialize to nonsense values 
        
    def placeImages(self):
        self.image=self.ImgB
        #self.image=pygame.transform.scale(self.image,[100,100])
        #self.image.set_colorkey(White)
        self.rect =self.image.get_rect()
        self.image_R=self.ImgR
        self.rect_R =self.image_R.get_rect()
        self.image_P=self.ImgP
        self.rect_P =self.image_P.get_rect()
        self.image_S=self.ImgS
        self.rect_S =self.image_S.get_rect()

        if self.LorR == "L":
            self.ButtonPixP = self.LayoutParam.ButtonPixLP
            self.ButtonPix0 = self.LayoutParam.ButtonPixL1
            self.ButtonPix1 = self.LayoutParam.ButtonPixL2
            self.ButtonPix2 = self.LayoutParam.ButtonPixL3
            self.Key_R = pygame.K_q
            self.Key_P = pygame.K_a
            self.Key_S = pygame.K_z
        elif self.LorR == "R":
            self.ButtonPixP = self.LayoutParam.ButtonPixRP
            self.ButtonPix0 = self.LayoutParam.ButtonPixR1
            self.ButtonPix1 = self.LayoutParam.ButtonPixR2
            self.ButtonPix2 = self.LayoutParam.ButtonPixR3
            self.Key_R = pygame.K_p
            self.Key_P = pygame.K_l
            self.Key_S = pygame.K_COMMA
        else:
            raise NotImplementedError
        self.rect.x=self.ButtonPixP[0]
        self.rect.y=self.ButtonPixP[1]
        self.rect_R.x=self.ButtonPix0[0]
        self.rect_R.y=self.ButtonPix0[1]
        self.rect_P.x=self.ButtonPix1[0]
        self.rect_P.y=self.ButtonPix1[1]
        self.rect_S.x=self.ButtonPix2[0]
        self.rect_S.y=self.ButtonPix2[1]
        # TODO: Add hidden images 
    def update(self): # this is used by humans to pick and AI to make another random choice
        return []
    def updateState(self,YourChoice,OpponentChoice): # Used by AI to keep track of history
        #raise NotImplementedError
        return []
    
class Player_Human(PlayerClass):
    def __init__(self,LorR):
        super().__init__(LorR)

    def update(self):
       keys=pygame.key.get_pressed()
       cur=pygame.mouse.get_pos()
       click=pygame.mouse.get_pressed()
       for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
       if  (self.ButtonPix0[0]+self.ButtonPix0[2]>cur[0]>self.ButtonPix0[0] and
            self.ButtonPix0[1]+self.ButtonPix0[3]>cur[1]>self.ButtonPix0[1] and 
            click[0]==1): 
           self.Choice = 0 
           self.image=self.ImgR
       elif(self.ButtonPix1[0]+self.ButtonPix1[2]>cur[0]>self.ButtonPix1[0] and
            self.ButtonPix1[1]+self.ButtonPix1[3]>cur[1]>self.ButtonPix1[1] and 
            click[0]==1): 
           self.Choice = 1 
           self.image=self.ImgP
       elif(self.ButtonPix2[0]+self.ButtonPix2[2]>cur[0]>self.ButtonPix2[0] and
            self.ButtonPix2[1]+self.ButtonPix2[3]>cur[1]>self.ButtonPix2[1] and 
            click[0]==1): 
           self.Choice = 2 
           self.image=self.ImgS
       elif keys[self.Key_R]:
           self.Choice = 0 
           self.image=self.ImgR
       elif keys[self.Key_P]:
           self.Choice = 1 
           self.image=self.ImgP
       elif keys[self.Key_S]:
           self.Choice = 2 
           self.image=self.ImgS

class Player_Comp_Nash(PlayerClass):
    def __init__(self,LorR):
        super().__init__(LorR)
        self.RolWheel = [1/3,1/3,1/3]

    def update(self):
        self.MakeSelection()
        if self.Choice ==0:
            self.image=self.ImgR
        if self.Choice ==1:
            self.image=self.ImgP
        if self.Choice ==2:
            self.image=self.ImgS

    def MakeSelection(self):
        pgtime.wait(5) # two computers were correlated 
        for alice in range(0,100):
            alice 
        temp_rand = random.uniform(0,1)
        for beck in range(3):
            if temp_rand< self.RolWheel[beck]:
                self.Choice = (beck+1)%3 
                # beck is the random prediction of the players next move
                # and the modulo is to find the wining move 
                return
            temp_rand -= self.RolWheel[beck]
            # decrease and then compare to next increment 
        raise Exception('Rollet Wheel Exceeded')
    
class Player_Comp_BeatLast(PlayerClass):
    # Player plays to beat the last move
    def __init__(self,LorR):
        super().__init__(LorR)
        self.ModelParamZ = ModelParamZ() # provides ProbRandStratagy
        self.RolWheel = [1/3,1/3,1/3]
        self.State = [0] # prediction of what the player will play based on last round 
        self.Prediction = [1.0/3.0,1.0/3.0,1.0/3.0]

    def update(self):
        self.MakeSelection()
        if self.Choice ==0:
            self.image=self.ImgR
        if self.Choice ==1:
            self.image=self.ImgP
        if self.Choice ==2:
            self.image=self.ImgS

    def updateState(self,OponentPlay, MyPlay):
        self.State[0] = (MyPlay+1)%3 
        # Rock+1 = Paper, Paper+1 = Sissor, Sissor+1=3, 3 modulo 3=0=Rock
        #self.State[0] = (OponentPlay+2)%3 
        ## Rock+2 = Paper, Paper+1 = Sissor, Sissor+1=3, 3 modulo 3=0=Rock
        self.RolWheel = [self.ModelParamZ.ProbRandStratagy/2.0,
                         self.ModelParamZ.ProbRandStratagy/2.0,
                         self.ModelParamZ.ProbRandStratagy/2.0]
        # initialize all predictions to baseline, then change the predicted one
        # note that this is the prediction that should be made to win
        self.RolWheel[self.State[0]] = 1.0-self.ModelParamZ.ProbRandStratagy

    def MakeSelection(self):
        pgtime.wait(5) # two computers were correlated 
        for alice in range(0,100):
            alice 
        temp_rand = random.uniform(0,1)
        for beck in range(3):
            if temp_rand< self.RolWheel[beck]:
                self.Choice = (beck+1)%3 
                # beck is the random prediction of the players next move
                # and the modulo is to find the wining move 
                return
            temp_rand -= self.RolWheel[beck]
            # decrease and then compare to next increment 
        raise Exception('Rollet Wheel Exceeded')
    
a = RPSGame()
#quit()
