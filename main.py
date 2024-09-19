# main.py

from phonebook import PhoneBook
from validation import validate_name

def main():
    phonebook = PhoneBook()

    while True:
        # Print the user interface with numbered options
        print("\n=========================================")
        print("       Welcome to PhoneBook Manager")
        print("=========================================")
        print("Please choose an action:")
        print("1. Add a new contact")
        print("2. Update an existing contact")
        print("3. Delete a contact by phone number")
        print("4. Batch add contacts from CSV file")
        print("5. Batch delete contacts by phone numbers")
        print("6. Batch delete contacts from CSV file")
        print("7. Search for a contact by name")
        print("8. Display all contacts")
        print("9. Quit")
        print("=========================================")
        # action = input("Choose action: add, update, delete, batch_add_by_csv, batch_delete_by_phone_numbers, batch_delete_by_csv, search, display, quit: ").lower()
        
        # Get user input for action
        try:
            action = int(input("Enter the number corresponding to your action: ").strip())
        except ValueError:
            print("\nInvalid input! Please enter a number between 1 and 9.")
            continue
        
        print("\n-----------------------------------------")
        
        # Map user input to actions
        # Add a new contact
        if action == 1:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone = input("Enter phone number (###) ###-####: ")
            email = input("Enter email (optional): ")
            address = input("Enter address (optional): ")
            phonebook.add_contact(first_name, last_name, phone, email, address)

        # Batch add contacts from CSV file
        elif action == 4:
            csv_file = input("Enter CSV file path: ").strip().strip("'\"")
            phonebook.import_contacts_from_csv(csv_file)

        # Update an existing contact
        elif action == 2:
            phone = input("Enter phone number of contact to update: ")
            new_first_name = input("Enter new first name (or press Enter to skip): ")
            new_last_name = input("Enter new last name (or press Enter to skip): ")
            new_phone = input("Enter new phone number (###) ###-#### (or press Enter to skip): ")
            email = input("Enter new email (optional): ")
            address = input("Enter new address (optional): ")
            phonebook.update_contact(phone, new_first_name, new_last_name, new_phone, email, address)

        # Delete a contact by phone number
        elif action == 3:
            phone = input("Enter phone number of contact to delete: ")
            phonebook.delete_contact(phone)

        # Batch delete contacts from CSV file
        elif action == 6:
            csv_file = input("Enter CSV file path: ").strip().strip("'\"")
            phonebook.delete_contacts_from_csv(csv_file)
        
        # Batch delete contacts by phone numbers
        elif action == 5:
            phonebook.delete_contacts_from_input()

        # Search for a contact by name
        elif action == 7:
            name = input("Enter name to search: ")
            if validate_name(name):
                phonebook.search_by_name(name)
            else:
                print("Invalid name. Please enter alphabetic characters only.")

        # Display all contacts
        elif action == 8:
            phonebook.display_contacts()

        # Quit the application
        elif action == 9:
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice! Please choose a valid option from 1 to 9.")

if __name__ == "__main__":
    main()