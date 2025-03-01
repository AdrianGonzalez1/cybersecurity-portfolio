import hashlib #imports hashlib module at the top of the file
def hash_password(password): 
    password_bytes = password.encode() #Convert the string to bytes
    hash_pass = hashlib.sha256(password_bytes) #Create the hash using SHA-256
    hex_pass = hash_pass.hexdigest() #Converts hash into a readable format
    return hex_pass

#Example usage
password= input("Enter a password: ")
hashed = hash_password(password) #Call the function
print("SHA-256 Hashed Password:", hashed) #Print the result