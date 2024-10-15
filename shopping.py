shopping_list = []

def add(item):
    global shopping_list
    shopping_list.append(item)
def remove(item):
    global shopping_list
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print(f"{item} is not currently on the shopping list.")
def display():
    global shopping_list
    for i in range(len(shopping_list)):
        print(f"Item {i} is {shopping_list[i]}.")

while True:
    action = input("[A]dd an item, [R]emove an item, [D]isplay shopping list, or [Q]uit?")
    if action == 'A':
        item = input("Name of the item to add?")
        add(item)
    elif action == 'R':
        item = input("Name of the item to remove?")
        remove(item)
    elif action == 'D':
        display()
    elif action == 'Q':
        break
    else:
        print("That is not a valid option")