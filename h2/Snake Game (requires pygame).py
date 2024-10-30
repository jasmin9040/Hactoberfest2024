import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

# Set up snake and food
snake = [(20, 20)]
direction = (20, 0)
food = (random.randint(1, 19) * 20, random.randint(1, 19) * 20)

def move_snake():
    global snake, food, direction
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)
    if new_head == food:
        food = (random.randint(1, 19) * 20, random.randint(1, 19) * 20)
    else:
        snake.pop()

def game_over():
    head = snake[0]
    if head[0] < 0 or head[0] >= 400 or head[1] < 0 or head[1] >= 400 or head in snake[1:]:
        pygame.quit()
        sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 20):
                direction = (0, -20)
            elif event.key == pygame.K_DOWN and direction != (0, -20):
                direction = (0, 20)
            elif event.key == pygame.K_LEFT and direction != (20, 0):
                direction = (-20, 0)
            elif event.key == pygame.K_RIGHT and direction != (-20, 0):
                direction = (20, 0)
    
    move_snake()
    game_over()
    
    screen.fill((0, 0, 0))
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, 20, 20))
    pygame.draw.rect(screen, (255, 0, 0), (*food, 20, 20))
    
    pygame.display.flip()
    clock.tick(10)
