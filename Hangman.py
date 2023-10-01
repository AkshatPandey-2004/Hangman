import pygame
import os
import maths
#Setup Display
pygame.init()
WIDTH, HEIGHT=800, 500
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman Game")


#BUTTONS VARIABLE
RADIUS=20
GAP=15
letters=[]
startx=round((WIDTH-(RADIUS*2+ GAP)*13)/2)
starty=400
A=65
for i in range(26):
    x=startx +GAP * 2 + ((RADIUS*2+GAP) * (i%13)) 
    y=starty+ ((i//13)) * (GAP + RADIUS * 2)
    letters.append([x,y,chr(A+i),True])

#Fonts
LETTER_FONT=pygame.font.SysFont('comicsans',20)
WORD_FONT=pygame.font.SysFont('comicsans',40)


#load images
images=[]
for i in range(7):
    image=pygame.image.load("C:/Users/aksha/OneDrive/Desktop/CODER/Devops_Lab/Hangman/hangman"+str(i)+".png")
    images.append(image)


#colour
WHITE=(255,255,255)
BLACK=(0,0,0)

#game variable
hangman_status=0
word="DEVELOPER"
guessed=[]

#Setup Game
FPS=60
clock=pygame.time.Clock()
run=True

def draw():
    win.fill(WHITE)
    
    #DRAW WORDS
    display_word=""
    for letter in word:
        if letter  in guessed:
            display_word+=letter + " "
        else:
            display_word+="_ "
    text=WORD_FONT.render(display_word,1,BLACK)
    win.blit(text,(400,200))
    
    #DRAW BUTTONS
    for letter in letters:
        x, y, ltr, visible=letter
        if visible:
            pygame.draw.circle(win,BLACK,(x,y),RADIUS,3)
            text=LETTER_FONT.render(ltr,1,BLACK)
            win.blit(text,(x-text.get_width()/2,y-text.get_height()/2))

    win.blit(images[hangman_status],(150,100))
    pygame.display.update()

def main(points):
    #load images
    images=[]
    for i in range(7):
        image=pygame.image.load("C:/Users/aksha/OneDrive/Desktop/CODER/Devops_Lab/Hangman/hangman"+str(i)+".png")
        images.append(image)
        images_rect=image.get_rect()
    #game variable
    hangman_status=0
    word="DEVELOPER"
    guessed=[]

    #Setup Game
    FPS=60
    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                m_x, m_y=pygame.mouse.get_pos()
                for letter in letters:
                    x,y,ltr,visible=letter
                    if visible:
                        dis=math.sqrt((x-m_x)**2 + (y-m_y)**2)
                        if dis < RADIUS:
                            letter[3]=False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status+=1
        draw(word,guessed,hangman_status,images)
        won=True
        for letter in word:
            if letter not in guessed:
                won=False
                break

        if won:
            pygame.time.delay(1000)
            win.fill(WHITE)
            text=WORD_FONT.render("You Won!!",1,BLACK)
            win.blit(text,(WIDTH/2-text.get_width()/2,HEIGHT/2-text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(3000)
            break


        if hangman_status==6:
            pygame.time.delay(1000)
            win.fill(WHITE)
            text=WORD_FONT.render("You Lost!!",1,BLACK)
            win.blit(text,(WIDTH/2-text.get_width()/2,HEIGHT/2-text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(3000)
            break

#Button Variabel
#Below is the menu screen
while True:
    win.fill(WHITE)
    text=TITLE_FONT.render("HANGMAN_GAME",1,BLACK)
    win.blit(text,(WIDTH/2-text.get_width()/2,10))
    pygame.draw.rect(win, BLACK, pygame.Rect(340, 200, 120, 60),  3)
    text=TITLE_FONT.render("PLAY",1,BLACK)
    win.blit(text,(350,200))
    pygame.draw.rect(win, BLACK, pygame.Rect(340, 270, 120, 60),  3)
    text=TITLE_FONT.render("EXIT",1,BLACK)
    win.blit(text,(WIDTH/2-text.get_width()/2,270))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()




#main(points)
pygame.quit()
