import re

def check_phone(phone):
    pattern = r'^(\+91\s?)?[6-9]\d{9}$'
    if re.match(pattern, phone):
        return True
    return False
