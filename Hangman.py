import pygame
import sys
import math
import random

# Setup Display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# BUTTONS VARIABLE
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS*2 + GAP)*13) / 2)
starty = 350
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS*2 + GAP) * (i % 13))
    y = starty + ((i // 13)) * (GAP + RADIUS * 2)
    letters.append([x, y, chr(A+i), True])

# Fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 20)
WORD_FONT = pygame.font.SysFont('comicsans', 40)
TITLE_FONT = pygame.font.SysFont('comicsans', 60)
SCORE_FONT = pygame.font.SysFont('comicsans', 10)

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Background Image
def load_bg():
    background_image = pygame.image.load("C:/Users/aksha/OneDrive/Desktop/CODER/Devops_Lab/Hangman/bg_image.jpg")
    win.blit(background_image, (0, 0))

def draw(word, guessed, hangman_status, images, points, hint_visible, show_hint, hint):
    win.fill(WHITE)
    load_bg()
    # Title
    text = TITLE_FONT.render("HANGMAN_GAME", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 10))

    # Draw Words
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # Draw Score
    text = SCORE_FONT.render("SCORE: " + str(points), 1, BLACK)
    win.blit(text, (700, 50))

    # Draw Buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    if hint_visible:  # Only display the hint if it is visible
        pygame.draw.rect(win, BLACK, pygame.Rect(170, 450, 200, 30), 3)
        text = LETTER_FONT.render("HINT", 1, BLACK)
        win.blit(text, (240, 450))

    if show_hint:   
        text = LETTER_FONT.render("Hint: "+hint, 1, BLACK)
        win.blit(text, (400, 270))
    
    pygame.draw.rect(win, BLACK, pygame.Rect(400, 450, 200, 30), 3)
    text = LETTER_FONT.render("EXIT", 1, BLACK)
    win.blit(text, (470, 450))
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()

def reset(hangman_status, guessed):
    hangman_status = 0
    guessed = []
    for letter in letters:
        letter[3] = True

def main(points):
    # Load images
    images = []
    for i in range(7):
        image = pygame.image.load("C:/Users/aksha/OneDrive/Desktop/CODER/Devops_Lab/Hangman/hangman" + str(i) + ".png")
        images.append(image)
        images_rect = image.get_rect()

    # Game variables
    hangman_status = 0
    word = "DEVELOPER"
    hint = "Codes software and programs."
    guessed = []
    hint_visible = True  # Add a variable to track the visibility of the hint
    show_hint=False
    win_p=10
    # Setup Game
    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                hint_button_rect = pygame.Rect(170, 450, 200, 30)
                if hint_button_rect.collidepoint(event.pos):
                    hint_visible = False  # Hide the hint when the button is clicked
                    show_hint=True
                    win_p-=5
                exit_button_rect = pygame.Rect(400, 450, 200, 30)
                if exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
        draw(word, guessed, hangman_status, images, points, hint_visible, show_hint, hint)  # Pass the hint_visible variable to the draw function
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            points += win_p
            reset(hangman_status, guessed)
            pygame.time.delay(1000)
            win.fill(WHITE)
            load_bg()
            title_text = WORD_FONT.render("BINGO!!", 1, BLACK)
            title_rect = title_text.get_rect(center=(WIDTH/2, 100))
            win.blit(title_text, title_rect)
            text = WORD_FONT.render("You Guessed The Right Word", 1, BLACK)
            win.blit(text, (150, 180))
            text = WORD_FONT.render("Your Current Score: "+str(points), 1, BLACK)
            win.blit(text, (200, 250))
            pygame.display.update()
            pygame.time.delay(3000)
            reset(hangman_status, guessed)
            main(points)
            break

        if hangman_status == 6:
            reset(hangman_status, guessed)
            pygame.time.delay(1000)
            win.fill(WHITE)
            load_bg()
            draw_loser_screen(word, points)
            break


def main_menu():
    win.fill(WHITE)
    load_bg()
    # Title
    title_text = TITLE_FONT.render("HANGMAN GAME", 1, BLACK)
    title_rect = title_text.get_rect(center=(WIDTH/2, 100))
    win.blit(title_text, title_rect)

    # Play Button
    play_button = pygame.Rect(250, 250, 300, 80)
    pygame.draw.rect(win, BLACK, play_button, 3)
    play_text = WORD_FONT.render("PLAY", 1, BLACK)
    play_text_rect = play_text.get_rect(center=play_button.center)
    win.blit(play_text, play_text_rect)

    # Exit Button
    exit_button = pygame.Rect(250, 350, 300, 80)
    pygame.draw.rect(win, BLACK, exit_button, 3)
    exit_text = WORD_FONT.render("EXIT", 1, BLACK)
    exit_text_rect = exit_text.get_rect(center=exit_button.center)
    win.blit(exit_text, exit_text_rect)

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if play_button.collidepoint(mouse_x, mouse_y):
                    points = 0
                    main(points)
                elif exit_button.collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    sys.exit()
                    
def draw_loser_screen(word, points):
    win.fill(WHITE)
    load_bg()
    # Title
    title_text = TITLE_FONT.render("You Lost!!", 1, BLACK)
    title_rect = title_text.get_rect(center=(WIDTH/2, 50))
    win.blit(title_text, title_rect)

    text = WORD_FONT.render("Words was: " + str(word), 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 100))

    text = WORD_FONT.render("Your Score: " + str(points), 1, BLACK)
    win.blit(text, (WIDTH/1.9 - text.get_width()/1.8, 170))

    # Retry Button
    retry_button = pygame.Rect(250, 250, 300, 80)
    pygame.draw.rect(win, BLACK, retry_button, 3)
    retry_text = WORD_FONT.render("Retry", 1, BLACK)
    retry_text_rect = retry_text.get_rect(center=retry_button.center)
    win.blit(retry_text, retry_text_rect)

    # Exit Button
    exit_button = pygame.Rect(250, 350, 300, 80)
    pygame.draw.rect(win, BLACK, exit_button, 3)
    exit_text = WORD_FONT.render("Exit", 1, BLACK)
    exit_text_rect = exit_text.get_rect(center=exit_button.center)
    win.blit(exit_text, exit_text_rect)

    pygame.display.update()

points = 0

main_menu()
