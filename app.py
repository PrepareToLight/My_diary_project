from rect import *

Menu= ["Select option: ", "a) Add new entry", "b) View entrys", "c) Exit", "d) Show menu", "Your selection: "]
menu = '''Select option: 
a) Add new entry
b) View entrys
c) Exit
d) Show menu

Your selection: '''
entry_list = []

def dairy():
    run, show = True, True
    while run:

        if show == True:
            print(menu)
            show = False
        else:
            print("Your selection: (for menu press d)")

        choice = input()
        if choice.lower() == "a":
            print("Add new entry: ")
            new_entry = input()
            entry_list.append(new_entry)
        elif choice.lower() == "b":
            print(entry_list)
        elif choice.lower() == "c":
            run = False
        elif choice.lower() == "d":
            show = True

pg.init()

x,y = -100, -100
while run:
    clock.tick(FPS)

    cursor = pg.Rect(x, y, 10, 10)
    screen.fill(background) #this isn so important to refresh screen
    
    img0, rect0 = draw_text(screen, Menu[0])
    img1, rect1 = draw_text(screen, Menu[1], (50, 51))
    img2, rect2 = draw_text(screen, Menu[2], (50, 101))
    img3, rect3 = draw_text(screen, Menu[3], (50, 151))


    #those lines ables us to terminate the program and some other functionality
    for event in pg.event.get():
        print(event) #right now i need this to track all events
        if event.type == pg.QUIT:   
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False
        if event.type == pg.MOUSEMOTION:
            x, y = event.pos
        if event.type == pg.MOUSEBUTTONDOWN:
            if cursor.colliderect(rect3):
                run = False
        
    if cursor.colliderect(rect3):
        pg.draw.rect(screen, (255,255,0), rect3, 1)
    elif cursor.colliderect(rect2):
        pg.draw.rect(screen, (255,255,0), rect2, 1)
    elif cursor.colliderect(rect1):
        pg.draw.rect(screen, (255,255,0), rect1, 1)

    #uncomment if you want to see a cursor rect position position
    #pg.draw.rect(screen, (255,0,0), cursor, 1) 

    pg.display.flip() #how is it diffrent from update?


pg.quit()

