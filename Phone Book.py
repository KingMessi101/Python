class PhoneBook:
    def __init__(self):
        self.contacts= {}

    def add_contact(self):
        name = input("Enter Name: ").strip()
        phone = input("Enter Phone Number: ").strip()

        if name in self.contacts:
            print(f"Contact '{name}' already exists. Use update option.\n")
        else:
            self.contacts[name] = phone
            print(f"Contact '{name}' added successfuly!\n")

    def view_contact(self):
        name = input("Enter Name to Search: ").strip()
        if name in self.contacts:
            print(f"\n Contact Found: {name} {self.contacts[name]}\n")
        else:
            print(f"Contact Not Found\n")

    def search_by_number(self):
        phone = input("Enter Phone Number To search: ").strip()
        found = False
        for name, num in self.contacts.items():
            if num == phone:
                print(f"\n Phone Number Belongs To: {name}\n")
                found = True
                break
        if not found:
            print(f"no contact found with this phone number.\n")
    def update_contact(self):
        name = input("Enter Name to Update: ").strip()
        if name in self.contacts:
            new_phone = input("Enter New Phone Number: ").strip()
            self.contacts[name] = new_phone
            print(f"Contact '{name}' updated successfully.\n")
        else:
            print("Contact not found.\n")

    def delete_contacts(self):
        name = input("Enter name to delete: ").strip()
        if name in self.contacts:
            del self.contacts [name]
            print(f"Contact {name} deleted successfully.\n")
        else:
            print("Contact not Found.\n")

    def display_all_contacts(self):
        if self.contacts:
            print("\nAll Contacts:")
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}:")
            print("\n")
        else:
            print("No contacts to display.\n")

def main():
    phonebook = PhoneBook()

    while True:
        print("PhoneBook Menu: ")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Search by phone number")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Display All Contacts")
        print("7. Exit")

        choice = input("Choose an Option: ").strip()

        if choice == "1":
            phonebook.add_contact()
        elif choice == "2":
            phonebook. view_contact()
        elif choice == "3":
            phonebook. search_by_number()
        elif choice == "4":
            phonebook. update_contact()
        elif choice == "5":
            phonebook. delete_contacts()
        elif choice == "6":
            phonebook. display_all_contacts()
        elif choice == "7":
            print("Exiting Phone Book Application...")
        else:
            print("Invalid Option. Please Try Again")
        
if __name__ == "__main__":
    main()