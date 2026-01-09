import subprocess
import os
import struct
import time

def get_paths():
    # Using __file__ ensures paths work even when called via runpy
    current_dir = os.path.dirname(os.path.abspath(__file__))
    exe_path = os.path.join(current_dir, "pong.exe")
    data_path = os.path.join(".\system_files", "pong_scoreboard.bin")
    return exe_path, data_path

def view_data(data_path):
    print("\n" + "="*30)
    print("      LIFETIME SCORES")
    print("="*30)
    
    if os.path.exists(data_path):
        try:
            with open(data_path, "rb") as f:
                # 'ii' = two 4-byte integers (Player 1, Player 2)
                raw_data = f.read(8)
                if len(raw_data) == 8:
                    p1_score, p2_score = struct.unpack('ii', raw_data)
                    print(f" Player 1: {p1_score} points")
                    print(f" Player 2: {p2_score} points")
                else:
                    print(" [!] Save file format is invalid.")
        except Exception as e:
            print(f" [!] Error reading file: {e}")
    else:
        print(" [i] No saved data found yet.")
    
    print("="*30)
    input("\nPress Enter to return to menu...") # Keeps the data on screen

def menu():
    exe_path, data_path = get_paths()
    
    while True:
        # Clear console for a clean menu look
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("=== PONG MASTER INTERFACE ===")
        print("1. Start Pong (pong.exe)")
        print("2. View Saved Play Data")
        print("3. Return to Main Script")
        
        choice = input("\nSelect Option: ")

        if choice == '1':
            if os.path.exists(exe_path):
                print(f"\n[SYSTEM] Launching {exe_path}...")
                subprocess.run([exe_path])
            else:
                print(f"\n[ERROR] {exe_path} not found!")
                time.sleep(2)
        
        elif choice == '2':
            view_data(data_path)
            
        elif choice == '3':
            print("\nReturning to original script...")
            break # This allows runpy to finish and return to caller
        
        else:
            print("\nInvalid selection!")
            time.sleep(1)

# This check ensures it runs whether called directly or via runpy
if __name__ == "__main__" or __name__ == "run_path_name":
    menu()
else:
    # If runpy is used, it usually executes the module code directly
    menu()

"""
© 2026 Lakshya.  
Licensed under CC BY-NC 4.0.  
https://creativecommons.org/licenses/by-nc/4.0/
"""