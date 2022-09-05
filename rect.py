import pygame as pg

pg.init()

#screen specs
background = (0,0,0)
FPS = 60
size = width, height = 900, 600
run = True
COLOR = (0,255,0)

screen = pg.display.set_mode(size)
clock = pg.time.Clock()


Font = pg.font.SysFont(None, 24) #none tells us that we dont specify the "font" style
#it's going to be a defaoult systems font. Secound part is the fontsize

def draw_text(screen, text: str, position: tuple = (0, 0)) -> None:
    img = Font.render(text, True, (0,255,255))
    screen.blit(img, position)

