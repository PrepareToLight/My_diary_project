from rect import *

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

    if run_a:
        img4, rect4 = draw_text(screen, text, (0, 200))
        img5, rect5 = draw_text(screen, "Exit editing mode without saving", (50, 500))
        if cursor.colliderect(rect5):
            pg.draw.rect(screen, (255,255,0), rect5, 1)

    #those lines ables us to terminate the program and some other functionality
    for event in pg.event.get():
        print(event) #right now i need this to track all events
        if event.type == pg.QUIT:   
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False
            if run_a:
                if event.key == pg.K_BACKSPACE: 
                    if len(text) > 0:
                        text = text[:-1]
                elif event.key == 13:
                    entry_list.append(text)
                    text = "Enter your text here"
                    run_a = False
                else:
                    text += event.unicode

        if event.type == pg.MOUSEMOTION:
            x, y = event.pos
        if event.type == pg.MOUSEBUTTONDOWN:
            if cursor.colliderect(rect3):
                run = False
            if run_a:
                if cursor.colliderect(rect5):
                    run_a = False
            if cursor.colliderect(rect1):
                run_a = True
                
        
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

