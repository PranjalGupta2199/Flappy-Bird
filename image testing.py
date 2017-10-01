import pygame,time,sys
from pygame.locals import *

pygame.init()
class game_window():
    def __init__(self,width,height,color,caption):
        self.resolution = width,height
        self.bckg_color = color
        self.caption = caption

    def Pygame_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption(self.caption)
        self.screen.fill(self.bckg_color)
        pygame.display.update()

    def display_text(self,text,color,size,font,x,y):
        self.font = pygame.font.SysFont(font,size)
        self.label = self.font.render(text,1,color)
        self.screen.blit(self.label,(x,y))
        pygame.display.update()



WHITE = 255,255,255
img = pygame.image.load('background.png')
img2 = pygame.image.load('flappybird.png')
img2 = pygame.transform.scale(img2,(150,100))
img = pygame.transform.scale(img,(400,400))
running = True
x = 0

speed = 10000
set1 = game_window(400,400,WHITE,'IMAGE_TESTING')
set1.Pygame_init()
game_time = time.clock()

while running:
    Time = (time.clock() - game_time)
    x += speed * Time
    if x >= 400:
        x = 0
    set1.screen.blit(img, (x, 0))
    set1.screen.blit(img,(0,0),(400-x,0,x,400))
    set1.screen.blit(img2,(100,0))
    game_time = time.clock()


    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()







