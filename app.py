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
        img5, rect5 = draw_text(screen, "Exit or press Enter to save", (50, 500))
        if cursor.colliderect(rect5):
            pg.draw.rect(screen, (255,255,0), rect5, 1)
    if run_b:
        img_1_b = draw_text(screen, "Yours previous entries", (0, 200))
        if len(entry_list) < 1:
            draw_text(screen, "No entries", (50, 250))
        elif len(entry_list) < 2:
            draw_text(screen, "1. " + entry_list[0], (50, 250))
        elif len(entry_list) < 5:
            for id,entry in enumerate(entry_list[::-1]):
                draw_text(screen, entry, (50, 250 + 50*id))
        else:
            for id,entry in enumerate(entry_list[len(entry_list)-1:len(entry_list)-6:-1]):
                draw_text(screen, entry, (50, 250 + 50*id))


        img_2_b, rect_2_b = draw_text(screen, "Exit view mode", (50, 500))
        if cursor.colliderect(rect_2_b):
            pg.draw.rect(screen, (255,255,0), rect_2_b, 1)

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
                    if len(text) > 0:
                        entry_list.append(text)
                        text = "Click here to start writing or to delete changes"
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
                if cursor.colliderect(rect4):
                    text = ""
            if run_b:
                if cursor.colliderect(rect_2_b):
                    run_b = False

            if cursor.colliderect(rect1) and run_b == False:
                run_a = True
            if cursor.colliderect(rect2) and run_a == False:
                run_b = True
                
        
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

