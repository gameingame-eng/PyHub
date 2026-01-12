# Pong (Native C++ Version)

A classic Pong game written in C++ using the SDL2 library. This version runs natively on Windows and includes a Python launcher.

## 📁 Directory Structure
```text
pong/
├── pong.cpp          # Main game logic
├── launcher.py       # Python wrapper to start the game
├── icon.ico          # Game icon
├── resource.rc       # Windows resource script for the icon
├── SDL2.dll          # Required SDL2 library file
└── README.md         # This file
```

## 🛠️ Prerequisites

To build this game, you need the **MinGW-w64** toolchain (installed via MSYS2).

1. **Install MSYS2**: [msys2.org](https://www.msys2.org/)
2. **Install Compiler & SDL2**:
   Open the **MSYS2 UCRT64** terminal and run:
   ```bash
   pacman -S mingw-w64-ucrt-x86_64-gcc mingw-w64-ucrt-x86_64-SDL2
3. **Add to PATH** add this to PATH

## 🚀 How to Build

Run these commands inside the `pong` directory:

1. **Compile the Icon Resource**:
   windres resource.rc -O coff -o resource.res

2. **Compile the Game**:
   g++ pong.cpp resource.res -o pong.exe -lmingw32 -lSDL2main -lSDL2

## 🎮 How to Play

### Option 1: Direct
Double-click `pong.exe`. (Ensure `SDL2.dll` is in the same folder!)

### Option 2: Python Launcher
Run the launcher from the root or the game folder:
```bash
python launcher.py
```
## ⌨️ Controls

| Player | Up | Down |
| :--- | :--- | :--- |
| **Left Paddle (P1)** | `W` | `S` |
| **Right Paddle (P2)** | `UP Arrow` | `DOWN Arrow` |

---
© 2026 Lakshya.  
Licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).