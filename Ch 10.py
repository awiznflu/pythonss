# from pathlib import Path
#
# path = Path('pi_digits.txt')
# contents = path.read_text()
#
# for line in contents.splitlines():
#     print(line)

# Open the file in append mode so that entries are added to the file without overwriting it
with open('guest_book.txt', 'a') as file:
    while True:
        # Prompt the user for their name
        name = input("Please enter your name (or type 'quit' to stop): ")

        # Check if the user wants to quit
        if name.lower() == 'quit':
            break

        # Write the name to the file, followed by a new line
        file.write(name + '\n')

print("Thank you for signing the guest book!")

try:
    # Try reading the contents of the cats.txt file
    with open('cats.txt') as cat_file:
        print("Cat names:")
        for line in cat_file:
            print(line.strip())

    # Try reading the contents of the dogs.txt file
    with open('dogs.txt') as dog_file:
        print("\nDog names:")
        for line in dog_file:
            print(line.strip())

except FileNotFoundError:
    # Fail silently: no error message will be printed
    pass

from pathlib import Path
import json


def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)

    if username:
        # Ask the user if the stored username is correct
        correct_username = input(f"Welcome back, {username}! Is this the correct username? (yes/no) ").lower()
        if correct_username != 'yes':
            username = get_new_username(path)
            print(f"We'll remember you when you come back, {username}!")
        else:
            print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")


greet_user()
