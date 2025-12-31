import os
import sys
import platform
import runpy

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def clear():
    os.system("cls" if platform.system() == "Windows" else "clear")

def main_menu():
    while True:
        clear()
        print("--- PyHub ---")
        print("1. Calculator")
        print("2. GameHub")
        print("3. PySpelling")
        print("4. User Data")
        print("5. Exit")

        choice = input("Select: ")

        try:
            if choice == "1":
                # Path inside the EXE bundle
                # Use run_name="__main__" or it will crash inside the EXE
                runpy.run_path(resource_path(os.path.join("features", "calculator.py")), run_name="__main__")
            elif choice == "2":
                runpy.run_path(resource_path(os.path.join("features", "GameHub", "games.py")), run_name="__main__")
            elif choice == "3":
                runpy.run_path(resource_path(os.path.join("features", "PySpelling", "dictionary.py")), run_name="__main__")
            elif choice == "4":
                runpy.run_path(resource_path("dat.py"), run_name="__main__")
            elif choice == "5":
                break
        except Exception as e:
            print(f"Error launching feature: {e}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()