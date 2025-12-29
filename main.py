#imports
import os
import time
import base64
import runpy
from pathlib import Path
import sys
# FUnctions
def get_stored_name():
    # Define the path
    ROOT = Path(__file__).parent
    folder = ROOT / "system_files"
    filename = folder / "username.bin"

    if os.path.exists(filename):
        try:
            with open(filename, "rb") as file:
                encoded_data = file.read()
                return base64.b64decode(encoded_data).decode("utf-8")
        except Exception:
            return None
    return None


def save_name(name):
    ROOT = Path(__file__).parent
    folder = ROOT / "system_files"
    filename = folder / "username.bin"

    permission = input(f"Ok {name}, Can I save your name locally for future refrence? (Y/N): ")

    if permission.lower() == 'y':
        # 1. Create the directory if it doesn't exist
        if not os.path.exists(folder):
            os.makedirs(folder)

        # 2. Encode and save
        encoded_name = base64.b64encode(name.encode("utf-8"))
        with open(filename, "wb") as file:
            file.write(encoded_name)
        print(f"Name stored securely in {filename}")
    else:
        print("Name will not be saved.")



print("Hello!")
name = get_stored_name()

if name:
    print(f"Welcome back, {name}!")
else:
    name = input("What's your name? ")
    save_name(name)
    print(f"Hello, {name}!")
time.sleep(2)
print("Welcome to PyHub!")
print("Here is a list of available features with a corresponding number")
time.sleep(1)
print("1 - Snake Calculator")
print("2 - Games")
feature = input("What feature would you like to access? ")
if feature == "1":
    print("OK!")
    print("Running Snake Calculator")
    runpy.run_path("features/calculator.py")
elif feature == "2":
    print("Running Games")
    runpy.run_path("features/GameHub/games.py")
else:
    print("Invalid.")
print("Thank you for using PyHub!")
print("Please rerun for using a different program")
print("Bye now!")
sys.exit(0)