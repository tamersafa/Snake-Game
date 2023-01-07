from utils .settings import *
import random
from datetime import datetime

WIN = pygame.display.set_mode((WIDTH,HEIGHT+100))
pygame.display.set_caption("Snake Game")

SUR = pygame.Surface((WIDTH, HEIGHT))
SCO = pygame.Surface((WIDTH, 100))

font = pygame.font.SysFont('Helvetica', 16)

''' VARIABLES '''

## INITIAL SNAKE POSITION
snake_y = random.randrange(0, HEIGHT, BLOCKSIZE)
snake_x = random.randrange(0, WIDTH, BLOCKSIZE) 

snake_size = 1
snake = [(snake_x, snake_y)]

## INITIAL FOOD POSITION
food_y = random.randrange(0, HEIGHT, BLOCKSIZE)
food_x = random.randrange(0, WIDTH, BLOCKSIZE) 

moves = [False, False, False, False]

''' FUNCTIONS '''

def time_now(t):
    seconds = str(elaps.seconds-60*(elaps.seconds//60))
    minutes = str(elaps.seconds//60)

    if int(seconds) < 10:
        seconds = '0'+seconds
    if int(minutes) < 10:
        minutes = '0'+minutes

    return "Elapsed Time: " + minutes + ":" + seconds

def grid():
    SUR.fill(BLACK)
    SCO.fill(WHITE)
    
def show_score():
    pygame.display.set_caption()

def set_food_pos():
    global food_x, food_y, snake
    while (food_x, food_y) in snake:
        food_y = random.randrange(0, HEIGHT, BLOCKSIZE)
        food_x = random.randrange(0, WIDTH, BLOCKSIZE) 
    
    return (food_x, food_y)


def move_snake():
    global snake_x, snake_y, snake, snake_size, moves

    rect = pygame.Rect(snake_x, snake_y, BLOCKSIZE, BLOCKSIZE)

    if moves[0] and rect.top-BLOCKSIZE >= 0:
        snake_y-=BLOCKSIZE
    if moves[1] and rect.bottom+BLOCKSIZE <= HEIGHT:
        snake_y+=BLOCKSIZE
    if moves[2] and rect.right+BLOCKSIZE <= WIDTH:
        snake_x+=BLOCKSIZE
    if moves[3] and rect.left-BLOCKSIZE >= 0:
        snake_x-=BLOCKSIZE

    snake.append((snake_x, snake_y))
    
    for i in range(len(snake)-snake_size):
        rect = pygame.Rect(snake[i][0], snake[i][1], BLOCKSIZE, BLOCKSIZE)
        pygame.draw.rect(SUR, BLACK, rect, 1)
        snake.remove(snake[i])

    for i in range(snake_size):
        rect = pygame.Rect(snake[-1-i][0], snake[-1-i][1], BLOCKSIZE, BLOCKSIZE)
        pygame.draw.rect(SUR, RED, rect, 100)


def draw_grid():
    global snake, snake_x, snake_y, snake_size, food_x, food_y
    grid()
    
    if snake_x == food_x and snake_y == food_y:
        snake_size += 1
        food_x, food_y = set_food_pos()
        rect = pygame.Rect(food_x, food_y, BLOCKSIZE, BLOCKSIZE)
        pygame.draw.rect(SUR, RED, rect, 100)

    move_snake()

    rect = pygame.Rect(food_x, food_y, BLOCKSIZE, BLOCKSIZE)
    pygame.draw.rect(SUR, GREEN, rect, 100)
    pygame.display.update()

''' PYGAME SETUP '''

run = True
clock = pygame.time.Clock()
start_time = datetime.now()
end_time = 0

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            keys_pressed = pygame.key.get_pressed()

            if keys_pressed[pygame.K_UP]:
                moves = [True, False, False, False]
            if keys_pressed[pygame.K_DOWN]:
                moves = [False, True, False, False]
            if keys_pressed[pygame.K_RIGHT]:
                moves = [False, False, True, False]
            if keys_pressed[pygame.K_LEFT]:
                moves = [False, False, False, True]

    draw_grid()
    WIN.blit(SUR, (0,0))
    WIN.blit(SCO, (0,HEIGHT))

    score = font.render("Snake Size: "+str(snake_size),True, (0,0,0))

    end_time = datetime.now()
    elaps = end_time - start_time
    s = time_now(elaps)
    timer = font.render(s, True, (0,0,0))

    WIN.blit(score, (10,HEIGHT+45))
    WIN.blit(timer, (500,HEIGHT+45))

pygame.quit()