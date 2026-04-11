import hashlib

# Store hashed password
stored_password = hashlib.sha256("Mysecure123!".encode()).hexdigest()

def login(user_input):
    hashed_input = hashlib.sha256(user_input.encode()).hexdigest()

    if hashed_input == stored_password:
        print("Access granted ✅")
    else:
        print("Access denied ❌")

password = input("Enter password: ")
login(password)
