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
        choice = input("Enter your choice (1-4): ")
        
        # Check if the choice is a digit and within the valid range
        if choice.isdigit() and 1 <= int(choice) <= 4:
            choice = int(choice)
            
            if choice == 1:
                addedItem = input("Enter the item to add: ")
                shopping_list.append(addedItem)
            elif choice == 2:
                removedItem = input("Enter the item to remove: ")
                if removedItem in shopping_list:
                    shopping_list.remove(removedItem)
                else:
                    print("Item doesn't exist in the list.")
            elif choice == 3:
                if shopping_list:
                    print("Current Shopping List:")
                    for item in shopping_list:
                        print(f"- {item}")
                else:
                    print("The shopping list is empty.")
            elif choice == 4:
                print("Goodbye!")
                break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
