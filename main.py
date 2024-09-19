# main.py

from phonebook import PhoneBook
from validation import validate_name

def main():
    phonebook = PhoneBook()

    while True:
        action = input("Choose action: add, update, delete, batch_add_by_csv, batch_delete_by_phone_numbers, batch_delete_by_csv, search, display, quit: ").lower()

        if action == "add":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone = input("Enter phone number (###) ###-####: ")
            email = input("Enter email (optional): ")
            address = input("Enter address (optional): ")
            phonebook.add_contact(first_name, last_name, phone, email, address)

        elif action == 'batch_add_by_csv':
            csv_file = input("Enter CSV file path: ").strip().strip("'\"")
            phonebook.import_contacts_from_csv(csv_file)

        elif action == "update":
            phone = input("Enter phone number of contact to update: ")
            new_first_name = input("Enter new first name (or press Enter to skip): ")
            new_last_name = input("Enter new last name (or press Enter to skip): ")
            new_phone = input("Enter new phone number (###) ###-#### (or press Enter to skip): ")
            email = input("Enter new email (optional): ")
            address = input("Enter new address (optional): ")
            phonebook.update_contact(phone, new_first_name, new_last_name, new_phone, email, address)

        elif action == "delete":
            phone = input("Enter phone number of contact to delete: ")
            phonebook.delete_contact(phone)

        elif action == 'batch_delete_by_csv':
            csv_file = input("Enter CSV file path: ").strip().strip("'\"")
            phonebook.delete_contacts_from_csv(csv_file)

        elif action == 'batch_delete_by_phone_numbers':
            phonebook.delete_contacts_from_input()


        elif action == "search":
            name = input("Enter name to search: ")
            if validate_name(name):
                phonebook.search_by_name(name)
            else:
                print("Invalid name. Please enter alphabetic characters only.")

        elif action == "display":
            phonebook.display_contacts()

        elif action == "quit":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()