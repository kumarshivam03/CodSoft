contacts = []

def add_contact():
    contacts.append({
        "Name": input("Name: "),
        "Phone": input("Phone: "),
        "Email": input("Email: "),
        "Address": input("Address: ")
    })
    print("Contact added.")

def view_contact_list():
    if not contacts:
        print("No contacts.")
    else:
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['Name']}, {contact['Phone']}")

def search_contact(query):
    results = [c for c in contacts if query in c['Name'] or query in c['Phone']]
    return results

def update_contact():
    view_contact_list()
    try:
        index = int(input("Index to update: ")) - 1
        if 0 <= index < len(contacts):
            c = contacts[index]
            c.update({
                "Name": input(f"Updated Name ({c['Name']}): ") or c['Name'],
                "Phone": input(f"Updated Phone ({c['Phone']}): ") or c['Phone'],
                "Email": input(f"Updated Email ({c['Email']}): ") or c['Email'],
                "Address": input(f"Updated Address ({c['Address']}): ") or c['Address']
            })
            print("Contact updated.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")

def delete_contact():
    view_contact_list()
    try:
        index = int(input("Index to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted_contact = contacts.pop(index)
            print(f"Contact '{deleted_contact['Name']}' deleted.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact_list()
        elif choice == "3":
            query = input("Search by name or phone: ")
            results = search_contact(query)
            [print(f"{c['Name']}, {c['Phone']}") for c in results] if results else print("No matching contacts.")
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
