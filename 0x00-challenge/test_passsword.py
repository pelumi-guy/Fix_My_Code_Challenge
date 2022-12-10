from sys import argv

User = __import__('3-user').User

newUser = User()

newUser.password = 'galactic'

password = argv[1]

print(f"{password} is valid: {newUser.is_valid_password(password)}")

