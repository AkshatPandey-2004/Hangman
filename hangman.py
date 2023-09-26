import pygame
import os
#Setup Display
pygame.init()
WIDTH, HEIGHT=800, 500
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman Game")

#load images
images=[]
for i in range(7):
    image=pygame.image.load("C:/Users/aksha/OneDrive/Desktop/CODER/Devops_Lab/Hangman/hangman"+str(i)+".png")
    images.append(image)


#colour
WHITE=(255,255,255)
#game variable
hangman_status=0

#Setup Game
FPS=60
clock=pygame.time.Clock()
run=True
while run:
    clock.tick(FPS)

    win.fill(WHITE)
    win.blit(images[hangman_status],(150,100))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            print(pos)

pygame.quit()
