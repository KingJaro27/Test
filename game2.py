import pygame
import random

# Initialisierung von Pygame
pygame.init()

# Fenstergröße und Hintergrundfarbe
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
bg_color = (0, 0, 0)

# Snake Geschwindigkeit und Startposition
snake_speed = 12
snake_block = 25
x = width // 2
y = height // 2
x_change = 0
y_change = 0

# Snake Farbe und Länge
snake_color = (0, 255, 0)
snake_body = []
snake_length = 1

# Essen Position und Farbe
food_color = (255, 0, 0)
food_x = random.randint(0, width - snake_block) // snake_block * snake_block
food_y = random.randint(0, height - snake_block) // snake_block * snake_block

clock = pygame.time.Clock()

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -snake_block
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = snake_block
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = -snake_block
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = snake_block
                x_change = 0

    if x >= width or x < 0 or y >= height or y < 0:
        running = False

    x += x_change
    y += y_change

    screen.fill(bg_color)

    pygame.draw.rect(screen, snake_color, [x, y, snake_block, snake_block])

    snake_head = []
    snake_head.append(x)
    snake_head.append(y)
    snake_body.append(snake_head)
    if len(snake_body) > snake_length:
        del snake_body[0]

    for part in snake_body[:-1]:
        if part == snake_head:
            running = False

    for part in snake_body:
        pygame.draw.rect(
            screen, snake_color, [part[0], part[1], snake_block, snake_block]
        )

    pygame.draw.rect(screen, food_color, [food_x, food_y, snake_block, snake_block])

    if x == food_x and y == food_y:
        snake_length += 1
        food_x = random.randint(0, width - snake_block) // snake_block * snake_block
        food_y = random.randint(0, height - snake_block) // snake_block * snake_block

    pygame.display.update()

    clock.tick(snake_speed)

pygame.quit()
