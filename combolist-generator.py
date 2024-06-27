import itertools
import string
import random
import datetime

def generate_combolist():
    # Ask for username and password lengths
    username_length = int(input("Enter the desired length for usernames: "))
    password_length = int(input("Enter the desired length for passwords: "))

    # Ask for number of combinations
    num_combinations = int(input("Enter the number of combinations to generate: "))

    # Define characters to use for usernames and passwords
    username_chars = string.ascii_lowercase + string.digits
    password_chars = string.ascii_letters + string.digits + string.punctuation

    # Function to generate a single username
    def generate_username():
        return ''.join(random.choice(username_chars) for _ in range(username_length))

    # Function to generate a single password
    def generate_password():
        return ''.join(random.choice(password_chars) for _ in range(password_length))

    # Generate combolist
    combolist = []
    for _ in range(num_combinations):
        username = generate_username()
        password = generate_password()
        combolist.append(f"{username}:{password}")

    # Get current date and time
    current_datetime = datetime.datetime.now()
    timestamp = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

    # Save combolist to file
    filename = f"combolist_{timestamp}.txt"
    with open(filename, "w") as f:
        f.write('\n'.join(combolist))

    print(f"Generated {num_combinations} combinations and saved to {filename}")

if __name__ == "__main__":
    generate_combolist()
