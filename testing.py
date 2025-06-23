from utils import load_vocab


def testing_mode():
    vocab = load_vocab()
    units = list(vocab.keys())
    print("Available units:", units)
    unit = input("Choose a unit: ").strip().lower()
    if unit not in vocab:
        print("Invalid unit.")
        return

    words = vocab[unit]
    correct = 0
    wrong = []

    for entry in words:
        print("\nWord:", entry["word"])
        answer = input("What is the meaning? ").strip()
        if answer == entry["meaning"]:
            correct += 1
        else:
            wrong.append(entry)

    total = len(words)
    print("\n=== Test Summary ===")
    print(f"Number of correct answers: {correct} out of {total}")
    print(f"Score: {correct / total * 100:.1f}% ")
    print(f"Total questions: {total}")

    if wrong:
        print("Incorrect Answers:")
        for entry in wrong:
            print("- ", entry["word"], entry["meaning"])
