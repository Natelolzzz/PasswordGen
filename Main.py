import random
import string

def generate_password():
  # Create a list of possible characters for the password
  chars = string.ascii_letters + string.digits + string.punctuation

  # Generate a random password of length 20
  password = "".join(random.choice(chars) for _ in range(20))

  return password

print(generate_password())
