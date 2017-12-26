#basicPaint.py

from pygame import *
from random import*
from tkinter import*
from math import*

root=Tk()
root.withdraw() ## removes the extra TK window

init()
font.init()

size=(1080,720)
screen = display.set_mode(size)

## Fonts

comicFont = font.SysFont("Times New Roman",26)
displayText = comicFont.render("Backgrounds",True,(0,0,0))
rotPic = displayText

## other variables

eradius = 10
radius = 10
t = 5
lthick = 5
elthick = 5
page = 0
stamp = "no stamp"
background = "nothing"
size = 10

## Colours

RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
WHITE=(255,255,255)
BLACK=(0,0,0)
YELLOW = (226, 244, 66)
LIGHTBLUE = (0, 255, 250)
PINK = (255, 0, 246)
PURPLE = (165, 0, 255)
MEGENTA = (255, 0, 144)
AQUA_BLUE = (2, 255, 191)
GREEN_YELLOW = (131, 255, 0)

## time 

myTime = time.Clock()

## Music

dbz_M = mixer.Sound("music/Dragonballsuper.wav")
mixer.music.load("music/Dragonballsuper.wav")
mixer.Sound.play(dbz_M)
mixer.music.play(-1)

## load all regular

dragonball = image.load("images/Dragonballback.png") ## back ground (put images/"name") this indicates it's in images folder
wheelPic = image.load("images/colwheel.jpg")
eraserPic = image.load("images/eraser.png")
pencilPic = image.load("images/pencil.png")
stampPic = image.load("images/stamp tool.png")
circlePic = image.load("images/circle tool.png")
rectanglePic = image.load("images/rectangle tool.png")
sprayPic = image.load("images/spraypaint.png")
upArrowPic = image.load("images/up arrow.png")
downArrowPic = image.load("images/down arrow.png")
cursorPic = image.load("images/cursor_image.png")
colourPic = image.load("images/colour_picker tool.png")
textPic = image.load("images/textbox.png")
paintbrushPic = image.load("images/paintbrush.png")
markerPic = image.load("images/marker_tool.png")
loadIcon = image.load("images/icons/load.png")
saveIcon = image.load("images/icons/save.jpg")
backIcon = image.load("images/icons/back_button.png")
paint_brushPic = image.load("images/paintbrush.png")
markerPic = image.load("images/marker_tool.png")

#########################################################

## load all stamps

gokuPic = image.load("images/Choice 1/goku_ssgss.png")
goku_ultraPic = image.load("images/Choice 1/goku ultra instinct.png")
gohanPic = image.load("images/Choice 1/gohan.png")
beerusPic = image.load("images/Choice 1/beerus.png")
goku_ssgPic = image.load("images/Choice 1/goku ssg.png")
jerinPic = image.load("images/Choice 1/Jiren.png")
keflaPic = image.load("images/Choice 1/Kefla.png")
vegetabPic = image.load("images/Choice 1/vegeta blue.png")
black_zamasu = image.load("images/Choice 1/black x zamsu.png")
goku_blackPic = image.load("images/Choice 1/Goku_Black.png")
golden_frezaPic = image.load("images/Choice 1/golden freza.png")
goku_rose = image.load("images/Choice 1/Goku_Black rose.png")

#######################################################

## load all stamp icons 

gokuIcon = image.load("images/icons/goku icon.png")
gohanIcon = image.load("images/icons/gohanicon.png")
goku_ssgIcon = image.load("images/icons/goku ssg.png")
beerusIcon = image.load("images/icons/beerus.jpg")
goku_ultraIcon = image.load("images/icons/goku ultra.png")
jerinIcon = image.load("images/icons/jerin.png")
keflaIcon = image.load("images/icons/kefla.png")
vegetaIcon = image.load("images/icons/vegeta.png")
blackzamausIcon = image.load("images/icons/merged icon.png")
gokuroseIcon = image.load("images/icons/roseicon.png")
golden_frezaIcon = image.load("images/icons/golden freza.png")
goku_black = image.load("images/icons/goku black.png")

## Load all background text

back01 = image.load("images/back/page02.png")
back02 = image.load("images/back/page03.png")
back03 = image.load("images/back/page04.png")
back04 = image.load("images/back/page05.png")
back05 = image.load("images/back/page06.png")
back06 = image.load("images/back/page07.png")
back07 = image.load("images/back/page08.png")
back08 = image.load("images/back/page09.png")
back09 = image.load("images/back/page10.png")

