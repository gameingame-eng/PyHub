import base64 as b64
import os
from pathlib import Path
import runpy as run
import time as t
def nameupd():
    print("I currently have your name locally saved as:")
    print(name)
    updateornot = input("Would you like to update it (Y/N)? ")
    return updateornot
def get_stored_name():
    # Define the path
    ROOT = Path(__file__).parent
    folder = ROOT / "system_files"
    filename = folder / "username.bin"

    if os.path.exists(filename):
        try:
            with open(filename, "rb") as file:
                encoded_data = file.read()
                name = b64.b64decode(encoded_data).decode("utf-8")
                return name
        except Exception:
            return None
    return None
    return name

def update_username():
    # 1. Setup paths
    ROOT = Path(__file__).parent
    folder = ROOT / "system_files"
    filename = folder / "username.bin"

    # 2. Get the new name
    new_name = input("Enter the new name you want to save: ").strip()

    if not new_name:
        print("Error: Name cannot be empty.")
        return

    # 3. Ensure the folder exists
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Created directory: {folder}")

    try:
        # 4. Encode to Base64 (to match your existing system)
        encoded_name = b64.b64encode(new_name.encode("utf-8"))

        # 5. Write to the file
        with open(filename, "wb") as file:
            file.write(encoded_name)

        print("-------------------------------")
        print(f" Success! Name updated to: {new_name}")
        print("-------------------------------")

    except Exception as e:
        print(f" An error occurred: {e}")
name = get_stored_name()
print(f"Hello, {name}")
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