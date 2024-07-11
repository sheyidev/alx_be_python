## Allow users to create a simple shopping list manager 
# that allows users to add items,view the current list, and remove items
shopping_list = []

def display_menu():
   print("Shopping List Manager")
   print("1. Add Item")
   print("2. Remove Item")
   print("3. View List")
   print("4. Exit")

def add_item(shopping_list):
   item = input("Enter the item to add: ")
   shopping_list.append(item)
   print(f"Your {item} has been added to the shopping list")

def remove_item(shopping_list):
   item = input("Enter your choice: ") 
   if item in shopping_list:
      shopping_list.remove(item)
      print(f"Your {item} has been removed from the shopping list")
   else :
      print(f"Item is not found")
def list_item(shopping_list):
   if not item:
      print("Item does not exist")
   for item in shopping_list:
      print(item)
