my_list = []
while True:
 print("\n--- List Operations Menu ---")
 print("1. Insert an element")
 print("2. Remove an element")
 print("3. Append an element")
 print("4. Display length of the list")
 print("5. Pop an element")
 print("6. Clear the list")
 print("7. Display the list")
 print("8. Exit")
 choice = int(input("Enter your choice (1-8): "))
 if choice == 1:
  pos= int(input("Enter position to insert: "))
 element = input("Enter element to insert: ")
 my_list.insert(pos, element)
 print("Element inserted successfully.")
elif choice == 2:
   element = input("Enter element to remove: ")
    if element in my_list:
    my_list.remove(element)
    print("Element removed successfully.")
    else:
    print("Element not found in list.")
 elif choice == 3:
 element = input("Enter element to append: ")
 my_list.append(element)
 print("Element appended successfully.")
 elif choice == 4:
 print(f"Length of the list: {len(my_list)}")
 elif choice == 5:
 if my_list:
 popped = my_list.pop()
 print(f"Popped element: {popped}")
 else:
 print("List is empty.")
 elif choice == 6:
 my_list.clear()
 print("List cleared successfully.")
 elif choice == 7:
 print("Current List:", my_list)
 elif choice == 8:
 print("Exiting program...")
 break