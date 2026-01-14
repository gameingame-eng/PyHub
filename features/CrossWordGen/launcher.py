import subprocess
import os
import sys

def launch_crossword():
    base_path = os.path.dirname(os.path.abspath(__file__))
    exe_path = os.path.join(base_path, "crossword.exe")
    working_dir = os.path.join(base_path, "features", "CrossWordGen")

    if os.path.exists(exe_path):
        try:
            subprocess.Popen([exe_path], cwd=working_dir)
        except Exception as e:
            print(f"Error launching executable: {e}")
    else:
        print(f"Executable not found at: {exe_path}")


if __name__ == "__main__":
    launch_crossword()
    input("Press Enter to continue...")