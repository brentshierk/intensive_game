import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()

test_surface = pygame.Surface((100,200))


sky_surface = pygame.image.load('./bg_desert.png')
ground_surface = pygame.image.load('./grasshalf.png')
#text_surface = test_font.render('my game',False,'Green')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface(0,300))

    pygame.display.update()
    clock.tick(60)