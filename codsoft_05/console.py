class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contact_list(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")

    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, contact, new_name, new_phone_number, new_email, new_address):
        contact.name = new_name
        contact.phone_number = new_phone_number
        contact.email = new_email
        contact.address = new_address

    def delete_contact(self, contact):
        self.contacts.remove(contact)

def main():
    contact_book = ContactBook()

    while True:
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)
            print("Contact added successfully!")

        elif choice == "2":
            contact_book.view_contact_list()

        elif choice == "3":
            search_term = input("Enter search term: ")
            found_contacts = contact_book.search_contact(search_term)
            if found_contacts:
                print("Found contacts:")
                for contact in found_contacts:
                    print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")
            else:
                print("No contacts found.")

        elif choice == "4":
            name = input("Enter name of contact to update: ")
            found_contacts = contact_book.search_contact(name)
            if found_contacts:
                contact = found_contacts[0]
                new_name = input("Enter new name: ")
                new_phone_number = input("Enter new phone number: ")
                new_email = input("Enter new email: ")
                new_address = input("Enter new address: ")
                contact_book.update_contact(contact, new_name, new_phone_number, new_email, new_address)
                print("Contact updated successfully!")
            else:
                print("Contact not found.")

        elif choice == "5":
            name = input("Enter name of contact to delete: ")
            found_contacts = contact_book.search_contact(name)
            if found_contacts:
                contact = found_contacts[0]
                contact_book.delete_contact(contact)
                print("Contact deleted successfully!")
            else:
                print("Contact not found.")

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()