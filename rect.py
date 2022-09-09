import pygame as pg

pg.init()

#screen specs
background = (0,0,0)
FPS = 60
size = width, height = 900, 600
run = True
run_a = False
run_b = False
COLOR = (0,255,0)

screen = pg.display.set_mode(size)
clock = pg.time.Clock()


Font = pg.font.SysFont(None, 50) #none tells us that we dont specify the "font" style
#it's going to be a defaoult systems font. Secound part is the fontsize

def draw_text(screen, text: str, position: tuple = (0, 0)) -> None:
    img = Font.render(text, True, (255,255,255))
    rect = img.get_rect()
    rect.x, rect.y = position
    screen.blit(img, position)
    return img, rect

#some variables
Menu= ["Select option: ", "a) Add new entry", "b) View entrys", "c) Exit Dairy", "d) Show menu", "Your selection: "]
text = "Click here to start writing or to delete changes"
entry_list = []