#############################################################

## load all background images

b1 = image.load("images/Background/beerus_planet.jpg")
b2 = image.load("images/Background/boat_place.jpg")
b3 = image.load("images/Background/Kame_house.png")
b4 = image.load("images/Background/king_kai.jpg")
b5 = image.load("images/Background/nameless planet_stage.png")
b6 = image.load("images/Background/nameless_planet.png")
b7 = image.load("images/Background/stage tournment of power.png")
b8 = image.load("images/Background/super_dragon.png")
b9 = image.load("images/Background/tower.jpg")

## transform all background images

b1T = transform.scale(b1,(680,450))
b2T = transform.scale(b2,(680,450))
b3T = transform.scale(b3,(680,450))
b4T = transform.scale(b4,(680,450))
b5T = transform.scale(b5,(680,450))
b6T = transform.scale(b6,(680,450))
b7T = transform.scale(b7,(680,450))
b8T = transform.scale(b8,(680,450))
b9T = transform.scale(b9,(680,450))

## default colour 

col=BLACK #default colour is black

bcol = WHITE ## default colour for background

## default tool

tool = "cursor" ## default tool is cursor for selecting 

display.set_caption("Dragon ball super Paint") ## for displaying dragon ball super paint in top left hand corner

###############################################

## identifying all rects for tools 

dragonrect = Rect(0,0,1080,720) ## this if for the background
canvasB = Rect(204,120,684,454) ## this is the rectangular black border for the canvas
canvasRect = Rect(206,122,680,450) ## this is the canvas
pencilRect = Rect(210,605,40,40) ## pencil rectagle 
eraserRect = Rect(210,650,40,40) ## eraser rectangle 
wheelRect = Rect(683,600,200,100) ## colour wheel rectangle 
platB = Rect(204,598,684,104) ## platform border
platRect = Rect(206,600,680,100) ## platform where all the tools will be
screRect = Rect(10,122,185,450) ## screen where more options will be displayed
screB_Rect = Rect(8,120,189,454)
circleRect = Rect(260,605,40,40)
stampRect = Rect(260,650,40,40)
rectangleRect = Rect(310,605,40,40)
lineRect = Rect(310,650,40,40)
ellipseRect = Rect(360,650,40,40)
sprayRect = Rect(360,605,40,40)
backRect = Rect(410,605,40,40)
cursorRect = Rect(410,650,40,40)
colourRect = Rect(460,605,40,40)
textRect = Rect(460,650,40,40)
paintRect = Rect(510,605,40,40)
markerRect = Rect(510,650,40,40)
loadRect = Rect(25,135,40,40)
saveRect = Rect(100,135,40,40)
show_colourrect = Rect(593,607,80,40)

#################################

## identifying all rects for backgrounds

back01Rect = Rect(20,170,165,30)
back02Rect = Rect(20,210,165,30)
back03Rect = Rect(20,250,165,30)
back04Rect = Rect(20,290,165,30)
back05Rect = Rect(20,330,165,30)
back06Rect = Rect(20,370,165,30)
back07Rect = Rect(20,410,165,30)
back08Rect = Rect(20,450,165,30)
back09Rect = Rect(20,490,165,30)

##############################################

## transforming all background texts

back01T = transform.scale(back01,(165,30))
back02T = transform.scale(back02,(165,20))
back03T = transform.scale(back03,(165,20))
back04T = transform.scale(back04,(165,20))
back05T = transform.scale(back05,(165,20))
back06T = transform.scale(back06,(165,20))
back07T = transform.scale(back07,(165,25))
back08T = transform.scale(back08,(165,30))
back09T = transform.scale(back09,(165,25))

###########################################

## transforming - scaling images

dragonT=transform.scale(dragonball,(1080,720)) ## scaling the background
wheelT=transform.scale(wheelPic,(202,99))
pencilT=transform.scale(pencilPic,(40,40))
eraserT=transform.scale(eraserPic,(40,40))
circleT = transform.scale(circlePic,(35,35))
stampT = transform.scale(stampPic,(40,40))
sprayT = transform.scale(sprayPic,(40,40))
cursorT = transform.scale(cursorPic,(40,40))
colourT = transform.scale(colourPic,(40,40))
loadT = transform.scale(loadIcon,(40,40))
saveT = transform.scale(saveIcon,(40,40))
backT = transform.scale(backIcon,(40,40))
textT = transform.scale(textPic,(40,40))
paintT = transform.scale(paint_brushPic,(40,40))
markerT = transform.scale(markerPic,(40,40))

