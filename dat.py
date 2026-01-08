import base64 as b64
import os
from pathlib import Path
import runpy as run
import time as t
"""
© 2026 Lakshya.  
Licensed under CC BY-NC 4.0.  
https://creativecommons.org/licenses/by-nc/4.0/
"""
# Globals
name = None
name_found = False

def get_stored_name():
    global name, name_found

    ROOT = Path(__file__).parent
    folder = ROOT / "system_files"
    filename = folder / "username.bin"

    if os.path.exists(filename):
        try:
            with open(filename, "rb") as file:
                encoded_data = file.read()
                name = b64.b64decode(encoded_data).decode("utf-8")
                name_found = True
        except Exception:
            name_found = False
    else:
        name_found = False

def nameupd():
    if name_found:
        print("I currently have your name locally saved as:")
        print(name)
        return input("Would you like to update it (Y/N)? ")
    else:
        print("I do not have your name saved.")
        return input("Would you like to save it (Y/N)? ")

def update_username():
    ROOT = Path(__file__).parent
    folder = ROOT / "system_files"
    filename = folder / "username.bin"

    new_name = input("Enter the new name you want to save: ").strip()

    if not new_name:
        print("Error: Name cannot be empty.")
        return

    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Created directory: {folder}")

    try:
        encoded_name = b64.b64encode(new_name.encode("utf-8"))
        with open(filename, "wb") as file:
            file.write(encoded_name)

        print("-------------------------------")
        print(f" Success! Name updated to: {new_name}")
        print("-------------------------------")

    except Exception as e:
        print(f" An error occurred: {e}")

# ---- Program flow ----
get_stored_name()

print("Hello!")
print("---------------")

updateornot = nameupd()

if updateornot.lower() == "y":
    update_username()
    print("Task complete, returning to PyHub....")
    run.run_path("main.py")

elif updateornot.lower() == "n":
    print("Returning to PyHub...")
    t.sleep(1)
    print(".")
    t.sleep(0.5)
    run.run_path("main.py")
