from utils import load_vocab, save_vocab

vocab = load_vocab()


def clean_word(word):

    word = word.strip().lower()
    if word != "":
        return word
    else:
        raise ValueError(f"input cannot be empty!")


def add_word(unit, word, meaning):

    if unit not in vocab:
        vocab[unit] = []

    if any(entry["word"] == word for entry in vocab[unit]):
        print("Word already exists!")
        return

    vocab[unit].append({"word": word, "meaning": meaning})
    save_vocab(vocab)

    print(f"Added {word} to {unit}")


def delete_word(unit, word):

    if unit in vocab:
        vocab[unit] = [e for e in vocab[unit] if e["word"] != word]
        save_vocab(vocab)
        print(f"Deleted {word} from {unit}")
    else:
        print("Unit not found.")


def update_word(unit, old_word, new_word, new_meaning):

    if unit in vocab:
        for entry in vocab[unit]:
            if entry["word"] == old_word:
                entry["word"] = new_word
                entry["meaning"] = new_meaning
                save_vocab(vocab)
                print(f"Updated {old_word} in {unit}")
                return
        print("Word not found.")
    else:
        print("Unit not found.")


def list_words(unit):

    if unit in vocab:
        for entry in vocab[unit]:
            print(f'{entry["word"]}: {entry["meaning"]}')
    else:
        print("Unit not found.")


def editing_menu():

    print("\nEditing Mode:")
    print("a. Add word")
    print("b. Delete word")
    print("c. Update word")
    print("d. List words")

    try:
        sub = clean_word(input("Choose a sub-option: "))
        unit = clean_word(input("Unit name: "))

        if sub == "a":
            word = clean_word(input("English word: "))
            meaning = clean_word(input("Meaning: "))
            add_word(unit, word, meaning)
        elif sub == "b":
            word = clean_word(input("Word to delete: "))
            delete_word(unit, word)
        elif sub == "c":
            old = clean_word(input("Word to update: "))
            new = clean_word(input("New word: "))
            new_meaning = clean_word(input("New meaning: "))
            update_word(unit, old, new, new_meaning)
        elif sub == "d":
            list_words(unit)
        else:
            print("Unknown Option!")

    except ValueError as e:
        print(f"Error: {e}")

