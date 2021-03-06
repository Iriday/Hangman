from random import choice
from string import ascii_letters
import re


def input_(message=""):
    return input(message).strip().lower()


def output(data=""):
    print(data)


def remove_all(string, regex):
    return re.sub(regex, "", string)


def get_words_from_file(filepath):
    words = list()
    with open(filepath, mode="r") as file:
        for line in file:
            words.extend(re.split("[,\\s]+", line.strip().lower()))

    return list(filter(lambda word: word.__len__() > 0, words))


def uncover_letter(entire_word, word_to_update, letter):
    uncovered = -1  # -1-> no letter
    for i in range(0, len(entire_word)):
        if entire_word[i] == letter:
            if word_to_update[i] == letter:
                return 0  # 0-> already uncovered
            word_to_update[i] = letter
            uncovered = 1  # 1-> uncovered
    return uncovered


def input_check(input_letter_, inputted_letters_):
    if len(input_letter_) != 1:
        return "You should print a single letter"
    if input_letter_ not in ascii_letters:
        return "It is not an ASCII letter"
    if input_letter_ in inputted_letters_:
        return "You already typed this letter"
    return 0


def menu():
    while True:
        in_ = input_("1. Play the game\n2. Import words\n3. Show all words\n0. Exit\n")
        if in_ == "0" or in_ == "exit" or in_ == "quit" or in_ == "leave" or in_ == "stop" or in_ == "break" or in_ == "bye":
            return 0
        elif in_ == "1" or in_ == "play" or in_ == "start" or in_ == "run":
            return 1
        elif in_ == "2" or in_ == "import" or in_ == "import words":
            return 2
        elif in_ == "3" or in_ == "show" or in_ == "show words" or in_ == "show all words":
            return 3
        else:
            output("Incorrect input\n")


def start_game():
    output("\t\t\t\tH A N G M A N")

    WORDS = ("java", "kotlin", "python", "javascript", "rust", "ruby", "perl", "swift", "scratch", "haskel", "pascal",
             "fortran", "ada", "apex", "groovy", "dart", "scala", "cplusplus", "assembly", "prolog")

    while True:
        option = menu()
        if option == 0:
            break
        elif option == 2:
            try:
                words = get_words_from_file(input_("Enter filepath: "))
                if words.__len__() == 0:
                    output("Something went wrong, check filepath\\file content\n")
                    continue
            except Exception:
                output("Something went wrong, check filepath\\file content\n")
                continue
            WORDS = words
            output("Words have been imported successfully\n")
            continue
        elif option == 3:
            output("Words: " + ", ".join(WORDS) + ".\n")
            continue

        rand_word = choice(WORDS)

        inputted_letters = set()

        word_hint_str = len(rand_word) * "-"
        word_hint_list = list(word_hint_str)

        num_of_tries = 8
        while num_of_tries != 0:
            output(f"\n{word_hint_str}")

            input_letter = input_("Input a letter: ")
            err_message = input_check(input_letter, inputted_letters)
            if err_message != 0:
                output(err_message)
                continue
            inputted_letters.add(input_letter)

            uncovered = uncover_letter(rand_word, word_hint_list, input_letter)
            if uncovered == -1:
                output("No such letter in the word")
                num_of_tries -= 1
            else:
                word_hint_str = "".join(word_hint_list)
                if rand_word == word_hint_str:
                    output(f"\nYou guessed the word {rand_word}!\nYou survived!\n")
                    break
        else:
            output("\nYou are hanged!\n")


start_game()
