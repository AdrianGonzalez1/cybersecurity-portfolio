import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))  # Proper parentheses
    
    return password  # Correct indentation

# Test the function
print(generate_password())   # Default length (8)
print(generate_password(12)) # Custom length (12)
