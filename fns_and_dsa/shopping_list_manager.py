def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            addedItem =input("Enter the item to add:")
            shopping_list.append(addedItem)
            # Prompt for and add an item
            pass
        elif choice == 2:
            removedItem =input("Item you want to remove ?")
            if removedItem in shopping_list:
                shopping_list.remove(removedItem)
            else: 
                print("Item doesn't exist in cart")
            # Prompt for and remove an item
            pass
        elif choice == 3:
            for item in shopping_list:
                print(item +" ,", end="")
            # Display the shopping list
            pass
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()