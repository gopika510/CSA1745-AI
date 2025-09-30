def create_list():
    """Creates and returns a base list."""
    return ["apple", "banana", "cherry"]

def show_list(lst):
    print("\nCurrent List:", lst)

def add_item(lst):
    """Insert at a specific index."""
    item = input("Enter item to insert: ")
    try:
        index = int(input("Enter index to insert at: "))
        lst.insert(index, item)
        print("Item inserted successfully!")
    except:
        print("Invalid index! Item not added.")

def append_item(lst):
    """Append an item at the end."""
    item = input("Enter item to append: ")
    lst.append(item)
    print("Item appended successfully!")

def extend_list(lst):
    """Extend list with multiple items."""
    items = input("Enter items to extend (comma-separated): ").split(",")
    items = [x.strip() for x in items]
    lst.extend(items)
    print("List extended successfully!")

def delete_item(lst):
    """Delete by value or index."""
    print("\nDelete Options:")
    print("1. Delete by Value")
    print("2. Delete by Index")
    option = input("Enter choice (1/2): ")

    if option == '1':
        item = input("Enter item to remove: ")
        if item in lst:
            lst.remove(item)
            print("Item removed successfully!")
        else:
            print("Item not found in list!")
    elif option == '2':
        try:
            index = int(input("Enter index to delete: "))
            del lst[index]
            print("Item deleted successfully!")
        except:
            print("Invalid index!")
    else:
        print("Invalid option!")

def main():
    my_list = create_list()
    
    while True:
        print("\n========== LIST METHODS MENU ==========")
        print("1. Show List")
        print("2. Add (Insert)")
        print("3. Append")
        print("4. Extend")
        print("5. Delete")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            show_list(my_list)
        elif choice == '2':
            add_item(my_list)
        elif choice == '3':
            append_item(my_list)
        elif choice == '4':
            extend_list(my_list)
        elif choice == '5':
            delete_item(my_list)
        elif choice == '6':
            print("\nExiting Program. Thank you!")
            break
        else:
            print("\nInvalid choice! Enter a number between 1 and 6.")

# Run the program
if _name_ == "_main_":
    main()
