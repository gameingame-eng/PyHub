import random
import string
import runpy as run
def back_to_main():
  print("Returning to PyHub")
  print(".")
  run.run_path("./main.py")
def get_user_input():
    length = int(input("Enter desired password length: "))
    chars_to_avoid1 = input("Enter characters to avoid (leave blank if none): ")
    chars_to_avoid2 = "/.<>,`~][}{]|"
    chars_to_avoid = chars_to_avoid1 + chars_to_avoid2
    word_to_include = input("Enter a word to include in the password (leave blank if none): ")

    if len(word_to_include) > length:
        raise ValueError("The word to include is longer than the desired password length. Try again.")

    return length, chars_to_avoid, word_to_include

def build_character_pool(chars_to_avoid):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    pool = [char for char in all_chars if char not in chars_to_avoid]
    
    if not pool:
        raise ValueError("Character pool is empty after removing avoided characters.")
    
    return pool

def generate_password(length, word_to_include, pool):
    remaining_length = length - len(word_to_include)
    
    # Split remaining characters for left and right
    left_length = remaining_length // 2
    right_length = remaining_length - left_length

    left_chars = [random.choice(pool) for _ in range(left_length)]
    right_chars = [random.choice(pool) for _ in range(right_length)]

    # Assemble the password
    password_list = left_chars + list(word_to_include) + right_chars
    password = ''.join(password_list)
    print("Generated password:", password)




length, chars_to_avoid, word_to_include = get_user_input()
pool = build_character_pool(chars_to_avoid)
generate_password(length, word_to_include, pool)
back_to_main()