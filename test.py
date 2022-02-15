import pygame
import os
pygame.init()
width = 800
height = 600
def astroid():
    screen = pygame.display.set_mode((width, height))
    redSquare = pygame.transform.scale(pygame.image.load(os.path.join("astroid.png")), (100, 100))
    fpsClock = pygame.time.Clock()
    imageX =700 #x coordnate of image
    imageY = 30  # y coordinate of image
    running = True
    black = (0, 0, 0)
    while (running):  # main game loop
        imageX -= 1
        screen.fill(black)  # clear screen
        screen.blit(redSquare, (imageX, imageY))  # paint to screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos
        pygame.display.update()
        fpsClock.tick(30)
    # loop over, quite pygame
    pygame.quit()