from random import choice
import re


def input_(message=""):
    return input(message).strip().lower()


def output(data_=""):
    print(data_)


def create_list_of(size, char=" "):
    return list(char * size)


def remove_all(string, regex):
    return re.sub(regex, "", string)


def open_letter(entire_word, word_to_update, letter):
    opened = False
    for i in range(0, len(entire_word)):
        if entire_word[i] == letter:
            word_to_update[i] = letter
            opened = True
    return opened


def start_game():
    output("H A N G M A N")

    WORDS = ("java", "kotlin", "python", "javascript", "rust", "ruby", "perl", "swift", "scratch", "haskel", "pascal",
             "fortran", "ada", "apex", "groovy", "dart", "scala", "c++", "assembly", "prolog")
    rand_word = choice(WORDS)

    regex = "[', \\[\\]]+"

    word_hint_list = create_list_of(len(rand_word), "-")
    word_hint_str = remove_all(word_hint_list.__str__(), regex)

    for num_of_tries in range(0, 10):
        output(f"\n{word_hint_str}")

        input_letter = input_("Input a letter: ")

        opened = open_letter(rand_word, word_hint_list, input_letter)
        if not opened:
            output("No such letter in the word")
            continue

        word_hint_str = remove_all(word_hint_list.__str__(), regex)
        if rand_word == word_hint_str:
            output("\nYou survived!")
            return

    output("\nYou are hanged!")


start_game()
