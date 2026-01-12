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
import subprocess as sub

# Global variable to track music state
Java_Found = False
music_paused = False
def JavaCheck():
    has_java_str = sys.argv[1] if len(sys.argv) > 1 else "False"
    has_java = has_java_str == "True"
    return has_java
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
        print("5. System Stats")
        if Java_Found == True:
            print("6. GradeApp")
        elif Java_Found == False:
            print("6. GradeApp - Will not work as java is not install on this machine")
        else
        print("7. User Data Management")
        print("8. Exit")
        print(f"--- Music: {'OFF' if music_paused else 'ON'} (Press 'k' + Enter to toggle) ---")
        if Java_Found == True:
            print("")
        elif Java_Found == False:
            print("")
            print("Java was not found on this Machine. You will not be able to run the GradeApp")
            print("Feature unless you install it and add it to PATH")
        else:
            print("")
        print("----Thank you to lkoliks for the background music-----")

        choice = input("Select: ").lower() # .lower() handles 'K' or 'k'

        try:
            if choice == "k":
                toggle_music()
                continue 
            elif choice == "1":
                runpy.run_path(resource_path(os.path.join("features", "calculator.py")), run_name="__main__")
            elif choice == "2":
                runpy.run_path(resource_path(os.path.join("features", "GameHub", "games.py")), run_name="__main__")
            elif choice == "3":
                runpy.run_path(resource_path(os.path.join("features", "PySpelling", "dictionary.py")), run_name="__main__")
            elif choice == "7":
                runpy.run_path(resource_path("dat.py"), run_name="__main__")
            elif choice == "8":
                break
            elif choice == "4":
                runpy.run_path(resource_path(os.path.join("features", "PassGen", "passgen.py")), run_name="__main__")
            elif choice == "5":
                stats_path = resource_path(os.path.join("features", "cStats", "Stats.exe"))
            elif choice == "6":
                if Java_Found == True:
                    launcher_path = resource_path(os.path.join("features", "GradeApp", "launcher.py"))
                    runpy.run_path(launcher_path, run_name="__main__")
                else:
                    launcher_path = resource_path(os.path.join("features", "GradeApp", "__err__.py"))
                    runpy.run_path(launcher_path, run_name="__main__")

                
                # Use subprocess.run to wait for the user to finish viewing stats
                sub.run(stats_path, check=True)
        except Exception as e:
            print(f"Error launching feature: {e}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    Java_Found = JavaCheck()
    playmusic()
    main()
