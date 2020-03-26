from random import choice


def input_():
    return input("Guess the word: ").strip().lower()


def output(data_):
    print(data_)


def get_outcome(program_word_, user_word_):
    return "You survived!" if program_word_ == user_word_ else "You are hanged!"


output("H A N G M A N")

WORDS = ("java", "kotlin", "python", "javascript")

rand_word = choice(WORDS)

user_word = input_()

output(get_outcome(rand_word, user_word))
