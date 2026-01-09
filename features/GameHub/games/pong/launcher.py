import subprocess
import os
import struct
import time

def get_paths():
    # Dynamic pathing for runpy compatibility
    current_dir = os.path.dirname(os.path.abspath(__file__))
    exe_path = os.path.join(current_dir, "pong.exe")
    data_path = os.path.join(".\system_files", "pong_scoreboard.bin")
    return exe_path, data_path

def view_data(data_path):
    # This function now blocks with an input() to prevent flashing
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*30)
    print("      HISTORIC PLAY DATA")
    print("="*30)
    
    if os.path.exists(data_path):
        try:
            with open(data_path, "rb") as f:
                entry_num = 1
                while True:
                    raw_bytes = f.read(8)
                    if not raw_bytes or len(raw_bytes) < 8:
                        break
                    p1, p2 = struct.unpack('ii', raw_bytes)
                    print(f" Match {entry_num:03}: P1 [{p1}] | P2 [{p2}]")
                    entry_num += 1
        except Exception as e:
            print(f" Error: {e}")
    else:
        print(" No saved entries found.")
    
    print("="*30)
    input("\nPAUSED: Press Enter to return to menu...")

def menu():
    exe_path, data_path = get_paths()
    
    while True: # Keep the menu alive
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- PONG LAUNCHER MENU ---")
        print("1. Launch Game")
        print("2. View All Saved Entries")
        print("3. Exit to Main Script")
        
        choice = input("\nSelect (1-3): ")

        if choice == '1':
            if os.path.exists(exe_path):
                print("\nLaunching... Close game window to return.")
                subprocess.run([exe_path])
            else:
                print(f"\nError: {exe_path} missing.")
                time.sleep(2)
        
        elif choice == '2':
            view_data(data_path) # Goes to the blocking view_data function
            
        elif choice == '3':
            print("\nReturning to caller...")
            break # This is the ONLY way to exit back to your runpy script
        
        else:
            print("\nInvalid input.")
            time.sleep(1)

# Critical: This ensures the menu starts whether run directly or via runpy
if __name__ == "__main__":
    menu()
else:
    # This handles the runpy case where __name__ might change
    menu()

"""
© 2026 Lakshya.  
Licensed under CC BY-NC 4.0.  
https://creativecommons.org/licenses/by-nc/4.0/
"""