########################################## Transforming the stamp pics only 

### page 0

gokuT = transform.scale(gokuPic,(217,228))
goku_ssgT = transform.scale(goku_ssgPic,(128,211))
goku_ultraT = transform.scale(goku_ultraPic,(192,135))

### page 1 

jerinT = transform.scale(jerinPic,(144,240))
gohanT = transform.scale(gohanPic,(117,170))
beerusT = transform.scale(beerusPic,(128,218))

### page 2 

keflaT = transform.scale(keflaPic,(116,155))
vegetaT = transform.scale(vegetabPic,(132,203))
black_zamT = transform.scale(black_zamasu,(125,252))

### page 3

goku_roseT = transform.scale(goku_rose,(128,235))
goku_blackT = transform.scale(goku_blackPic,(118,187))
golden_frezaT = transform.scale(golden_frezaPic,(119,160))

############################################

## Blitting all tools and canvas

screen.blit(dragonT,dragonrect) ## adding the background 
draw.rect(screen,BLACK,canvasB)
draw.rect(screen,WHITE,canvasRect)
draw.rect(screen,BLACK,platB)
draw.rect(screen,WHITE,platRect)
draw.rect(screen,BLACK,screB_Rect)
draw.rect(screen,WHITE,screRect)
screen.blit(wheelT,wheelRect)
screen.blit(pencilT,pencilRect)
screen.blit(eraserT,eraserRect)
screen.blit(stampT,stampRect)
screen.blit(circleT,Rect(262,607,35,35))
draw.rect(screen,BLACK,Rect(315,615,30,20),1)
draw.line(screen,BLACK,(315,655),(345,685),1)
draw.ellipse(screen,BLACK,[365,660,32,20],1)
screen.blit(sprayT,sprayRect)
screen.blit(backT,backRect)
screen.blit(cursorT,cursorRect)
screen.blit(colourT,colourRect)
screen.blit(textT,textRect)
screen.blit(paintT,paintRect)
screen.blit(markerT,markerRect)
draw.rect(screen,BLACK,Rect(591,605,84,44),0)

###############################

## identifying all the rects for stamps only

### page 0

gokuRect = Rect(50,155,100,100)
goku_ultraRect = Rect(50,295,100,100)
goku_ssgRect = Rect(50,420,100,100)

### page 1

jerinRect = Rect(50,155,100,100)
gohanRect = Rect(50,295,100,100)
beerusRect = Rect(50,420,100,100)

### page 2

kelfaRect = Rect(50,155,100,100)
vegetaRect = Rect(50,295,100,100)
black_zamusRect = Rect(50,420,100,100)

### page 3

goku_roseRect = Rect(50,155,100,100)
goldenfrezaRect = Rect(50,295,100,100)
goku_blackRect = Rect(50,420,100,100)

## up down arrows

upArrowRect = Rect(15,125,170,25)
downArrowRect = Rect(15,540,170,25)

##############################################

running = True

## omx and omy is basically just mx and my but you need to put omx and omy

omx=300 
omy=300

