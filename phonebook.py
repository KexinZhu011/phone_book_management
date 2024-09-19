# CRUD operations of the contact

from contact import Contact
from validation import validate_phone, validate_email
from logger import log_action
import csv

class PhoneBook:
    def __init__(self):
        """Initialize the PhoneBook with an empty contact list"""
        self.contacts = []
    
    def add_contact(self, first_name, last_name, phone, email=None, address=None):
        """Add a new contact to the phonebook after validation and checking for duplicates"""
        
        # Check if phone number is valid and email (if provided) is valid
        if validate_phone(phone) and (not email or validate_email(email)):
            
            # Check if the contact already exists by phone number
            if self.search_by_phone(phone):
                print(f"Failed to add. Contact with phone number {phone} already exists.")
            else:
                # If not found, add the new contact
                contact = Contact(first_name, last_name, phone, email, address)
                self.contacts.append(contact)
                log_action(f"Added contact: {contact}")
                print(f"Log action: Added contact {contact}")
                print(f"Contact for {first_name} {last_name} added.")
        
        # If validation fails, provide detailed feedback
        else:
            if not validate_phone(phone):
                print("Invalid phone number.")
            elif email and not validate_email(email):
                print("Invalid email.")    

    def update_contact(self, phone, first_name=None, last_name=None, new_phone=None, email=None, address=None):
        """Update an existing contact"""
        contact = self.search_by_phone(phone)
        if contact:
            if first_name:
                contact.first_name = first_name
            if last_name:
                contact.last_name = last_name
            if new_phone:
                if validate_phone(new_phone):
                    contact.phone = new_phone
                else:
                    print("Invalid new phone number.")
                    return
            if email:
                if validate_email(email):
                    contact.email = email
                else:
                    print("Invalid new email.")
                    return
            if address:
                contact.address = address
            log_action(f"Updated contact: {contact}")
            print(f"Contact for {contact.first_name} {contact.last_name} updated.")
        else:
            print("No contact found with the provided phone number.")

    def delete_contact(self, phone):
        """Delete a contact from the phonebook by phone number"""
        contact = self.search_by_phone(phone)
        if contact:
            self.contacts.remove(contact)
            log_action(f"Deleted contact: {contact}")
            print(f"Contact for {contact.first_name} {contact.last_name} deleted.")
        else:
            print("No contact found with the provided phone number.")

    def search_by_phone(self, phone):
        """Search for a contact by phone number"""
        for contact in self.contacts:
            if contact.phone == phone:
                return contact
        return None

    def display_contacts(self):
        """Display all contacts in the phonebook, with optional sorting if multiple contacts exist."""
        if not self.contacts:
            print("No contacts found.")
            return

        # First, display the contacts as they are
        for contact in self.contacts:
            print(contact)

        # If there are multiple contacts, prompt user for further action
        if len(self.contacts) > 1:
            option = input("Would you like to sort by last name? (asc/desc/none): ").lower()

            if option == 'asc':
                sorted_contacts = sorted(self.contacts, key=lambda contact: contact.last_name)
                print("\nSorted contacts in ascending order by last name:")
                for contact in sorted_contacts:
                    print(contact)

            elif option == 'desc':
                sorted_contacts = sorted(self.contacts, key=lambda contact: contact.last_name, reverse=True)
                print("\nSorted contacts in descending order by last name:")
                for contact in sorted_contacts:
                    print(contact)

            else:
                print("No further sorting applied.")


    def search_by_name(self, name):
        """Search contacts by name (first or last name), with sorting options if multiple results are found."""
        results = [contact for contact in self.contacts if name.lower() in contact.first_name.lower() or name.lower() in contact.last_name.lower()]
        
        if not results:
            print(f"No contacts found for name: {name}.")
            return

        # First, display the search results as they are
        for contact in results:
            print(contact)

        # If multiple results are found, prompt the user for further action
        if len(results) > 1:
            option = input("Multiple contacts found. Would you like to sort by last name? (asc/desc/none): ").lower()

            if option == 'asc':
                results = sorted(results, key=lambda contact: contact.last_name)
                print("\nSorted search results in ascending order by last name:")
                for contact in results:
                    print(contact)

            elif option == 'desc':
                results = sorted(results, key=lambda contact: contact.last_name, reverse=True)
                print("\nSorted search results in descending order by last name:")
                for contact in results:
                    print(contact)

            else:
                print("No further sorting applied.")


    def group_contacts_by_last_name(self):
        """Group contacts by the initial letter of the last name"""
        if not self.contacts:
            print("No contacts found.")
            return

        # Create a dictionary to group contacts by the initial of the last name
        grouped_contacts = {}
        for contact in self.contacts:
            initial = contact.last_name[0].upper()  # Get the first letter of the last name
            if initial not in grouped_contacts:
                grouped_contacts[initial] = []
            grouped_contacts[initial].append(contact)

        # Display the grouped contacts
        for initial, contacts in sorted(grouped_contacts.items()):
            print(f"\nContacts starting with '{initial}':")
            for contact in contacts:
                print(contact)


    # add batch
    def import_contacts_from_csv(self, csv_file):
        """Import contacts from a CSV file"""
        try:
            with open(csv_file, newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if validate_phone(row['phone']) and (not row['email'] or validate_email(row['email'])):
                        contact = Contact(
                            first_name=row['first_name'],
                            last_name=row['last_name'],
                            phone=row['phone'],
                            email=row.get('email'),
                            address=row.get('address')
                        )
                        # Check for duplicates before adding
                        if not self.search_by_phone(row['phone']):
                            self.contacts.append(contact)
                            log_action(f"Added contact: {contact}")
                            print(f"Contact {row['first_name']} {row['last_name']} added from CSV.")
                        else:
                            print(f"Duplicate contact with phone number {row['phone']} found. Skipping.")
                    else:
                        print(f"Invalid phone number or email for {row['first_name']} {row['last_name']}. Skipping.")
        except FileNotFoundError:
            print(f"File {csv_file} not found.")
        except Exception as e:
            print(f"Error occurred while importing contacts: {e}")

    # batch delete by csv
    def delete_contacts_from_csv(self, csv_file):
        """Delete multiple contacts from a CSV file by phone numbers"""
        try:
            with open(csv_file, newline='') as file:
                reader = csv.DictReader(file)
                phones_to_delete = []
                for row in reader:
                    # Ensure the 'phone' column exists in the CSV file
                    phone = row.get('phone')
                    if phone:
                        phones_to_delete.append(phone.strip())
                    else:
                        print("Missing 'phone' field in CSV.")
                
                # Now delete the contacts based on the collected phone numbers
                self.delete_contacts(phones_to_delete)

        except FileNotFoundError:
            print(f"File {csv_file} not found.")
        except Exception as e:
            print(f"Error occurred while deleting contacts: {e}")

    # batch delete by entering phone numbers
    def delete_contacts_from_input(self):
        """Allow user to delete multiple contacts by phone numbers input"""
        phones_input = input("Enter phone numbers to delete (separated by commas): ")
        # Split input by commas, strip each phone, and filter out empty strings
        phones = [phone.strip() for phone in phones_input.split(',') if phone.strip()]
        if phones:
            self.delete_contacts(phones)
        else:
            print("No valid phone numbers entered or extra commas detected.")

    def delete_contacts(self, phones):
        """Delete multiple contacts from the phonebook by phone numbers"""
        for phone in phones:
            contact = self.search_by_phone(phone)
            if contact:
                self.contacts.remove(contact)
                log_action(f"Deleted contact: {contact}")
                print(f"Contact for {contact.first_name} {contact.last_name} deleted.")
            else:
                print(f"No contact found with phone number {phone}.")