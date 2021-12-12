# Подключить нужные модули
from random import randint 
import pygame 
pygame.init() 

win_width = 800 
win_height = 600
left_bound = win_width / 40             # границы, за которые персонаж не выходит (начинает ехать фон)
right_bound = win_width - 8 * left_bound
shift = 0

img_file_back = 'cave.png'
img_file_hero = 'm1.png'
img_file_enemy = 'enemy.png' 
img_file_bomb = 'bomb.png'
img_file_princess = 'princess.png'
FPS = 60



pygame.display.set_caption("ARCADA") 
window = pygame.display.set_mode([win_width, win_height])

back = pygame.transform.scale(pygame.image.load(img_file_back).convert(), (win_width, win_height)) 

x = 0
run = True
while run:

    local_shift = x % win_width
    
    print(local_shift)
    window.blit(back, (local_shift, 0)) 
    if local_shift != 0:
        window.blit(back, (local_shift - win_width, 0)) 

    x -= 2

    # Обработка событий
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False 
    
    pygame.display.update() 

    # Пауза
    pygame.time.delay(20)