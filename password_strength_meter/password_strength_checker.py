def password_strength(password):
    pass_score = 0

    if len(password) >= 8: # Conditional to check the length of pass
        pass_score += 1 # Increments password strength score

    has_upper = False # Flag to track if theres uppercase char
    has_lower = False # Flag to track if theres lowercase char

    for char in password: # Loops through each character in the passowrd string 
        if char.isupper(): # Conditional to check if there are uppercase characters
            has_upper = True # If there are uppercase sets value to True
        if char.islower(): # Conditional to check if there are lowercase characters
            has_lower = True # If there are lowercase sets value to True
        if has_upper and has_lower:
            break # Exit loop earl if both conditions are met

    # Increments the password strength score if conditions are met
    if has_upper and has_lower: 
            pass_score += 1
    
    has_digit = False # Flag to track if there is a digit in the password string

    # Loops through each char in search of a digit
    for char in password:
        if char.isdigit():
            has_digit = True # Sets flag value to true if digit is found
            break # Only breaks if a digit is found 
    
    if has_digit:
        pass_score += 1

    has_special = False # Flag to track if there is a special char in the password string

    # Loops through each char in search of special char
    for char in password:
        if char.isalnum():
            has_special = True # Sets flag value to true if special char is found
            break
    if has_special:
        pass_score += 1
     # Prints the final password strength score       
    print("Password stength score:", pass_score) 

    if pass_score <= 1:
        print("Password strength: Weak")
    elif pass_score <= 3:
        print("Password Strength: Moderate")
    else:
        print("Password Strength: Strong")

# Asks user to input a password
password = input("Please enter your password: ")
password_strength(password)