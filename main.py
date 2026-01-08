"""
© 2026 Lakshya.  
Licensed under CC BY-NC 4.0.  
https://creativecommons.org/licenses/by-nc/4.0/
"""


import pygame
import os
import sys
import platform
import runpy
def playmusic():
    pygame.mixer.init()
    pygame.mixer.music.load("features/music/elevator-music.mp3")
    pygame.mixer.music.play(-1)  # -1 = loop forever

def resource_path(relative_path):
    # Get absolute path to resource, works for dev and for PyInstaller
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def clear():
    if platform.system() == "wasi":
        print("")
    else:
        os.system("cls" if platform.system() == "Windows" else "clear")

def main():
    while True:
        clear()
        print("--- PyHub ---")
        print("1. Calculator")
        print("2. GameHub")
        print("3. PySpelling")
        print("4. PassGen")
        print("5. User Data Management")
        print("6. Exit")
        print("----Thank you to lkoliks or the backround music-----")

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
            elif choice == "5":
                runpy.run_path(resource_path("dat.py"), run_name="__main__")
            elif choice == "6":
                break
            elif choice == "4":
                runpy.run_path(resource_path(os.path.join("features", "PassGen", "passgen.py")), run_name="__main__")
        except Exception as e:
            print(f"Error launching feature: {e}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    playmusic()
    main()