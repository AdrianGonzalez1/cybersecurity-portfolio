# A pretend "target password" we're trying to guess
target_password = "password123"

# A list of common passwords
common_passwords = [
    "123456",
    "password",
    "12345678",
    "qwerty",
    "abc123",
    "admin",
    "welcome",
    "iloveyou",
    "monkey"
]

# A list to hold the guesses we're going to try
guesses = []

# Create some simple variations of each password
for password in common_passwords:
    guesses.append(password)               # the original
    guesses.append(password.capitalize())  # first letter uppercase
    guesses.append(password.upper())       # all uppercase
    guesses.append(password[::-1])         # reversed
    guesses.append(password + "123")       # add numbers
    guesses.append("123" + password)       # numbers before
    guesses.append(password + "!")         # add symbol
    guesses.append(password + "@2024")     # add year

# Start trying each guess
print("Trying to crack the password...\n")

attempts = 0  # count how many guesses we try

for guess in guesses:
    attempts += 1
    print("Trying:", guess)
    
    if guess == target_password:
        print("\n✅ Password found:", guess)
        print("🔁 Total attempts:", attempts)
        break
else:
    print("\n❌ Password not found in the list.")
