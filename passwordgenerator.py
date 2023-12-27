import random
import string
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
while True:
    try:
        password_length = int(input("Enter the desired password length: "))
        break
    except ValueError:
        print("Please enter a valid number.")
password = generate_password(password_length)
print(f"Generated Password: {password}")
