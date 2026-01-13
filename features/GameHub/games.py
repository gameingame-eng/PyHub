"""
© 2026 Lakshya.  
Licensed under CC BY-NC 4.0.  
https://creativecommons.org/licenses/by-nc/4.0/
"""
import os
import webview
import time
from pathlib import Path
import runpy as run
import sys


# 1. This function stays here so the EXE knows how to find its internal files
def resource_path(relative_path):
    try:
        # If running as an EXE (PyInstaller)
        base_path = sys._MEIPASS
    except Exception:
        # If running as a script, get the folder containing THIS script
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_path, relative_path)



def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def launch_game(game):
    # 2. Use Path() around resource_path so .exists() works correctly
    if game == "snowrider":
        html_file = Path(resource_path(os.path.join("features", "GameHub", "games", "snowrider.html")))
        gamename = "Snow Rider 3D"
    elif game == "Drive_mad":
        html_file = Path(resource_path(os.path.join("features", "GameHub", "games", "drivemad.html")))
        gamename = "Drive Mad"

    if html_file.exists():
        print(f"Launching {gamename} in a popup... (Check your taskbar)")

        # We use str() here because webview needs a string, not a Path object
        webview.create_window(
            f'{gamename} - PyHub',
            str(html_file.absolute()),
            width=900,
            height=600,
            resizable=True
        )
        webview.start()
        print("We have detected that the game was closed")
        print("So here is the menu for you again!")
    else:
        print(f"Error: Could not find {html_file}")
        input("Press Enter to continue...")


def games_menu():
    while True:
        clear_screen()
        print("---  PyHub Games Menu  ---")
        print("1. Snow Rider 3D")
        print("2. Drive Mad")
        print("3. Pong")
        print("4. Snake")
        print("5. Return to Main Menu")
        print("------------------------------")

        choice = input("Select a game to play: ")

        if choice == "1":
            launch_game("snowrider")
        elif choice == "2":
            launch_game("Drive_mad")
        elif choice == "5":
            print("Returning...")
            return
        elif choice == "3":
            # Construct the absolute path using your resource_path function
            pong_path = resource_path(os.path.join("games", "pong", "launcher.py"))
            
            if os.path.exists(pong_path):
                run.run_path(pong_path)
            else:
                print(f"Error: Launcher not found at {pong_path}")
                time.sleep(2)
        elif choice == "4":
            snake_path = resource_path(os.path.join("games", "snake", "snake.py"))
            
            if os.path.exists(snake_path):
                run.run_path(snake_path)
            else:
                print(f"Error: Launcher not found at {snake_path}")
                time.sleep(2)
        else:
            print("Invalid selection. Try again.")
            time.sleep(1)
games_menu()