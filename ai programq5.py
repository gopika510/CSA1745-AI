def create_list():
    """Creates and returns a base list with a nested list."""
    return ["apple", "banana", "cherry", ["mango", "orange"]]

def show_original(lst):
    print("\nOriginal List:", lst)

def list_length(lst):
    print("\nLength of the list:", len(lst))

def concatenate_list(lst):
    extra = ["grape", "kiwi"]
    new_list = lst + extra
    print("\nAfter Concatenation:", new_list)

def check_membership(lst):
    item = input("\nEnter an item to check membership: ")
    print(f"Membership ({item} in list):", item in lst)

def iterate_list(lst):
    print("\nIterating through list:")
    for item in lst:
        print(item)

def indexing_list(lst):
    try:
        index = int(input("\nEnter index to retrieve element: "))
        print(f"Element at index {index}:", lst[index])
    except:
        print("Invalid index!")

def slicing_list(lst):
    print("\nSlicing (index 1 to 3):", lst[1:4])

def main():
    my_list = create_list()
    
    while True:
        print("\n========== LIST OPERATIONS MENU ==========")
        print("1. Show Original List")
        print("2. Find Length")
        print("3. Concatenate List")
        print("4. Check Membership")
        print("5. Iterate List")
        print("6. Indexing")
        print("7. Slicing")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            show_original(my_list)
        elif choice == '2':
            list_length(my_list)
        elif choice == '3':
            concatenate_list(my_list)
        elif choice == '4':
            check_membership(my_list)
        elif choice == '5':
            iterate_list(my_list)
        elif choice == '6':
            indexing_list(my_list)
        elif choice == '7':
            slicing_list(my_list)
        elif choice == '8':
            print("\nExiting Program. Thank you!")
            break
        else:
            print("\nInvalid choice! Enter a number between 1 and 8.")

# Run the program
if _name_ == "_main_":
    main()
