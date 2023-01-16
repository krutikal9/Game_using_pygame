import pygame

pygame.init()
sc = pygame.display.set_mode((100,100))
pygame.display.set_caption()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
