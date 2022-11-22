import random

words = ["cup", "ball", "computer", "python", "apple", "water", "flower"]
random_word = random.choice(words)
hidden_word = []
choices = 10
for i in random_word:
    hidden_word.append("_")


def hangman():
    remaining_choices = choices
    while not random_word == str(''.join(hidden_word)):
        print("The word you are looking for:")
        print(' '.join(hidden_word))
        print(f'Remaining choices: {remaining_choices}')
        print("Write a letter:")
        letter = str(input())
        if letter == random_word:
            print(f'Congratulations, the word you are looking for is: {random_word}!!!')
            return exit(0)
        for i in range(0, len(random_word)):
            if random_word[i] == letter:
                hidden_word[i] = letter
        if random_word == str(''.join(hidden_word)):
            print(f'Congratulations, the word you are looking for is: {random_word}!!!')
        remaining_choices -= 1
        if remaining_choices == 0:
            print(f'Unfortunately, the chances are over. The word you are looking for is {random_word}!!!')
            return exit(0)


hangman()
