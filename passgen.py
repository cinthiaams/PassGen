'''PassGen is a simple and customizable password generator'''

import random
import string

def gen_pass(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    '''Generate a random password'''
    if not any([use_upper, use_lower, use_digits, use_symbols]):
        raise ValueError ("At least one character type must be selected")

    character_pool = ''
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main ():
    '''Main function to run the PassGen password generator.'''

    print("Welcome to PassGen - Your Password Generator\n")

    length =  int(input("Enter the length of the password (default 12): ") or 12)

    use_upper = input("Include uppercase letters? (y/n, default y): ").lower() != 'n'
    use_lower = input("Include lowercase letters? (y/n, default y): ").lower() != 'n'
    use_digits = input("Include digits? (y/n, default y): ").lower() != 'n'
    use_symbols = input("Include symbols? (y/n, default y): ").lower() != 'n'

    try:
        password = gen_pass(length, use_upper, use_lower, use_digits, use_symbols)
        print(f"\nYour generate password is: {password}\n")
    except ValueError as e:
        print(f"\nError: {e}\n")

if __name__ == "__main__":
    main()