while running:
    click = False ## for 1 step programs

    draw.rect(screen,col,show_colourrect,0)
  
    ## Random colours
    rred = randint(0,255)
    rgreen = randint(0,255)
    rblue = randint(0,255)
        
    for evt in event.get():
        
        if evt.type == QUIT:            
            running = False
            
        if evt.type==KEYDOWN:            
            if evt.key==K_LCTRL:
                draw.rect(screen,WHITE,canvasRect)
                
            elif evt.key==K_RIGHT and tool == "eraser":
                eradius+=5

            elif evt.key==K_LEFT and tool == "eraser":
                eradius-=5

        if evt.type == MOUSEBUTTONDOWN:
            click = True
            sx,sy = evt.pos

            if evt.button == 5: # scrolling down

                if tool =="circle":
                    radius -=1

                    if radius <2:
                        radius =2

                elif tool == "rectangle":
                    t -=1

                    if t <0:
                        t = 0

                elif tool == "eraser":
                    eradius -=1

                    if eradius <0:
                        eradius =0

                elif tool == "ellipse":
                    elthick -=1

                    if elthick <0:
                        elthick =1

                elif tool == "line":
                    lthick -=1

                    if lthick <0:
                        lthick =1

            if evt.button == 4:

                if tool == "circle":
                    radius +=1

                elif tool == "rectangle":
                    t +=1

                elif tool == "eraser":
                    eradius +=1

                elif tool == "line":
                    lthick +=1

                elif tool == "ellipse":
                    elthick +=1

            background = screen.copy()

    mx,my=mouse.get_pos()

    print(mx,my)## to calculate the x and y of anthing if needed (helpful)

    mb=mouse.get_pressed() ## shorter version of the mouse button check

    #################################### selecting the tools

    ################### rectangle for tools

    draw.rect(screen,GREEN,pencilRect,2)
    draw.rect(screen,GREEN,eraserRect,2)
    draw.rect(screen,GREEN,stampRect,2)
    draw.rect(screen,GREEN,circleRect,2)
    draw.rect(screen,GREEN,rectangleRect,2)
    draw.rect(screen,GREEN,lineRect,2)
    draw.rect(screen,GREEN,ellipseRect,2)
    draw.rect(screen,GREEN,sprayRect,2)
    draw.rect(screen,GREEN,cursorRect,2)
    draw.rect(screen,GREEN,backRect,2)
    draw.rect(screen,GREEN,colourRect,2)
    draw.rect(screen,GREEN,textRect,2)
    draw.rect(screen,GREEN,paintRect,2)
    draw.rect(screen,GREEN,markerRect,2)

    #################################### all extra tools for choice 1 

    if tool == "cursor" and page ==0:

        draw.rect(screen,AQUA_BLUE,screB_Rect)
        draw.rect(screen,WHITE,screRect)
        screen.blit(loadT,loadRect)
        screen.blit(saveT,saveRect)

    elif tool == "background" and page == 0:
        draw.rect(screen,BLACK,screB_Rect)
        draw.rect(screen,WHITE,screRect)

        screen.blit(rotPic,(20,130))

        screen.blit(back01T,back01Rect)
        screen.blit(back02T,back02Rect)
        screen.blit(back03T,back03Rect)
        screen.blit(back04T,back04Rect)
        screen.blit(back05T,back05Rect)
        screen.blit(back06T,back06Rect)
        screen.blit(back07T,back07Rect)
        screen.blit(back08T,back08Rect)
        screen.blit(back09T,back09Rect)

        draw.rect(screen,BLACK,back01Rect,2)
        draw.rect(screen,BLACK,back02Rect,2)
        draw.rect(screen,BLACK,back03Rect,2)
        draw.rect(screen,BLACK,back04Rect,2)
        draw.rect(screen,BLACK,back05Rect,2)
        draw.rect(screen,BLACK,back06Rect,2)
        draw.rect(screen,BLACK,back07Rect,2)
        draw.rect(screen,BLACK,back08Rect,2)
        draw.rect(screen,BLACK,back09Rect,2)

    elif tool == "pencil":
        draw.rect(screen,BLUE,screB_Rect)
        draw.rect(screen,WHITE,screRect)
        ##draw.rect(screen,GREEN,

    elif tool == "eraser":

        draw.rect(screen,GREEN,screB_Rect)
        draw.rect(screen,WHITE,screRect)

    elif tool == "stamp" and page ==0:

        draw.rect(screen,RED,screB_Rect)
        draw.rect(screen,WHITE,screRect)
        screen.blit(gokuIcon,gokuRect)
        draw.rect(screen,BLACK,gokuRect,2)
        screen.blit(goku_ultraIcon,goku_ultraRect)
        draw.rect(screen,BLACK,goku_ultraRect,2)
        screen.blit(goku_ssgIcon,goku_ssgRect)
        draw.rect(screen,BLACK,goku_ssgRect,2)     
        screen.blit(downArrowPic,downArrowRect)

    elif tool == "stamp" and page==1:

        draw.rect(screen,RED,screB_Rect)
        draw.rect(screen,WHITE,screRect)
        screen.blit(jerinIcon,jerinRect)
        draw.rect(screen,BLACK,jerinRect,2)   
        screen.blit(gohanIcon,gohanRect)
        draw.rect(screen,BLACK,gohanRect,2)
        screen.blit(beerusIcon,beerusRect)
        draw.rect(screen,BLACK,beerusRect,2)       

        screen.blit(upArrowPic,upArrowRect)
        screen.blit(downArrowPic,downArrowRect)

    elif tool == "stamp" and page== 2:

        draw.rect(screen,RED,screB_Rect)
        draw.rect(screen,WHITE,screRect)

        screen.blit(keflaIcon,kelfaRect)
        draw.rect(screen,BLACK,kelfaRect,2)

        screen.blit(vegetaIcon,vegetaRect)
        draw.rect(screen,BLACK,vegetaRect,2)

        screen.blit(blackzamausIcon,black_zamusRect)
        draw.rect(screen,BLACK,black_zamusRect,2)
        
        screen.blit(upArrowPic,upArrowRect)
        screen.blit(downArrowPic,downArrowRect)

    elif tool == "stamp" and page==3:

        draw.rect(screen,RED,screB_Rect)
        draw.rect(screen,WHITE,screRect)
        
        screen.blit(gokuroseIcon,goku_roseRect)
        draw.rect(screen,BLACK,goku_roseRect,2)
        
        screen.blit(golden_frezaIcon,goldenfrezaRect)
        draw.rect(screen,BLACK,goldenfrezaRect,2)
        
        screen.blit(goku_black,goku_blackRect)
        draw.rect(screen,BLACK,goku_blackRect,2)
        
        screen.blit(upArrowPic,upArrowRect)

    elif tool == "circle":

        draw.rect(screen,YELLOW,screB_Rect)
        draw.rect(screen,WHITE,screRect)

    elif tool == "rectangle":

        draw.rect(screen,PURPLE,screB_Rect)
        draw.rect(screen,WHITE,screRect)

    elif tool == "line":

        draw.rect(screen,MEGENTA,screB_Rect)
        draw.rect(screen,WHITE,screRect)

    elif tool == "spraypaint":

        draw.rect(screen,LIGHTBLUE,screB_Rect)
        draw.rect(screen,WHITE,screRect)

    elif tool == "ellipse":

        draw.rect(screen,GREEN_YELLOW,screB_Rect)
        draw.rect(screen,WHITE,screRect)

    elif tool == "colour_picker":

        draw.rect(screen,RC,screB_Rect)
        draw.rect(screen,WHITE,screRect)

    elif tool == "text":

        draw.rect(screen,RC,screB_Rect)
        draw.rect(screen,WHITE,screRect)

    elif tool == "paint":

        draw.rect(screen,RC,screB_Rect)
        draw.rect(screen,WHITE,screRect)

    elif tool == "marker":

        draw.rect(screen,RC,screB_Rect)
        draw.rect(screen,WHITE,screRect)

    ##################### changing the color

    if tool == "cursor":
        draw.rect(screen,RED,cursorRect,2)
    
    elif tool == "pencil":
        draw.rect(screen,RED,pencilRect,2)

    elif tool == "eraser":
        draw.rect(screen,RED,eraserRect,2)

    elif tool == "stamp":
        draw.rect(screen,RED,stampRect,2)

    elif tool == "circle":
        draw.rect(screen,RED,circleRect,2)

    elif tool == "rectangle":
        draw.rect(screen,RED,rectangleRect,2)

    elif tool == "line":
        draw.rect(screen,RED,lineRect,2)

    elif tool == "ellipse":
        draw.rect(screen,RED,ellipseRect,2)

    elif tool == "spraypaint":
        draw.rect(screen,RED,sprayRect,2)

    elif tool == "background":
        draw.rect(screen,RED,backRect,2)

    elif tool == "colour_picker":
        draw.rect(screen,RED,colourRect,2)

    elif tool == "text":
        draw.rect(screen,RED,textRect,2)

    elif tool == "paint":
        draw.rect(screen,RED,paintRect,2)

    elif tool == "marker":
        draw.rect(screen,RED,markerRect,2)
        
