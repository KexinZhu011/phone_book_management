"""Log the action taken on the phonebook"""

from datetime import datetime

def log_action(action):
    """Log the action taken on the phonebook"""
    with open("phonebook_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()} - {action}\n")