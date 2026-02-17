contacts = {}

while True:
    print("\n1. Add Contact\n2. Search Contact\n3. Update Contact\n4. Delete Contact\n5. Display All Contacts\n6. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added.")

    elif choice == 2:
        name = input("Enter name to search: ")
        if name in contacts:
            print("Phone number:", contacts[name])
        else:
            print("Contact not found.")

    elif choice == 3:
        name = input("Enter name to update: ")
        if name in contacts:
            phone = input("Enter new phone number: ")
            contacts[name] = phone
            print("Contact updated.")
        else:
            print("Contact not found.")

    elif choice == 4:
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == 5:
        if contacts:
            print("All contacts:")
            for name, phone in contacts.items():
                print(name, ":", phone)
        else:
            print("No contacts found.")

    elif choice == 6:
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
