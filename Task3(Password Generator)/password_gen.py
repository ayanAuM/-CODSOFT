import random
import string


def generate_password(length):
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits+ string.punctuation

    # Generate a random password of the specified length
    password = ''.join(random.choice(characters)for _ in range(length))

    return password

def main():
    try:
        # Prompt the user for the desired password length
        length = int(input('How many characters would you like your password to be? '))

        if length <= 0:
            print(" Password length should be a positive integer.")
        else:
            # Generate and display the password
            password=generate_password(length)
            print("Your generated password is : ",password)
    except ValueError:
        print("Invalid input. Please enter a valid positive integer for the password length. ")
        
if __name__ == "__main__":
    main()        
