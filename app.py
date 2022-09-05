from rect import *


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


while run:
    clock.tick(FPS)
    #those lines ables us to terminate the program and some other functionality
    for event in pg.event.get():
        if event.type == pg.QUIT:   
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False
    
    draw_text(screen, menu)
    

    pg.display.flip() #how is it diffrent from update?


pg.quit()

