# make a list to hold onto our items
shopping_list = []

# print out instructions on how to use the app
done_help = 'Enter "DONE" to stop adding items.'
show_help = 'Enter "SHOW" to view the items on your list so far'
help_help = 'Enter "HELP" at any time to view this information again'

print('What should we pick up at the store?')
print(done_help)
print(show_help)
print(help_help)


while True:
    # ask for new items
    new_item = input("> ")

    # be able to quit the app
    if new_item == 'DONE':
        break
    elif new_item == 'SHOW':
        print('So far we have: ')

        for item in shopping_list:
            print(item)
    elif new_item == 'HELP':
        print(done_help)
        print(show_help)
        print(help_help)

    # add new items to our list
    shopping_list.append(new_item)

# print out the list
print ("Heres your list!")

for item in shopping_list:
    print(item)
