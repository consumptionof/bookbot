from string import ascii_lowercase


def main():
    with open("books/frankenstein.txt", "r") as f:
        file_contents = f.read()

    print(number_of_words(file_contents))
    letters_counted = count_of_letters(file_contents)
    for i in ascii_lowercase:
        print(f"{i} occurs in Frankenstein {letters_counted[i]} times.")


def number_of_words(file):
    return len(file.split())


def count_of_letters(file):
    letters = {}
    for letter in file.lower():
        if letter not in letters:
            letters[letter] = 0
        letters[letter] += 1
    return letters


main()
