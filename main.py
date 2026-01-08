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

# Global variable to track music state
music_paused = False

def playmusic():
    """Initializes and starts the music."""
    global music_paused
    pygame.mixer.init()
    try:
        # Using resource_path to ensure it works in EXE
        music_file = resource_path(os.path.join("features", "music", "elevator-music.mp3"))
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1)
        music_paused = False
    except Exception as e:
        print(f"Could not load music: {e}")

def toggle_music():
    """Toggles the music state."""
    global music_paused
    if music_paused:
        pygame.mixer.music.unpause()
        music_paused = False
        print("Music Resumed!")
    else:
        pygame.mixer.music.pause()
        music_paused = True
        print("Music Paused!")

def resource_path(relative_path):
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
        print(f"--- Music: {'OFF' if music_paused else 'ON'} (Press 'k' + Enter to toggle) ---")
        print("----Thank you to lkoliks for the background music-----")

        choice = input("Select: ").lower() # .lower() handles 'K' or 'k'

        try:
            if choice == "k":
                toggle_music()
                continue # Refresh the menu to show updated status
            elif choice == "1":
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