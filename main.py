# импорт
import pygame
import sys

FPS = 60

pygame.init()
pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# если надо до цикла отобразить какие либо обьекты то обновляем экран
pygame.display.update()

# главный цикл
while True:

    # задержка
    clock.tick(FPS)

    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    # изменение объектов

    # обновление экрана (обязательно!!!)
    pygame.display.update()
