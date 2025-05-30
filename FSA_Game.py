import random
import time
from wordbank import WORDS
from structures import STRUCTURES

def get_structures_by_level(level):
    if level == 1:
        return [s for s in STRUCTURES if len(s) <= 3]
    elif level == 2:
        return [s for s in STRUCTURES if 4 <= len(s) <= 5]
    else:
        return [s for s in STRUCTURES if len(s) > 5]

def generate_correct_sentence(structure, words_dict):
    return ' '.join(random.choice(words_dict[cat]) for cat in structure)

def check_sentence_with_fsa(sentence: str, structure: list, words_dict: dict) -> bool:
    words = sentence.lower().split()
    if len(words) != len(structure):
        return False
    for word, expected_category in zip(words, structure):
        if word not in words_dict.get(expected_category, []):
            return False
    return True

def play_game():
    points = 5
    print("Welcome into the grammar FSA game")
    print("You can type exit to stop the game")
    
    while True:
        try:
            level = int(input("\nChoose a level (1 easy, 2 medium, 3 hard): "))
            if level in [1, 2, 3]:
                break
        except ValueError:
            pass
        print("Choose between 1,2 and 3")

    structures_by_level = get_structures_by_level(level)
    max_time = 15 if level == 1 else 10 if level == 2 else 7

    while points > 0:
        structure = random.choice(structures_by_level)
        print(f"\nExpected structure: {' + '.join(structure)}")
        print(f"(⏱ {max_time} sec max)")

        start = time.time()
        try:
            sentence = input("Write a sentence : ")
        except:
            sentence = ""
        duration = time.time() - start

        if sentence.lower() == "exit":
            break

        if duration > max_time:
            print("Times up! -1 point")
            points -= 1
            continue

        if check_sentence_with_fsa(sentence, structure, WORDS):
            points += 1
            print("Correct ! Points:", points)
        else:
            correct = generate_correct_sentence(structure, WORDS)
            points -= 1
            print("Incorrect !")
            print("Possible correct example:", correct)
            print("Points remaining :", points)

    # Feedback final
    print("\n End of the game.")
    if points <= 0:
        print("GAME OVER. You've used up all your points.")
    else:
        print(f"You leaved with {points} points.")

    if points >= 10:
        print("Good job")
    elif points >= 5:
        print("Keep up the good work!")
    else:
        print("You can progress, do it again")

# Lancer le jeu
if __name__ == "__main__":
    play_game()
