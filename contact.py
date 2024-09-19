# personal information (name, phone number, address, etc.)
from datetime import datetime

class Contact:
    def __init__(self, first_name, last_name, phone, email=None, address=None):
        """Initialize the contact with essential information"""
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.address = address
        self.created_at = datetime.now()  # Record the creation time
        self.updated_at = datetime.now()  # Record the last update time

    def update(self, first_name=None, last_name=None, phone=None, email=None, address=None):
        """Update contact details and record update time"""
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if phone:
            self.phone = phone
        if email:
            self.email = email
        if address:
            self.address = address
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the contact"""
        return f"Name: {self.first_name} {self.last_name}, Phone: {self.phone}, Email: {self.email or 'N/A'}, Address: {self.address or 'N/A'}, Created: {self.created_at}, Updated: {self.updated_at}"