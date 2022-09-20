import pygame as pg
from database import *

class Text:
    def __init__(self, text, pos, fontsize=72, **options) -> None:
        self.text = text
        self.pos = pos

        self.fontname = None
        self.fontsize = fontsize
        self.fontcolor = (255,255,255)
        self.set_font()
        self.render()

    def set_font(self) -> None:
        self.font = pg.font.Font(self.fontname, self.fontsize)

    def render(self) -> None:
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos
    
    def draw(self):
        App.screen.blit(self.img, self.rect)

class Cursor:
    def __init__(self, color = (255,0,0)) -> None:
        self.x = -10
        self.y = -10
        self.color = color

    def show(self, Screen) -> None:
        pg.draw.rect(Screen, self.color, self.cursor, 1)

    def update(self):
        self.cursor = pg.Rect(self.x, self.y, 10, 10)

class Scene_Main:
    def __init__(self) -> None:
        self.run = True
        self.title = Text(text="My Dairy", pos=(400,0))
        self.option_a = Text(text="a) Add new entry", pos=(100,100))
        self.option_b = Text(text="b) View entrys", pos=(100,200))
        self.option_c = Text(text="c) Exit Dairy", pos=(100,300))
        self.option_a_run = False
        self.option_b_run = False
        self.option_c_run = False

    def show(self) -> None:
        self.title.draw()
        self.option_a.draw()
        self.option_b.draw()
        self.option_c.draw()

    def highlight(self, cursor):
        if cursor.cursor.colliderect(self.option_a.rect):
            pg.draw.rect(App.screen, (255,255,0), self.option_a.rect, 1)
            self.option_a_run = True
        else:
            self.option_a_run = False
        if cursor.cursor.colliderect(self.option_b.rect):
            pg.draw.rect(App.screen, (255,255,0), self.option_b.rect, 1)
            self.option_b_run = True
        else:
            self.option_b_run = False
        if cursor.cursor.colliderect(self.option_c.rect):
            pg.draw.rect(App.screen, (255,255,0), self.option_c.rect, 1)
            self.option_c_run = True
        else:
            self.option_c_run = False



class Scene_A:
    def __init__(self) -> None:
        self.run = False
        self.exit_run = False
        self.title = Text(text="Type text, than press ENTER:", pos=(100, 10))
        self.exit = Text(text="Back", pos=(700,500))
        self.container = pg.Rect(100, 100, 700, 50)
        self.text = ""
        self.letters = Text(text=self.text, pos=self.container.topleft)
        

    def show(self, screen) -> None:
        pg.draw.rect(screen, (255,0,255), self.container, 1)
        self.title.draw()
        self.exit.draw()
        self.letters.draw()
        

    def highlight(self, cursor):
        if cursor.cursor.colliderect(self.exit.rect):
            pg.draw.rect(App.screen, (255,255,0), self.exit.rect, 1)
            self.exit_run = True

    def write(self, event):
        if event.key == pg.K_BACKSPACE:
            if len(self.text) > 0:
                self.text = self.text[:-1]
                self.letters = Text(text=self.text, pos=self.container.topleft, fontsize=36)
        elif event.key == 13: #stands for ENTER key
            if len(self.text) > 0:
                add_entries(self.text)
                my_dairy_databse.input_to_table(entries[-1]["date"][:-7], self.text, table_name="entries")
                self.text = ""
                self.letters = Text(text=self.text, pos=self.container.topleft, fontsize=36)
        else:
            self.text += event.unicode
            self.letters = Text(text=self.text, pos=self.container.topleft, fontsize=36)
        
        

#this class repesents the scene for view option
class Scene_B:
    def __init__(self) -> None:
        self.run = False
        self.exit_run = False
        self.title = Text(text="Your latest Entrys", pos=(100,10))
        self.exit = Text(text="Back", pos=(700,500))

    def show(self) -> None:
        self.title.draw()
        self.exit.draw()

    def highlight(self, cursor):
        if cursor.cursor.colliderect(self.exit.rect):
            pg.draw.rect(App.screen, (255,255,0), self.exit.rect, 1)
            self.exit_run = True

    def show_entries(self, data_entries):    
        for i,entry in enumerate(data_entries[::-1]):
            Text(text=f"{entry['date'][0:10]} : {entry['content']}", pos=(0,30*(i+2)), fontsize=36).draw()
            

