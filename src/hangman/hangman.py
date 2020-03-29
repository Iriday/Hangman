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


def uncover_letter(entire_word, word_to_update, letter):
    uncovered = -1  # -1-> no letter
    for i in range(0, len(entire_word)):
        if entire_word[i] == letter:
            if word_to_update[i] == letter:
                return 0  # 0-> already uncovered
            word_to_update[i] = letter
            uncovered = 1  # 1-> uncovered
    return uncovered


def start_game():
    output("H A N G M A N")

    WORDS = ("java", "kotlin", "python", "javascript", "rust", "ruby", "perl", "swift", "scratch", "haskel", "pascal",
             "fortran", "ada", "apex", "groovy", "dart", "scala", "c++", "assembly", "prolog")
    rand_word = choice(WORDS)

    regex = "[', \\[\\]]+"

    word_hint_list = create_list_of(len(rand_word), "-")
    word_hint_str = remove_all(word_hint_list.__str__(), regex)

    num_of_tries = 8
    while num_of_tries != 0:
        output(f"\n{word_hint_str}")

        input_letter = input_("Input a letter: ")

        uncovered = uncover_letter(rand_word, word_hint_list, input_letter)
        if uncovered == -1:
            output("No such letter in the word")
            num_of_tries -= 1
        elif uncovered == 0:
            output("No improvements")
            num_of_tries -= 1
        else:
            word_hint_str = remove_all(word_hint_list.__str__(), regex)
            if rand_word == word_hint_str:
                output(f"\n{rand_word}\nYou guessed the word!\nYou survived!")
                break
    else:
        output("\nYou are hanged!")


start_game()
