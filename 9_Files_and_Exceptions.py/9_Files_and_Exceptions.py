#Exercise 01
from pathlib import Path

# Create a Path object
path = Path("learning_python.txt")

# -------------------------------
# Read the entire file at once
# -------------------------------
print("Reading the entire file:\n")

contents = path.read_text()
print(contents)

# -------------------------------
# Read the file into a list
# -------------------------------
print("\nReading the file line by line:\n")

lines = path.read_text().splitlines()

for line in lines:
    print(line)



#Exercise 02
from pathlib import Path

filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    path = Path(filename)

    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file '{filename}' does not exist.")
    else:
        print(f"\nContents of {filename}:")
        print(contents)



#Exercise 03
from pathlib import Path

# Create a Path object
path = Path("learning_python.txt")

# Read the file into a list of lines
lines = path.read_text().splitlines()

# Replace 'Python' with 'C' and print each line
for line in lines:
    modified_line = line.replace("Python", "C")
    print(modified_line)


#Exercise 04
#Original code (with temporary variable)
from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text()

lines = contents.splitlines()

for line in lines:
    print(line)    

#Simplified code (without the temporary variable)
from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text()

for line in contents.splitlines():
    print(line)

#Another example (Replacing "Python" with "C")        
from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text()

lines = contents.splitlines()

for line in lines:
    print(line.replace("Python", "C"))


#Exercise 05
from pathlib import Path

# Ask the user for their name
name = input("What is your name? ")

# Create a Path object
path = Path("guest.txt")

# Write the name to the file
path.write_text(name)

print(f"Hello, {name}! Your name has been saved to guest.txt.")


#Exercise 06
from pathlib import Path

# Create a Path object
path = Path("guest_book.txt")

while True:
    name = input("Enter your name (or 'q' to quit): ")

    if name.lower() == "q":
        break

    # Add the name to the file on a new line
    with path.open("a") as file:
        file.write(name + "\n")

    print(f"Welcome, {name}! Your name has been added to the guest book.")


#Exercise 07
while True:
    try:
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))

    except ValueError:
        print("Sorry! You must enter numbers only.\n")

    else:
        answer = first_number + second_number
        print(f"The sum is: {answer}")
        break    

#Exercise 08
while True:
    try:
        first_number = input("Enter the first number (or 'q' to quit): ")

        if first_number.lower() == "q":
            break

        second_number = input("Enter the second number (or 'q' to quit): ")

        if second_number.lower() == "q":
            break

        first_number = int(first_number)
        second_number = int(second_number)

    except ValueError:
        print("Sorry! Please enter valid numbers.\n")

    else:
        answer = first_number + second_number
        print(f"The sum is: {answer}\n")


#Exercise 09
from pathlib import Path

files = ["cats.txt", "dogs.txt"]

for file_name in files:
    path = Path(file_name)

    try:
        contents = path.read_text()

    except FileNotFoundError:
        print(f"Sorry, the file '{file_name}' could not be found.\n")

    else:
        print(f"Contents of {file_name}:")
        print(contents)


#Exercise 10
from pathlib import Path

files = ["cats.txt", "dogs.txt"]

for file_name in files:
    path = Path(file_name)

    try:
        contents = path.read_text()

    except FileNotFoundError:
        print(f"Sorry, the file '{file_name}' could not be found.\n")

    else:
        print(f"Contents of {file_name}:")
        print(contents)


#Exercise 11
        from pathlib import Path

files = ["cats.txt", "dogs.txt"]

for file_name in files:
    path = Path(file_name)

    try:
        contents = path.read_text()

    except FileNotFoundError:
        pass

    else:
        print(f"Contents of {file_name}:")
        print(contents)


#Exercise 12
from pathlib import Path

files = [
    "alice.txt",
    "frankenstein.txt",
    "sherlock_holmes.txt",
]

for file_name in files:
    path = Path(file_name)

    try:
        contents = path.read_text(encoding="utf-8")

    except FileNotFoundError:
        print(f"Sorry, {file_name} was not found.\n")

    else:
        lowercase_contents = contents.lower()

        count_the = lowercase_contents.count("the")
        count_the_space = lowercase_contents.count("the ")

        print(f"\nResults for {file_name}")
        print(f"'the' appears      : {count_the} times")
        print(f"'the ' appears     : {count_the_space} times")


#Exercise 13
from pathlib import Path
import json

path = Path("favorite_number.json")

favorite_number = int(input("What is your favorite number? ")) 

contents = json.dumps(favorite_number) #what ever user input we get we save that input inside a variable called contents.  

path.write_text(contents)   #write_text() expects a string, but Favorite_number is an integer. Instead, 
                                         #you should write the JSON string returned by json.dumps().

print("Your favorite number has been saved.")


#Exercise 14
from pathlib import Path
import json

path = Path("favorite_number.json")

if path.exists():
    contents = path.read_text()
    favorite_number = json.loads(contents)
    print(f"I know your favorite number! It's {favorite_number}.")
else:
    favorite_number = input("What is your favorite number? ")

    contents = json.dumps(favorite_number)
    path.write_text(contents)

    print("I'll remember your favorite number!")



#Exercise 15

from pathlib import Path
import json

path = Path("favorite_number.json")

favorite_number = int(input("What is your favorite number? ")) 

contents = json.dumps(favorite_number) #what ever user input we get we save that input inside a variable called contents.  

path.write_text(contents)   #write_text() expects a string, but Favorite_number is an integer. Instead, 
                                         #you should write the JSON string returned by json.dumps().

print("Your favorite number has been saved.")



#Exercise 16
#Last exercise in files and exception chapter.
#I want to practice this more.
from pathlib import Path
import json


def get_stored_user_info(path):
    """Get stored user information if available."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None


def get_new_user_info(path):
    """Prompt for new user information and save it."""
    username = input("What is your name? ")
    age = input("How old are you? ")
    favorite_color = input("What is your favorite color? ")

    user_info = {
        "username": username,
        "age": age,
        "favorite_color": favorite_color,
    }

    contents = json.dumps(user_info)
    path.write_text(contents)

    return user_info


def greet_user():
    """Greet the user."""
    path = Path("user_info.json")

    user_info = get_stored_user_info(path)

    if user_info:
        answer = input(
            f"Is '{user_info['username']}' your username? (yes/no): "
        )

        if answer.lower() == "yes":
            print("\nWelcome back!")
            print("Here's what I remember about you:")
            print(f"Username: {user_info['username']}")
            print(f"Age: {user_info['age']}")
            print(f"Favorite Color: {user_info['favorite_color']}")

        else:
            user_info = get_new_user_info(path)

            print("\nThanks! I'll remember you next time.")
            print(f"Username: {user_info['username']}")
            print(f"Age: {user_info['age']}")
            print(f"Favorite Color: {user_info['favorite_color']}")

    else:
        user_info = get_new_user_info(path)

        print("\nThanks! I'll remember you next time.")
        print(f"Username: {user_info['username']}")
        print(f"Age: {user_info['age']}")
        print(f"Favorite Color: {user_info['favorite_color']}")


greet_user()
