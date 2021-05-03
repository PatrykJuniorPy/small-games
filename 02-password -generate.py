import sys
import random
import string


password = []
characters_left = -1

def update_charactes_left(number_of_characters):
    global characters_left
    if number_of_characters < 0 or number_of_characters > characters_left:
        print("number from 0", characters_left)
        sys.exit(0)
    else:
        characters_left -= number_of_characters
        print("letters left:", characters_left)

password_length = int(input("how long password should be? "))

if password_length < 5:
    print("password must contain at least 5 letters or equal, try again.")
    sys.exit(0)
else:
    characters_left = password_length

lowercase_letters = int(input("how many lowers_cases? "))
update_charactes_left(lowercase_letters)

uppercase_letters = int(input("how many upper_cases? "))
update_charactes_left(uppercase_letters
                      )
special_characters = int(input("how many special_cases? "))
update_charactes_left(special_characters)

digits = int(input("how many digits? "))
update_charactes_left(digits)

if characters_left > 0:
    print("not all letters has been used, password has been updated with lowercase letters")
    lowercase_letters += characters_left

print()
print("password length:", password_length)
print("lowecase:", lowercase_letters)
print("uppercase", uppercase_letters)
print("special characters", special_characters)
print("digits", digits)

for _ in range(password_length):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)
print("generated passoword:", "".join(password))


if __name__ == '__main__':
    pass
