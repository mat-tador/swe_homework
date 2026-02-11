 
def password_strength(password: str) -> str: 

    if type(password) != str: 
        raise TypeError
    
    has_letters = any(c.isalpha() for c in password)
    has_numbers = any(c.isnumeric() for c in password)
    has_symbols = not password.isalnum()

    
    
    if len(password) >= 12 and has_letters and has_numbers and has_symbols:
        return "strong"
    elif len(password) >= 8 and has_letters and has_numbers: 
        return "medium"
    else: 
        return "weak"