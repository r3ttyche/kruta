import pygame
import sys

# Инициализация Pygame
pygame.init()

# Задаем параметры окна
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Labyrinth Game')
clock = pygame.time.Clock()

# Определяем цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Определяем параметры квадратика
square_size = 20
square_x, square_y = 50, 50
speed = 5

# Создание лабиринта (0 - пустое место, 1 - стена)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    
    # Перемещение квадратика
    if keys[pygame.K_LEFT]:
        if maze[(square_y // square_size)][(square_x - speed) // square_size] == 0:
            square_x -= speed
    if keys[pygame.K_RIGHT]:
        if maze[(square_y // square_size)][(square_x + speed) // square_size] == 0:
            square_x += speed
    if keys[pygame.K_UP]:
        if maze[(square_y - speed) // square_size][(square_x // square_size)] == 0:
            square_y -= speed
    if keys[pygame.K_DOWN]:
        if maze[(square_y + speed) // square_size][(square_x // square_size)] == 0:
            square_y += speed

    # Рисуем всё на экране
    screen.fill(BLACK)

    # Рисуем лабиринт
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 1:
                pygame.draw.rect(screen, WHITE, (col * square_size, row * square_size, square_size, square_size))

    # Рисуем квадратик
    pygame.draw.rect(screen, GREEN, (square_x, square_y, square_size, square_size))

    pygame.display.flip()
    clock.tick(60)