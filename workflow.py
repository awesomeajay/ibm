import random
import string

length = 12

characters = string.ascii_letters + string.digits + "!@#$%^&*"
password = ''.join(random.choice(characters) for _ in range(length))

print("Generated Password:", password)