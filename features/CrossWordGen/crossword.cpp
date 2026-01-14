#include "raylib.h"
#include <vector>
#include <string>
#include <algorithm>

const int GRID_SIZE = 10;
const int CELL_SIZE = 50;

struct Cell {
    char letter = ' ';
    bool isBlack = false;
};

// Simple check if word fits horizontally
bool canPlaceHorizontal(std::vector<std::vector<Cell>>& grid, std::string word, int r, int c) {
    if (c + word.length() > GRID_SIZE) return false;
    for (int i = 0; i < word.length(); i++) {
        if (grid[r][c + i].letter != ' ' && grid[r][c + i].letter != word[i]) return false;
    }
    return true;
}

void placeHorizontal(std::vector<std::vector<Cell>>& grid, std::string word, int r, int c) {
    for (int i = 0; i < word.length(); i++) grid[r][c + i].letter = word[i];
}

int main() {
    // 1. Setup Data
    std::vector<std::vector<Cell>> grid(GRID_SIZE, std::vector<Cell>(GRID_SIZE));
    std::vector<std::string> words = {"PYHUB", "RUST", "CODE", "CPP"};
    
    // Quick Demo: Place a few words
    placeHorizontal(grid, "PYHUB", 2, 2);
    placeHorizontal(grid, "CPP", 4, 2);

    // 2. Init Window
    InitWindow(GRID_SIZE * CELL_SIZE + 100, GRID_SIZE * CELL_SIZE + 100, "PyHub Crossword Gen");
    SetTargetFPS(60);

    while (!WindowShouldClose()) {
        BeginDrawing();
            ClearBackground(RAYWHITE);
            DrawText("PYHUB CROSSWORD", 20, 20, 20, DARKGRAY);

            for (int r = 0; r < GRID_SIZE; r++) {
                for (int c = 0; c < GRID_SIZE; c++) {
                    int x = c * CELL_SIZE + 50;
                    int y = r * CELL_SIZE + 50;
                    
                    // Draw Square
                    DrawRectangleLines(x, y, CELL_SIZE, CELL_SIZE, BLACK);
                    
                    // Draw Letter
                    if (grid[r][c].letter != ' ') {
                        char str[2] = {grid[r][c].letter, '\0'};
                        DrawText(str, x + 15, y + 10, 30, BLUE);
                    }
                }
            }
        EndDrawing();
    }

    CloseWindow();
    return 0;
}