##################################################

    if page == 0:

        if stamp == "gokub" and tool == "stamp":
            draw.rect(screen,RED,gokuRect,2)

        if stamp == "goku_u" and tool == "stamp":
            draw.rect(screen,RED,goku_ultraRect,2)

        if stamp == "goku_ssg" and tool == "stamp":
            draw.rect(screen,RED,goku_ssgRect,2)


        if background == "tourn_of_power" and tool == "background":
            draw.rect(screen,RED,back01Rect,2)

        if background == "kame_house" and tool == "background":
            draw.rect(screen,RED,back02Rect,2)

        if background == "beerus_planet" and tool == "background":
            draw.rect(screen,RED,back03Rect,2)

        if background == "bulma_boat" and tool == "background":
            draw.rect(screen,RED,back04Rect,2)

        if background == "king_kai" and tool == "background":
            draw.rect(screen,RED,back05Rect,2)

        if background == "kami_look" and tool == "background":
            draw.rect(screen,RED,back06Rect,2)

        if background == "nameless_p" and tool == "background":
            draw.rect(screen,RED,back07Rect,2)

        if background == "nameless_p_s" and tool == "background":
            draw.rect(screen,RED,back08Rect,2)

        if background == "super_shenron" and tool == "background":
            draw.rect(screen,RED,back09Rect,2)

    if page ==1:

        if stamp == "jerin" and tool == "stamp":
             draw.rect(screen,RED,jerinRect,2)

        if stamp == "gohan" and tool == "stamp":
             draw.rect(screen,RED,gohanRect,2)

        if stamp == "beerus" and tool == "stamp":
             draw.rect(screen,RED,beerusRect,2)

    if page ==2:

        if stamp == "kelfa" and tool == "stamp":
             draw.rect(screen,RED,keflaRect,2)

        if stamp == "vegeta" and tool == "stamp":
             draw.rect(screen,RED,vegetaRect,2)

        if stamp == "black_zamaus" and tool == "stamp":
             draw.rect(screen,RED,black_zamusRect,2)

    if page ==3:

        if stamp == "goku_rose" and tool == "stamp":
             draw.rect(screen,RED,goku_roseRect,2)

        if stamp == "goldenFreza" and tool == "stamp":
             draw.rect(screen,RED,goldenfrezaRect,2)

        if stamp == "goku_black" and tool == "stamp":
             draw.rect(screen,RED,goku_blackRect,2)
    

    if mb[0]==1: ## Checking left click

        if pencilRect.collidepoint(mx,my): ## check if the pencil rectangle is clicked (Note: the rectangle is there but you cant see it you can only see the picture 
            tool="pencil" ## set tool to pencil

        elif eraserRect.collidepoint(mx,my): ## same as pencil
            tool="eraser" ## set tool to eraser

        elif stampRect.collidepoint(mx,my):
            tool = "stamp"
            page = 0
            stamp = "nothing"

        elif circleRect.collidepoint(mx,my):
            tool = "circle"

        elif rectangleRect.collidepoint(mx,my):
            tool = "rectangle"

        elif lineRect.collidepoint(mx,my):
            tool = "line"

        elif ellipseRect.collidepoint(mx,my):
            tool = "ellipse"
            
        elif sprayRect.collidepoint(mx,my):
            tool = "spraypaint"

        elif cursorRect.collidepoint(mx,my):
            tool = "cursor"

        elif backRect.collidepoint(mx,my):
            tool = "background"
            page = 0

        elif colourRect.collidepoint(mx,my):
            tool = "colour_picker"
            RC = (rred,rgreen,rblue)

        elif textRect.collidepoint(mx,my):
            tool = "text"
            RC = (rred,rgreen,rblue)

        elif paintRect.collidepoint(mx,my):
            tool = "paint"
            RC = (rred,rgreen,rblue)

        elif markerRect.collidepoint(mx,my):
            tool = "marker"
            RC = (rred,rgreen,rblue)

    ##using the tools

    if mb[0]==1: ## if left click

        if canvasRect.collidepoint(mx,my): ## make sure all the lines stay within the canvas
            screen.set_clip(canvasRect) ## only the canvas can be updated

            if tool=="pencil": ## if the tool selected is a pencil
                draw.line(screen,col,(omx,omy),(mx,my),3) ## draw lines with a thick ness of 3

            elif tool=="eraser": ## if tool is eraser
                draw.circle(screen,WHITE,(mx,my),eradius) ## draw a circle that is white

            elif tool == "circle":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                draw.circle(screen,col,(sx,sy),radius,2)

            elif tool == "rectangle":            
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                draw.rect(screen,col,Rect(sx,sy,mx-sx,my-sy),t)

            elif tool == "ellipse":             
                screen.fill((0,0,0))
                screen.blit(background,(0,0))

                try:
                    ellRect = Rect(sx,sy,mx-sx,my-sy)
                    ellRect.normalize()               
                    draw.ellipse(screen,col,ellRect,elthick)

                except:
                    pass

            elif tool == "line":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                draw.line(screen,col,(sx,sy),(mx,my),lthick)

            elif tool == "colour_picker":

                if canvasRect.collidepoint(mx,my): ## check if mouse colides with any point on the colour rectangle 
                    col=screen.get_at((mx,my)) ## where ever the mouse collided take the pixel for that (in r g b form)
                    print(col) ## print default colour

            elif tool == "spraypaint":

                screen.set_clip(canvasRect)
                if canvasRect.collidepoint(mx,my):
                    radius=size
                    for i in range (30):
                        dx = randint(-radius,radius)
                        dy = randint(-radius,radius)
                        if hypot(dx,dy) <=radius:
                            draw.circle(screen,col,(mx+dx,my+dy),0)

            elif tool == "paint":

                if canvasRect.collidepoint(mx,my):
                    ax,ay = omx-mx,omy-my
                    dist = max(abs(ax),abs(ay))
                    for l in range (dist):
                        x = int(mx+l/dist*ax)
                        y = int(my+l/dist*ay)
                        draw.circle(screen,col,(x,y),size)

            elif tool == "marker":
                if canvasRect.collidepoint(mx,my):
                    fx,fy = sx-mx,sy-my
                    dist = max(abs(fx),abs(fy))
                    cover = Surface((680,450),SRCALPHA)
                    size = 10
                    for j in range (dist):
                        x = int(mx+j/dist*fx)
                        y = int(mx+j/dist*fy)
                        draw.circle(cover,(col[0],col[1],col[2],2),(size//2,size//2),size//2)
                        screen.blit(cover,(x+size//2,y+size//2))


############################################################ using tool for tools 1

        if page ==0:

            if gokuRect.collidepoint(mx,my) and tool == "stamp":
                    stamp = "gokub"

            if stamp == "gokub" and canvasRect.collidepoint(mx,my) and tool == "stamp":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                screen.blit(gokuT,(mx-59,my-79))

            elif goku_ultraRect.collidepoint(mx,my) and tool == "stamp":
                    stamp = "goku_u"

            if stamp == "goku_u" and canvasRect.collidepoint(mx,my) and tool == "stamp":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                screen.blit(goku_ultraT,(mx-64,my-25))

            elif goku_ssgRect.collidepoint(mx,my) and tool == "stamp":
                    stamp = "goku_ssg"

            if stamp == "goku_ssg" and canvasRect.collidepoint(mx,my) and tool == "stamp":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                screen.blit(goku_ssgT,(mx-64,my-105))

        if page == 1:

            if jerinRect.collidepoint(mx,my) and tool == "stamp":
                    stamp = "jerin"

            if stamp == "jerin" and canvasRect.collidepoint(mx,my) and tool == "stamp":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                screen.blit(jerinT,(mx-72,my-120))
               
            if gohanRect.collidepoint(mx,my) and tool == "stamp":
                    stamp = "gohan"

            if stamp == "gohan" and canvasRect.collidepoint(mx,my) and tool == "stamp":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                screen.blit(gohanT,(mx-50,my-60))

            if beerusRect.collidepoint(mx,my) and tool == "stamp":
                    stamp = "beerus"

            if stamp == "beerus" and canvasRect.collidepoint(mx,my) and tool == "stamp":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                screen.blit(beerusT,(mx-64,my-109))

        if page == 2:

            if kelfaRect.collidepoint(mx,my) and tool == "stamp":
                    stamp = "kefla"

            if stamp == "kefla" and canvasRect.collidepoint(mx,my) and tool == "stamp":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                screen.blit(keflaT,(mx-58,my-77))
                
            if vegetaRect.collidepoint(mx,my) and tool == "stamp":
                    stamp = "vegeta"

            if stamp == "vegeta" and canvasRect.collidepoint(mx,my) and tool == "stamp":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                screen.blit(vegetaT,(mx-66,my-101))

            if black_zamusRect.collidepoint(mx,my) and tool == "stamp":
                    stamp = "black_zamaus"

            if stamp == "black_zamaus" and canvasRect.collidepoint(mx,my) and tool == "stamp":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                screen.blit(black_zamT,(mx-62,my-126))
                
        if page == 3:

            if goku_roseRect.collidepoint(mx,my) and tool == "stamp":
                    stamp = "goku_rose"

            if stamp == "goku_rose" and canvasRect.collidepoint(mx,my) and tool == "stamp":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                screen.blit(goku_roseT,(mx-64,my-117))
                
            if goku_blackRect.collidepoint(mx,my) and tool == "stamp":
                    stamp = "goku_black"

            if stamp == "goku_black" and canvasRect.collidepoint(mx,my) and tool == "stamp":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                screen.blit(goku_blackT,(mx-75,my-93))

            if goldenfrezaRect.collidepoint(mx,my) and tool == "stamp":
                    stamp = "goldenFreza"

            if stamp == "goldenFreza" and canvasRect.collidepoint(mx,my) and tool == "stamp":
                screen.fill((0,0,0))
                screen.blit(background,(0,0))
                screen.blit(golden_frezaT,(mx-59,my-80))

##################################################################

        if page ==0:

            if back01Rect.collidepoint(mx,my) and tool == "background":
                background = "tourn_of_power"
                screen.blit(b7T,canvasRect)

            if back02Rect.collidepoint(mx,my) and tool == "background":
                background = "kame_house"
                screen.blit(b3T,canvasRect)

            if back03Rect.collidepoint(mx,my) and tool == "background":
                background = "beerus_planet"
                screen.blit(b1T,canvasRect)

            if back04Rect.collidepoint(mx,my) and tool == "background":
                background = "bulma_boat"
                screen.blit(b2T,canvasRect)

            if back05Rect.collidepoint(mx,my) and tool == "background":
                background = "king_kai"
                screen.blit(b4T,canvasRect)

            if back06Rect.collidepoint(mx,my) and tool == "background":
                background = "kami_look"
                screen.blit(b9T,canvasRect)

            if back07Rect.collidepoint(mx,my) and tool == "background":
                background = "nameless_p"
                screen.blit(b6T,canvasRect)

            if back08Rect.collidepoint(mx,my) and tool == "background":
                background = "nameless_p_s"
                screen.blit(b5T,canvasRect)

            if back09Rect.collidepoint(mx,my) and tool == "background":
                background = "super_shenron"
                screen.blit(b8T,canvasRect)

    if click:

            if downArrowRect.collidepoint(mx,my) and page >=0 and page <3:
                page+=1

            elif page!=0 and upArrowRect.collidepoint(mx,my) and page >0 and page <=3:
                page -=1
                
            screen.set_clip(None) # modify everything

            ## SAVING THE PROGRAM

            if saveRect.collidepoint(mx,my) and tool == "cursor" and page ==0:
                try:
                    fname = filedialog.asksaveasfilename(defaultextension = ".png")
                    ## asks the user to enter the file name they would like to save as
                    if fname !="":
                        image.save(screen.subsurface(canvasRect),fname)

                except:
                    pass ## prevent from program crashing

            ## OPENING A PROGRAM 

            if loadRect.collidepoint(mx,my) and tool == "cursor" and page ==0:
                try:
                    fname = filedialog.askopenfilename(filetypes = [("images","*.png;*.jpg;*.jpeg")])              
                    screen.set_clip(canvasRect)
                    myPic = image.load(fname)
                    myPic1 = transform.scale(myPic,(680,450))
                    screen.blit(myPic1,canvasRect)
                    screen.set_clip(None)

                except:
                    print("loading error")
                    pass

#####Changing the colour

    if mb[0]==1: ## check if left click

        if wheelRect.collidepoint(mx,my): ## check if mouse colides with any point on the colour rectangle 
            col=screen.get_at((mx,my)) ## where ever the mouse collided take the pixel for that (in r g b form)
            print(col) ## print default colour
           
    omx=mx ## setting omx to mx                          
    omy=my ## setting omy to my
    
    display.flip()
    
quit() # closes out pygame window

