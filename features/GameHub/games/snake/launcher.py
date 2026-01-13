import subprocess
import os

snake_path = os.path.abspath("features/GameHub/games/snake/snake.py")
result = subprocess.run(
    ["python", snake_path],
    capture_output=True,
    text=True
)
score = result.stdout.strip()

os.makedirs("system_files", exist_ok=True)

with open("system_files/snakescore.bin", "wb") as f:
    f.write(score.encode("utf-8"))

print("Snake score saved:", score)


