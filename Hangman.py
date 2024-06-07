import pygame
import sys
import math
import random
import time
import warnings
warnings.filterwarnings("ignore", category=UserWarning, message=".*iCCP: known incorrect sRGB profile.*")
# Setup Display
pygame.init()
WIDTH, HEIGHT = 800, 500
def display():
    global win
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
    y = starty + ((i // 13)) * (GAP + RADIUS *2)
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
        image = pygame.image.load("C:/Users/aksha/OneDrive/Desktop/CODER/Devops_Lab/Hangman/hangman" + str(i) + ".jpg")
        images.append(image)
        images_rect = image.get_rect()

    # Game variables
    hangman_status = 0
    words = [
    'apple', 'baby', 'beach', 'bird', 'book', 'box', 'bus', 'cake', 'cat', 'chair',
    'chicken', 'cloud', 'coin', 'computer', 'cup', 'dog', 'door', 'duck', 'egg', 'eye',
    'fish', 'flower', 'food', 'frog', 'game', 'girl', 'guitar', 'hat', 'house', 'jacket',
    'key', 'kite', 'lemon', 'light', 'lion', 'lock', 'love', 'map', 'money', 'moon']
    hints = [
    "Fruit with red or green skin.", "A newborn human.", "Sandy shore by the ocean.", "Feathered creature that can fly.", "An item to read for pleasure.",
    "A container for storing things.", "Large vehicle for public transport.", "Sweet dessert often with frosting.", "A furry pet that says 'meow.'", "A piece of furniture to sit on.",
    "Bird raised for eggs and meat.", "White puffy moisture in the sky.", "Circular piece of metal as currency.", "Device for work and play.", "Container for holding beverages.",
    "A loyal four-legged companion.", "Entryway into a building.", "Waterfowl known for quacking.", "Protein-rich breakfast food.", "Body part for seeing.",
    "Aquatic creature with fins.", "Colorful plant often given as a gift.", "Edible items we consume.", "Amphibian known for jumping.", "Form of entertainment or play.",
    "Young female human.", "Musical instrument with strings.", "Headwear to protect from sun.", "A dwelling where people live.", "Outerwear to stay warm.",
    "Tool to open doors or locks.","A flying object that soars in the sky.",
    "A sour yellow fruit often used in drinks.",
    "Source of illumination in the dark.", 
    "A majestic wild cat known for its mane.", 
    "A device used to secure something.", "Deep affection and care.", "Navigation tool with directions.", "Currency in coins and bills.", "Luminous celestial body."]

# Now, the hints list contains hints corresponding to each word in the words list.

    index=random.randint(0,len(words)-1)
    word = words[index].upper()
    hint = hints[index]
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
                    print("\nThank You For Playing")
                    print("\nName: "+name)
                    print("\nYour Score: "+ str(points))
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
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if retry_button.collidepoint(mouse_x, mouse_y):
                    points = 0  # Reset the points
                    main(points)  # Call the main() function to start a new game
                elif exit_button.collidepoint(mouse_x, mouse_y):
                    print("\nThank You For Playing")
                    print("\nName: "+name)
                    print("\nYour Score: "+ str(points))
                    pygame.quit()
                    sys.exit()


def Wanna_Play():
    Ans=input("\nShall we Start the Hangman game (y/n): ")
    if Ans.lower()== 'y':
        display()
        main_menu()
    elif Ans.lower()=='n':
        print("(: THANK YOU :)")
        sys.exit()
    else:
        print("\nInvalid Input!!!\nPlease enter only 'y' or 'n':>>\n")
        time.sleep(2)
        Wanna_Play()

def Rules():
    print('''
            HANGMAN RULES

Objective: Guess the randomly selected hidden word before you run out of attempts.

Game Setup:

The program selects a word at random and displays the empty spaces for each letter.
You start with 6 number of attempts.

Guessing Letters:

You try to guess letters one at a time.
Correct guesses fill in the blank spaces.
Incorrect guesses result in losing an attempt.

Winning Points:

If you correctly guess the word without using a hint, you earn 10 points for that word.
Using Hints:

If you use a hint (e.g., asking for a clue), you earn 5 points for that word.

Retry:

If you lose the game by running out of attempts, you can retry and play again with a new randomly chosen word.

End of Game:

The game ends when you either correctly guess the word, run out of attempts, or choose to quit.

Scoring:

Keep track of points earned for each word guessed correctly.
Enjoy the game and aim for a high score!

''')
points = 0
print("\n\t\t  Hangman 𝙶𝚊𝚖𝚎 ")
name=input("\nEnter Your Full Name: ").title()
intro="\nHello, {} ! 😊\n(: I hope you will enjoy this Game 😁 :)"  
print(intro.format(name))
Rules()
time.sleep(2)
Wanna_Play()
print("\nThank You For Playing")
print("\nName: "+name)
print("\nYour Score: "+ str(points))
