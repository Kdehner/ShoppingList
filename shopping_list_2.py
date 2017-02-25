# make a list to hold onto our items
shopping_list = []

def show_help():
    # print out instructions on how to use the app
    print('What should we pick up at the store?')
    print("""
Enter "DONE" to stop adding items!
Enter "SHOW" to view the items on your list so far!
Enter "HELP" at any time to view this information again!
Enter "SAVE" to save your shopping list!
Enter "NEW" to  start a new shopping list!""")

def show_list():
    # print out the list
    print ("Heres your list!")

    for item in shopping_list:
        print(item)

def add_to_list(new_item):
        # add new items to our list
        shopping_list.append(new_item.title())
        print('Added {}. List now has {} items.'.format(new_item, len(shopping_list)))

def open_shopping_list(str):
    shopping_list_file = open('shopping_list.txt', str)
    return shopping_list_file

def save_shopping_list():
    shopping_list_file = open_shopping_list('w')
    for item in shopping_list:
        shopping_list_file.write(item + '\n')
    close_shopping_file(shopping_list_file)
    print('~~ LIST SAVED! ~~')

def close_shopping_file(file):
    file.close()

def update_shopping_list():
    shopping_list_file = open_shopping_list('r')
    for item in shopping_list_file:
        shopping_list.append(item)
    close_shopping_file(shopping_list_file)
    show_list()

def shopping_list_new():
    shopping_list_file = open_shopping_list('w')
    close_shopping_file(shopping_list_file)
    del shopping_list[:]
    show_list()

def remove_list_item():
    show_list()
    print('What item would you like to remove')
    new_item = input("> ")
    shopping_list.remove(new_item.title())
    print('Removed ', new_item.title())
    show_list()




def main():
    update_shopping_list()
    show_help()

    while True:
        # ask for new items
        new_item = input("> ").lower()

        # be able to quit the app
        if new_item == 'DONE'.lower():
            break
        elif new_item == 'SHOW'.lower():
            show_list()
            continue
        elif new_item == 'HELP'.lower():
            show_help()
            continue
        elif new_item == 'SAVE'.lower():
            save_shopping_list()
            continue
        elif new_item == 'NEW'.lower():
            shopping_list_new()
            continue
        elif new_item == 'REMOVE'.lower():
            remove_list_item()
            continue
        add_to_list(new_item)

    save_shopping_list()
    show_list()

main()
