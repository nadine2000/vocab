import json

VOCAB_FILE = "vocab_hebrew.json"


def load_vocab():
    with open(VOCAB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_vocab(vocab):
    with open(VOCAB_FILE, "w", encoding="utf-8") as f:
        json.dump(vocab, f, ensure_ascii=False, indent=4)
