import random
import string

def generate_password(length=12):
    
    all_characters = string.ascii_letters + string.digits 
    
    password = "".join(random.choice(all_characters) for _ in range(length))
    return password

print("Your secure new password is:", generate_password(16))

