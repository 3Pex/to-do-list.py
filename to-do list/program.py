"""
Display list
Add list
Remove list
"""

list = []

def addList():
    add_item = str(input("What would you like to add?: "))
    list.append(add_item)

def viewList():
    for index, i in enumerate(list, start=1):
        print(f"{index}. {i}")

def removeList():
    viewList()
    delete_item = int(input("Which task would you like to delete?: "))
    delete_item -= 1

    if delete_item < len(list):
        removed_task = list.pop(delete_item)
        print(f"{removed_task} has been removed")
    

while True:
    option = int(input("\nWhat would you like to do?: \n (1: Add Task) \n (2: Remove Task) \n (3: View List) \n (4: Quit)"))
    if option == 1:
        addList()
    elif option == 2:
        removeList()
    elif option == 3:
        viewList()
    else:
        break
