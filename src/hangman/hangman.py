from random import choice


def input_(message=""):
    return input(message).strip().lower()


def output(data_):
    print(data_)


def get_outcome(program_word_, user_word_):
    return "You survived!" if program_word_ == user_word_ else "You are hanged!"


def replace_trailing(string, num, char=""):
    return string[0:len(string) - num:1].ljust(len(string), char)


output("H A N G M A N")

WORDS = ("java", "kotlin", "python", "javascript", "rust", "ruby", "perl", "swift", "scratch", "haskel", "pascal",
         "fortran", "ada", "apex", "groovy", "dart", "scala", "c++", "assembly", "prolog")
rand_word = choice(WORDS)

word_hint = replace_trailing(rand_word, len(rand_word) - 1, "-")

user_word = input_(f"Guess the word {word_hint}: ")

output(get_outcome(rand_word, user_word))
