import os
import webview  # New import
import time
from pathlib import Path


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def launch_game(game):
    ROOT = Path(__file__).parent
    if game == "snowrider":
        html_file = ROOT / "games" / "snowrider" / "snowrider.html"
        gamename = "Snow Rider 3D"
    elif game == "Drive_mad":
        html_file = ROOT / "games" / "drivemad" / "drivemad.html"
        gamename = "Drive Mad"


    if html_file.exists():
        print(f"Launching {gamename} in a popup... (Check your taskbar)")

        # This creates the dedicated window
        # width/height can be adjusted to your liking
        window = webview.create_window(
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
        print(f"Error: Could not find {html_file}, which is the core file for {gamename}.")


def games_menu():
    while True:
        clear_screen()
        print("---  PyHub Games Menu  ---")
        print("1. Snow Rider 3D")
        print("2. Drive Mad")
        print("3. Back to Main Menu")
        print("------------------------------")

        choice = input("Select a game to play: ")

        if choice == "1":
            launch_game("snowrider")
            # The script will wait here until you close the popup window
        elif choice == "2":
            launch_game("Drive_mad")
        elif choice == "3":
            print("Returning...")
            break
        else:
            print("Invalid selection. Try again.")
            time.sleep(1)


# Ensure this is NOT inside an 'if __name__ == "__main__":' block
# so runpy can trigger it.
games_menu()