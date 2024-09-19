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
        """Display all contacts in the phonebook"""
        if self.contacts:
            for contact in self.contacts:
                print(contact)
        else:
            print("No contacts found.")

    def search_by_name(self, name):
        """Search contacts by name (first or last name)"""
        results = [contact for contact in self.contacts if name.lower() in contact.first_name.lower() or name.lower() in contact.last_name.lower()]
        if results:
            for contact in results:
                print(contact)
        else:
            print(f"No contacts found for name: {name}.")

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