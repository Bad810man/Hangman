import random

wins = 0
loses = 0

def play():
    words = ['python', 'java', 'swift', 'javascript']
    program_word = random.choice(words)
    hint = list("-" * len(program_word))
    guessed_letters = set()
    attempts = 8

    while attempts > 0:
        print("".join(hint))
        letter = input("Input a letter: ")
        if len(letter) == 1:
            if letter.isalpha() and letter.islower():
                if letter not in guessed_letters:
                    if letter in program_word:
                        for i in range(len(hint)):
                            if program_word[i] == letter:
                                hint[i] = letter
                    else:
                        attempts -= 1
                        print("That letter doesn't appear in the word.")
                else:
                    print("You've already guessed this letter.")
            else:
                print("Please, enter a lowercase letter from the English alphabet.")
        else:
            print("Please, input a single letter.")

        guessed_letters.add(letter)
        if "".join(hint) == program_word:
            print("")
            print(f"You guessed the word {program_word}!")
            print("You survived!")
            return 1
            break

        if attempts == 0:
            print("You lost!")
            return 0

        print("")

def score(count_wins, count_loses):
    print(f"You won: {count_wins} times.")
    print(f"You lost: {count_loses} times.")

print("H A N G M A N\n")
while True:
    choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')

    if choice == "play":
        print("")
        result = play()
        if result == 1:
            wins += 1
        else:
            loses += 1
    elif choice == "results":
        score(wins, loses)
    elif choice == "exit":
        break