import pygame
import time
import random

pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Define display dimensions
display_width = 600
display_height = 400

# Define block size and speed
block_size = 10
snake_speed = 15

# Set up display
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

# Clock to control game speed
clock = pygame.time.Clock()

# Define font styles
score_font = pygame.font.SysFont(None, 25)
message_font = pygame.font.SysFont(None, 45)

# Function to display score
def display_score(score):
    score_text = score_font.render("Score: " + str(score), True, white)
    score_rect = pygame.Rect(0, 0, 100, 30)
    pygame.draw.rect(display, blue, score_rect)
    display.blit(score_text, [10, 5])

# Function to draw the snake
def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], block_size, block_size])

# Function to display message
def display_message(msg, submsg, color):
    mesg = message_font.render(msg, True, color)
    submesg = message_font.render(submsg, True, color)
    display.blit(mesg, [display_width / 2 - mesg.get_width() / 2, display_height / 3])
    display.blit(submesg, [display_width / 2 - submesg.get_width() / 2, display_height / 3 + 50])

# Main function for the game loop
def game_loop():
    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            display.fill(black)
            display_message("You Lost", "Press Y to Play Again or N to Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_y:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        x1 += x1_change
        y1 += y1_change

        # Wrap around the screen
        if x1 >= display_width:
            x1 = 0
        elif x1 < 0:
            x1 = display_width - block_size
        if y1 >= display_height:
            y1 = 0
        elif y1 < 0:
            y1 = display_height - block_size

        display.fill(black)
        pygame.draw.rect(display, red, [foodx, foody, block_size, block_size])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(block_size, snake_List)
        display_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
