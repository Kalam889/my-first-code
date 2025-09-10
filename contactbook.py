contacts = {}
while True:
    print("\n contact book: ")
    print("1. Create contact: ")
    print("2. Search contact: ")
    print("3. Update contact: ")
    print("4. Delete contact: ")
    print("5. View all contact: ")
    print("6. Exit: ")
    
    choice =input("Enter your choice(1-6): ")
    if choice == "1":
        name =input("Enter your name: ")
        phone =input("Enter your number: ")
        mail =input("Enter your mail: ")
        contacts[name]={"Phone": phone, "Mail": mail}
        print(f"{name}, has been added to your contact.")
    elif choice == "2":
        search_name =input("Enter name to search: ")
        if search_name in contacts:
            print(f'Phone:{contacts[search_name]["Phone"]} ')
            print(f'Mail:{contacts[search_name]["Mail"]} ')
    elif choice == "3":
        update_name =input("Enter name to update: ")
        if update_name in contacts:
            phone =input("Enter your updated number: ")
            mail =input("Enter your updated mail: ")
            contacts[update_name] ={"Phone":phone, "Mail":mail}
        else:
            print("Contact not found")
    
    elif choice == "4":
        name_to_delete =input("Enter name to delete: ")
        if name_to_delete in contacts:
            del contacts [name_to_delete]
            print(f"{name_to_delete} has been deleted. ")
        else:
            print("Contact not found.")
    elif choice == "5":
        if contacts:
            for name, info in contacts.items():
                print(f"\nName: {name}")
                print(f"Phone: {info['Phone']}")
                print(f"Mail: {info['Mail']}")
        else:
            print("No contacts to display.")
    elif choice == "6":
        print("Goodbye")
        break



