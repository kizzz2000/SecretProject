
import pygame
from pygame.locals import *

pygame.init()
width = 1000
height = 500
window = pygame.display.set_mode((width, height))
bg_img = pygame.image.load('space.png')
bg_img = pygame.transform.scale(bg_img, (width, height))

i = 0

runing = True
while runing:
    window.fill((0, 0, 0))
    window.blit(bg_img, (i, 0))
    window.blit(bg_img, (width + i, 0))
    if (i == -width):
        window.blit(bg_img, (width + i, 0))
        i = 0
    i -= 0.5
    for event in pygame.event.get():
        if event.type == QUIT:
            runing = False
    pygame.display.update()
pygame.quit()




# import pygame as pg
#
#
# class Entity(pg.sprite.Sprite):
#
#     def __init__(self, pos):
#         super().__init__()
#         self.image = pg.Surface((122, 70), pg.SRCALPHA)
#         pg.draw.polygon(self.image, pg.Color('dodgerblue1'),
#                         ((1, 0), (120, 35), (1, 70)))
#         # A reference to the original image to preserve the quality.
#         self.orig_image = self.image
#         self.rect = self.image.get_rect(center=pos)
#         self.angle = 0
#
#     def update(self):
#         self.angle += 2
#         self.rotate()
#
#     def rotate(self):
#         """Rotate the image of the sprite around its center."""
#         # `rotozoom` usually looks nicer than `rotate`. Pygame's rotation
#         # functions return new images and don't modify the originals.
#         self.image = pg.transform.rotozoom(self.orig_image, self.angle, 1)
#         # Create a new rect with the center of the old rect.
#         self.rect = self.image.get_rect(center=self.rect.center)
#
#
# def main():
#     screen = pg.display.set_mode((640, 480))
#     clock = pg.time.Clock()
#     all_sprites = pg.sprite.Group(Entity((320, 240)))
#
#     while True:
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 return
#
#         all_sprites.update()
#         screen.fill((30, 30, 30))
#         all_sprites.draw(screen)
#         pg.display.flip()
#         clock.tick(30)
#
#
# if __name__ == '__main__':
#     pg.init()
#     main()
#     pg.quit()







# import pygame
#
# pygame.init()
# screen = pygame.display.set_mode((1010, 1000))
# clock = pygame.time.Clock()
#
# def blitRotate(surf, image, pos, originPos, angle):
#
#     # offset from pivot to center
#     image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
#     offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
#
#     # roatated offset from pivot to center
#     rotated_offset = offset_center_to_pivot.rotate(-angle)
#
#     # roatetd image center
#     rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
#
#     # get a rotated image
#     rotated_image = pygame.transform.rotate(image, angle)
#     rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)
#
#     # rotate and blit the image
#     surf.blit(rotated_image, rotated_image_rect)
#
#     # draw rectangle around the image
#     pygame.draw.rect(surf, (255, 0, 0), (*rotated_image_rect.topleft, *rotated_image.get_size()),2)
#
# def blitRotate2(surf, image, topleft, angle):
#
#     rotated_image = pygame.transform.rotate(image, angle)
#     new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
#
#     surf.blit(rotated_image, new_rect.topleft)
#     pygame.draw.rect(surf, (255, 0, 0), new_rect, 2)
#
# try:
#     image = pygame.image.load('astroid.png')
# except:
#     text = pygame.font.SysFont('Times New Roman', 50).render('image', False, (255, 255, 0))
#     image = pygame.Surface((text.get_width()+1, text.get_height()+1))
#     pygame.draw.rect(image, (0, 0, 255), (1, 1, *text.get_size()))
#     image.blit(text, (1, 1))
# w, h = image.get_size()
#
# angle = 0
# done = False
# while not done:
#     clock.tick(60)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#
#     pos = (screen.get_width()/2, screen.get_height()/2)
#
#     screen.fill(0)
#     blitRotate(screen, image, pos, (w/2, h/2), angle)
#     #blitRotate2(screen, image, pos, angle)
#     angle += 1
#
#     pygame.draw.line(screen, (0, 255, 0), (pos[0]-20, pos[1]), (pos[0]+20, pos[1]), 3)
#     pygame.draw.line(screen, (0, 255, 0), (pos[0], pos[1]-20), (pos[0], pos[1]+20), 3)
#     pygame.draw.circle(screen, (0, 255, 0), pos, 7, 0)
#
#     pygame.display.flip()
#
# pygame.quit()
#
#
#
#
#
#
#
#





# import pygame
# pygame.init()
#
# #window width, and height ######################
# height = 650
# width  = 800
# astroid_pos_x = 100
# astroid_pos_y = 0
# clock = pygame.time.Clock()
#
# astroid = pygame.image.load('astroid.png')
# #astroid size ###############################
# astroid = pygame.transform.scale(astroid, (275, 275))
# #astroid start position######################
# astroid_rect = astroid.get_rect(center = (400, 325))
# #window width, and height ######################
# screen = pygame.display.set_mode((width, height))
#
# rotation = 1
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.QUIT
#             sys.exit()
#
#     if rotation >= 360:
#         rotation = 0
#     rotation += 1
#
#     rotated_astroid = pygame.transform.rotate(astroid, rotation)
#     rotated_astroid_rect = rotated_astroid.get_rect(center = astroid_rect.center)
#
#     screen.fill((0,0,0))
#
#     screen.blit(rotated_astroid, rotated_astroid_rect)
#
#     pygame.transform.rotate(astroid, (rotation))
#
#     astroid_pos_x += 1
#     astroid_pos_y += 1
#
#     pygame.display.flip()
#     clock.tick(60)




# import pygame
# import os
# pygame.init()
# width = 800
# height = 600

# screen = pygame.display.set_mode((width, height))
# redSquare = pygame.transform.scale(pygame.image.load(os.path.join("astroid.png")), (100, 100))
# fpsClock = pygame.time.Clock()
# imageX = 700 #x coordnate of image
# imageY = 30  # y coordinate of image
# running = True
# black = (0, 0, 0)
# while (running):  # main game loop
#     imageX -= 1
#     imageY += 1
#     screen.fill(black)  # clear screen
#     screen.blit(redSquare, (imageX, imageY))  # paint to screen
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             # Set the x, y postions of the mouse click
#             x, y = event.pos
#     pygame.display.update()
#     fpsClock.tick(30)
# # loop over, quite pygame
# pygame.quit()

