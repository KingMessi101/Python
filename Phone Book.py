class PhoneBook:
    def _init_(self):
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