
import random
import string


def generate_password():
    length = input("Please enter a valid password length (greater than 0): ")
    if int(length) > 0:
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=int(length)))
        print("Your password is: " , password)
    else:
       print("Invalid Length", "Please enter a valid password length (greater than 0).")


generate_password()
print("Thank you for using the password generator!")