class Scene_Exit:
    def __init__(self, width, height) -> None:
        w, h = 300, 150
        self.run = False
        self.exit_run = False
        self.close_app_run = False
        self.window = pg.Rect(int(width/2-w/2), int(height/2-h/2), w, h)
        self.exit = Text(text="No", pos=self.window.bottomright)
        self.exit.rect.bottomright = self.window.bottomright
        self.close_app = Text(text="Yes", pos=self.window.bottomleft)
        self.close_app.rect.bottomleft = self.window.bottomleft
        self.title = Text(text="Are you sure?", pos=self.window.midtop)
        self.title.rect.midbottom = self.window.midtop
        #self.window.width = self.title.rect.width
        #self.window.height = self.title.rect.height

    def show(self, screen):
        pg.draw.rect(screen,(255,255,255),self.window,1)
        self.title.draw()
        self.exit.draw()
        self.close_app.draw()

    def highlight(self, cursor):
        if cursor.cursor.colliderect(self.exit.rect):
            pg.draw.rect(App.screen, (255,255,0), self.exit.rect, 1)
            self.exit_run = True
            self.close_app_run = False
        if cursor.cursor.colliderect(self.close_app.rect):
            pg.draw.rect(App.screen, (255,255,0), self.close_app.rect, 1)
            self.close_app_run = True

class App:
    def __init__(self, width: int = 640, height: int = 240) -> None:
        pg.init()
        App.width = width
        App.height = height
        App.running = True
        flags = pg.RESIZABLE
        App.screen = pg.display.set_mode((width, height), flags)

        #initialize Other Classes class
        App.cursor = Cursor()
        App.main_scene = Scene_Main()
        App.scene_a = Scene_A()
        App.scene_b = Scene_B()
        App.scene_exit = Scene_Exit(width, height)


    def run(self):
        while App.running:
            for event in pg.event.get():
                #print(event)
                if event.type == pg.QUIT:
                    App.running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        App.running = False
                    if App.scene_a.run:
                        App.scene_a.write(event)
                if event.type == pg.MOUSEMOTION:
                    App.cursor.x, App.cursor.y = event.pos
                if event.type == pg.MOUSEBUTTONDOWN:
                    if App.main_scene.option_a_run:
                        App.main_scene.run = False
                        App.scene_a.run = True
                    if App.scene_a.exit_run:
                        App.scene_a.exit_run = False
                        App.scene_a.run = False
                        App.main_scene.run = True
                    if App.main_scene.option_b_run:
                        App.main_scene.run = False
                        App.scene_b.run = True
                    if App.scene_b.exit_run:
                        App.scene_b.exit_run = False
                        App.scene_b.run = False
                        App.main_scene.run = True
                    if App.main_scene.option_c_run:
                        App.main_scene.run = False
                        App.scene_exit.run = True
                    if App.scene_exit.exit_run:
                        App.scene_exit.exit_run = False
                        App.scene_exit.run = False
                        App.main_scene.run = True
                    if App.scene_exit.close_app_run:
                        App.running = False
                        
            App.screen.fill((0,0,0))
            App.cursor.update()
            if App.main_scene.run:
                App.main_scene.show()
                App.main_scene.highlight(App.cursor)
            elif App.scene_a.run:
                App.scene_a.show(App.screen)
                App.scene_a.highlight(App.cursor)
            elif App.scene_b.run:
                App.scene_b.show()
                App.scene_b.highlight(App.cursor)
                #print(entries)
                App.scene_b.show_entries(entries)
            elif App.scene_exit.run:
                App.scene_exit.show(App.screen)
                App.scene_exit.highlight(App.cursor)

            App.cursor.show(App.screen)
            pg.display.flip() #if you are going to test it you may find
            #qait suprising what You see. To prevent it uncomment this method, but before ypu see it :)
        pg.quit()

def main(width=900, height=600):
    App(width, height).run()

if __name__ == "__main__":
    
    #we connect the databse or creating it if we start program for the first time
    my_dairy_databse = DataBase("MyDairy")
    my_dairy_databse.create_table("entries", {"date_time": "TEXT", "content": "TEXT"})


    main()

    
    my_dairy_databse.close()
    #and we close it on the last line