menu = '''Select option: 
a) Add new entry
b) View entrys
c) Exit
d) Show menu

Your selection: '''
entry_list = []


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