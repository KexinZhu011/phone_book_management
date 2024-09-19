""" Implement input validation to ensure that user input 
    is in the correct format (e.g., phone format (###) ###-####)"""
import re

def validate_phone(phone):
    """Validate phone number format (###) ###-####"""
    # Remove leading/trailing spaces and extra spaces inside the phone number
    phone = phone.strip().replace(" ", "")

    # Regular expression to match (###)###-#### or ###-###-####
    pattern = re.compile(r"^(\(\d{3}\)\d{3}-\d{4}|\d{3}-\d{3}-\d{4})$")
    return bool(pattern.match(phone))

def validate_email(email):
    """Validate email format"""
    pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
    return bool(pattern.match(email))

def validate_name(name):
    """Check if the name is alphabetic"""
    return name.isalpha()