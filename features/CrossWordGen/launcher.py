import subprocess
import os

def launch_crossword():
    exe_path = os.path.join(os.path.dirname(__file__), "crossword.exe")
    working_dir = os.path.dirname(exe_path)

    if os.path.exists(exe_path):
        try:
            subprocess.Popen([exe_path], cwd=working_dir)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"File not found: {exe_path}")

if __name__ == "__main__":
    launch_crossword()