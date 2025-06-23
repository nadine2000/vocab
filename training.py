import time
import random
from utils import load_vocab


def training_mode():

    vocab = load_vocab()
    units = list(vocab.keys())

    print("Available units:", ", ".join(units))
    unit = input("Choose a unit: ").strip().lower()
    if unit not in vocab:
        print("Invalid unit.")
        return

    words = vocab[unit]
    print("\nWords in this unit:")
    for word in words:
        print("-", word["word"])

    choice = input("Practice full unit or range? (full/range): ").strip().lower()
    if choice == "range":
        start = input("Start word: ").strip().lower()
        end = input("End word: ").strip().lower()

        all_words = [entry["word"] for entry in words]
        if start not in all_words or end not in all_words:
            print("One or both words not found in unit.")
            return

        start_index = all_words.index(start)
        end_index = all_words.index(end)

        if start_index > end_index:
            print("Start word must appear before end word.")
            return

        selected = words[start_index:end_index + 1]

    elif choice == "full":
        selected = words
    else:
        print("Invalid Option! the valid options are full or range.")
        return

    total_words = len(selected)
    max_index = total_words - 1
    repeat_count = [0] * total_words

    while not all(word_counter == 7 for word_counter in repeat_count):
        index = random.randint(0, max_index)
        while repeat_count[index] == 7:
            index = (index + 1) % total_words
        print("\nWord:", selected[index]["word"])
        time.sleep(3)
        print("Meaning:", selected[index]["meaning"])
        repeat_count[index] += 1

    print("\nTraining complete.")
