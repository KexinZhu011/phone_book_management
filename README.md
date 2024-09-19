# phone_book_management
Python Assignment 1: Advanced Phone Book Management Application

## Overview
This project is an advanced command-line Phone Book Management application written in Python. It allows users to add, view, search, update, and delete contacts. The application supports individual and batch operations (from CSV files) and includes input validation, logging, and sorting/grouping features for better contact management.
![add_a_contact](https://github.com/KexinZhu011/phone_book_management/blob/main/images/add.png)
![add_from_csv](https://github.com/KexinZhu011/phone_book_management/blob/main/images/add_from_csv.png)

## Features

- **CRUD Operations**: Users can create, retrieve, update, and delete contacts.
  - Add contacts individually or in batch mode from CSV files. 
  - Search contacts by name or phone number. Supports fuzzy search. For example, searching for "mo" will return results such as "monica."
  - Update contacts.
  - Delete contacts individually, or in batch mode from CSV files, or in batch mode by phone numbers.
![delete](https://github.com/KexinZhu011/phone_book_management/blob/main/images/delete.png)

- **Input Validation**: Ensures proper format for phone numbers and email addresses.

- **Sorting and Grouping**:
  - Sort contacts by last name (ascending or descending).
  - Group contacts by the initial letter of their last name.
![display_by_desc](https://github.com/KexinZhu011/phone_book_management/blob/main/images/display.png)
- **Logging**: Tracks all actions (add, update, delete) with timestamps for auditing.

- **Error Handling**: 
    - Comprehensive validation to ensure data integrity, including invalid phone numbers or email addresses.
    - Duplicate Check for phone numbers during addition: When adding a new contact, the system checks for duplicate phone numbers to ensure that no two contacts have the same phone number.
    - Flexible Phone Number Input: The system accepts phone numbers even if there are minor format inconsistencies. For example, phone numbers can be saved in the format (###) ###-#### or (###)###-####. 
    - Deletion by Format: When performing bulk deletions based on phone numbers, the system can handle variations such as extra spaces between numbers, commas, or trailing spaces, and will still recognize and process the input correctly.

## Files

### 1. `contact.py`
- Contains the `Contact` class, which represents an individual contact.
- Each contact has the following attributes:
  - `first_name`
  - `last_name`
  - `phone`
  - `email` (optional)
  - `address` (optional)
  - Timestamps for when the contact was created and last updated.

### 2. `phonebook.py`
- Contains the `PhoneBook` class, which manages the CRUD operations for contacts.
  - **add_contact()**: Adds a new contact to the phonebook after validating phone number and email.
  - **update_contact()**: Updates an existing contact by phone number.
  - **delete_contact()**: Deletes a contact by phone number.
  - **import_contacts_from_csv()**: Adds contacts in batch mode from a CSV file.
  - **delete_contacts_from_csv()**: Deletes contacts in batch mode from a CSV file.
  - **delete_contacts_from_input()**: Deletes multiple contacts by entering phone numbers separated by comma.
  - **search_by_name()**: Searches contacts by first or last name, with options for sorting or grouping results.
  - **display_contacts()**: Displays all contacts, with sorting and grouping options if multiple contacts exist.

### 3. `validation.py`
- Contains functions for validating input data:
  - **validate_phone()**: Validates that the phone number follows the format `(###) ###-####`.
  - **validate_email()**: Validates that the email address follows a standard format.
  - **validate_name()**: Checks if the name is alphabetic.

### 4. `logger.py`
- Provides a logging mechanism to track all CRUD operations.
- Logs are stored in `phonebook_log.txt` with timestamps.

### 5. `main.py`
- The main entry point for the application.
- Handles user input for different actions:
  - `add`, `update`, `delete`
  - Batch operations (`batch_add_by_csv`, `batch_delete_by_csv`, `batch_delete_by_phone_numbers`)
  - `search`, `display`, and sorting options.

### 6. `add_data_example.csv`
- Example CSV file for adding contacts in batch mode.

### 7. `delete_data_example.csv`
- Example CSV file for deleting contacts in batch mode.

### 8. `phonebook_log.txt`
- Contains a log of all operations performed, including timestamps and details of each action (e.g., added or deleted contacts).

## Input Validation and Error Handling

- **Phone Validation**: 
    - Phone numbers must follow the format `(###) ###-####` or `(###)###-####`. Invalid phone numbers will be rejected with an error message. 
    - Phone numbers must be unique.
- **Email Validation**: Email addresses are optional but must follow the format `example@domain.com` if provided.
- **Name Validation**: Names are required and must contain only alphabetic characters.

### Example Scenarios

1. **Adding a contact with an invalid phone number**:
   - If the phone number doesn't match the required format, the contact will not be added, and the user will be prompted with an "Invalid phone number" message.

2. **Batch Adding Contacts from a CSV**:
   - Contacts can be added in bulk using a CSV file. Each contact will be validated as file `add_data_example.csv`, and any invalid entries will be skipped with a corresponding message.

3. **Batch Deleting Contacts by Phone Numbers**:
   - You can delete multiple contacts by providing a list of phone numbers, either manually or via a CSV file. Invalid phone numbers or contacts not found will be skipped with a corresponding message.
![delete_by_numbers](https://github.com/KexinZhu011/phone_book_management/blob/main/images/delete_by_numbers.png)

## Running the Application

1. Ensure Python 3.x is installed on your system.
2. Clone this repository:
   ```bash
   git clone https://github.com/KexinZhu011/phone_book_management.git
   cd phone_book_management
   python3 main.py
