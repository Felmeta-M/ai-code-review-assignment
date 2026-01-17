import re

def count_valid_emails(emails):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    count = 0
    
    for email in emails:
        if isinstance(email, str) and re.match(pattern, email):
            count += 1
    
    return count
