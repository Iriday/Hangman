from random import choice
from string import ascii_letters
import re


def input_(message=""):
    return input(message).strip().lower()


def output(data_=""):
    print(data_)


def create_list_of(size, char=" "):
    return list(char * size)


def remove_all(string, regex):
    return re.sub(regex, "", string)


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
    in_ = input_('Type "play" to play the game, "exit" to quit: ')

    if in_ == "exit" or in_ == "2" or in_ == "quit" or in_ == "leave" or in_ == "stop" or in_ == "break" or in_ == "bye":
        return 2
    elif in_ != "play" and in_ != "1" and in_ != "start":
        return -1
    return 1


def start_game():
    output("\t\t\t\tH A N G M A N")

    WORDS = ("java", "kotlin", "python", "javascript", "rust", "ruby", "perl", "swift", "scratch", "haskel", "pascal",
             "fortran", "ada", "apex", "groovy", "dart", "scala", "cplusplus", "assembly", "prolog")
    regex = "[', \\[\\]]+"

    while True:
        in_command = menu()
        if in_command == 2:
            break
        elif in_command == -1:
            output("Unknown command")
            continue

        rand_word = choice(WORDS)

        inputted_letters = set()

        word_hint_list = create_list_of(len(rand_word), "-")
        word_hint_str = remove_all(word_hint_list.__str__(), regex)

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
                word_hint_str = remove_all(word_hint_list.__str__(), regex)
                if rand_word == word_hint_str:
                    output(f"\nYou guessed the word {rand_word}!\nYou survived!\n")
                    break
        else:
            output("\nYou are hanged!\n")


start_game()
