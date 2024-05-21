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
        print("Contact added successfully!")

    def view_contacts(self):
        if self.contacts:
            print("\n--- Contact List ---")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. Name: {contact.name}, Phone: {contact.phone_number}")
        else:
            print("Contact List is empty.")

    def search_contact(self, search_query):
        found_contacts = []
        for contact in self.contacts:
            if search_query.lower() in contact.name.lower() or search_query in contact.phone_number:
                found_contacts.append(contact)
        if found_contacts:
            print("\n--- Search Results ---")
            for i, contact in enumerate(found_contacts, start=1):
                print(f"{i}. Name: {contact.name}, Phone: {contact.phone_number}")
        else:
            print("No contacts found matching the search query.")

    def update_contact(self, old_name, new_contact):
        for contact in self.contacts:
            if contact.name.lower() == old_name.lower():
                contact.name = new_contact.name
                contact.phone_number = new_contact.phone_number
                contact.email = new_contact.email
                contact.address = new_contact.address
                print("Contact updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self, contact_name):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == contact_name.lower():
                del self.contacts[i]
                print("Contact deleted successfully!")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()
    
    print("Welcome to the Contact Book App!")
    
    while True:
        print("\n--- MENU ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5/6): ")
        
        if choice == '1':
            print("\n--- Add Contact ---")
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)
        elif choice == '2':
            print("\n--- View Contacts ---")
            contact_book.view_contacts()
        elif choice == '3':
            print("\n--- Search Contact ---")
            search_query = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_query)
        elif choice == '4':
            print("\n--- Update Contact ---")
            old_name = input("Enter the name of the contact to update: ")
            new_name = input("Enter new name: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            new_contact = Contact(new_name, new_phone_number, new_email, new_address)
            contact_book.update_contact(old_name, new_contact)
        elif choice == '5':
            print("\n--- Delete Contact ---")
            contact_name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(contact_name)
        elif choice == '6':
            print("Exiting the Contact Book application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
