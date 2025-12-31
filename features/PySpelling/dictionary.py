import json
import os
import difflib
import string
from pathlib import Path

import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def load_word_list():
    folder = Path(__file__).parent

    # 1. Wrap the joined path in Path() so it becomes a Path object
    json_path = Path(resource_path(os.path.join("features", "PySpelling", "words_dictionary.json")))

    # 2. Move the existence check BEFORE trying to open the file
    if not json_path.exists():
        print(f"❌ Error: {json_path.name} not found in {json_path.parent}")
        print("Please move the JSON file into the PySpelling folder.")
        return None

    print("Loading local database...")
    # 3. Use 'with' once to load the data
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return set(data.keys())


def clean_word(text):
    return text.strip(string.punctuation).lower()


def check_sentence(raw_text, word_set):
    words = raw_text.split()
    corrected_output = []

    for original_word in words:
        clean = clean_word(original_word)
        if not clean or clean.isdigit() or clean in word_set:
            corrected_output.append(original_word)
        else:
            # Highlighting the error
            corrected_output.append(f"__[{original_word}]__")

    print("\n--- 📝 Result ---")
    print(" ".join(corrected_output))


def spell_checker_tool():
    word_set = load_word_list()
    if not word_set:
        input("\nPress Enter to return to menu...")
        return

    while True:
        print(f"\n--- ✅ PyHub Spell Checker ---")
        print("1. Single Word | 2. Sentence | 3. Back")
        choice = input("Selection: ").strip()

        if choice == '3':
            break
        elif choice == '1':
            word = input("Word: ").strip().lower()
            if word in word_set:
                print(f"Correct.")
            else:
                print(f"Misspelled.")
                sug = difflib.get_close_matches(word, list(word_set), n=3)
                if sug: print(f"   Try: {', '.join(sug)}")
        elif choice == '2':
            text = input("Enter sentence:\n> ")
            check_sentence(text, word_set)

        input("\nPress Enter to continue...")
spell_checker_tool()