import pygame, random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(20, 590)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

red = (255,0,0)
fps = 10



pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

total = 0
pont = 0

snake = [(200, 200), (210, 200), (220,200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255,255,255))

fundo = pygame.image.load('fundo.jpg')

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((200,0,0))
my_direction = None

clock = pygame.time.Clock()

font = pygame.font.Font(None, 30)



while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            #UP
            if my_direction == DOWN:
                pass
            else:    
                if event.key == K_w:
                    my_direction = UP
            #DOWN
            if my_direction == UP:
                pass
            else:  
                if event.key == K_s:
                    my_direction = DOWN
            #LEFT
            if my_direction == RIGHT:
                pass
            else:  
                if event.key == K_a:
                    my_direction = LEFT
            #RIGHT
            if my_direction == LEFT:
                pass
            else:  
                if event.key == K_d:
                    my_direction = RIGHT
            if event.key == K_ESCAPE:
                pygame.quit()
        
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        fps = fps + 1  
        total = total + 1 
     
    if int(total) > int(pont):
        pont = int(total)
        print(total)
            
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])
        
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
        
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1]) 
    
    if snake[0][0] and snake[0][1] > 590:
        pygame.quit()
    if snake[0][0] > 590:
        pygame.quit()
    if snake[0][0] and snake[0][1] < 0:
        pygame.quit()
    if snake[0][0] < 0:
        pygame.quit()
    
    pontos = font.render("Pontuação: {}".format(total), True, red)
    placar = font.render("Recorde: {}".format(pont), True, red)
    screen.blit(fundo, (0, 0))
    screen.blit(apple, apple_pos)
    screen.blit(pontos, (460, 5))
    screen.blit(placar, (5, 5))
    for pos in snake:
        screen.blit(snake_skin, pos)
            
    pygame.display.update()
    