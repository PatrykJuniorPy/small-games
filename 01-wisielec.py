import sys

if __name__ == '__main__':
    pass

no_of_tries = 5
word = "kamil"
used_letters = []
user_word = []


def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes


def show_state_of_game():
    print()
    print(user_word)
    print("pozostalo prob", no_of_tries)
    print("uzyte litery", used_letters)
    print()


for letter in word:
    user_word.append("_")

while True:
    letter = input("podaj literę: ")
    used_letters.append(letter)
    found_indexes = find_indexes(word, letter)
    if len(found_indexes) == 0:
        print("nie ma takiej litery")
        no_of_tries -= 1

        if no_of_tries == 0:
            print("koniec gry :(")
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter

        if "".join(user_word) == word:
            print("brawo to jest to slowo!")
            sys.exit(0)

    show_state_of_game()