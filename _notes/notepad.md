```py
# shopping_list_manager.py
# shopping_list_manager.py

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter the item to add: ").strip()
    shopping_list.append(item)
    print(f"'{item}' has been added to the shopping list.")

def remove_item(shopping_list):
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the shopping list.")
    else:
        print(f"'{item}' was not found in the shopping list.")

def view_list(shopping_list):
    if not shopping_list:
        print("The shopping list is empty.")
    else:
        print("\nCurrent Shopping List:")
        for item in shopping_list:
            print(f"- {item}")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


```

```python

# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in the format "YYYY-MM-DD HH:MM:SS".
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Calculate the future date after adding a specified number of days to the current date.
    """
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date after {days_to_add} days: {formatted_future_date}")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()

```