#include "raylib.h"
#include <vector>
#include <string>
#include <fstream>

const int GRID_SIZE = 12;
const int CELL_SIZE = 45;

struct Cell {
    char letter = ' ';
    bool isActive = false;
};

void SaveToJson(const std::vector<std::vector<Cell>>& grid) {
    std::ofstream file("crossword.json");
    file << "{\n  \"grid_size\": " << GRID_SIZE << ",\n  \"cells\": [\n";
    bool first = true;
    for (int r = 0; r < GRID_SIZE; r++) {
        for (int c = 0; c < GRID_SIZE; c++) {
            if (grid[r][c].isActive) {
                if (!first) file << ",\n";
                file << "    {\"r\": " << r << ", \"c\": " << c << ", \"char\": \"" << grid[r][c].letter << "\"}";
                first = false;
            }
        }
    }
    file << "\n  ]\n}";
    file.close();
}

int main() {
    InitWindow(GRID_SIZE * CELL_SIZE + 100, GRID_SIZE * CELL_SIZE + 150, "PyHub - Crossword Creator");
    
    Image icon = LoadImage("favicon.ico");
    if (icon.data != NULL) {
        SetWindowIcon(icon);
        UnloadImage(icon);
    }

    SetTargetFPS(60);

    std::vector<std::vector<Cell>> grid(GRID_SIZE, std::vector<Cell>(GRID_SIZE));

    int selectedR = 0;
    int selectedC = 0;
    std::string statusMsg = "Type to place letters | Press S to Save to JSON";

    while (!WindowShouldClose()) {
        if (IsKeyPressed(KEY_RIGHT) && selectedC < GRID_SIZE - 1) selectedC++;
        if (IsKeyPressed(KEY_LEFT) && selectedC > 0) selectedC--;
        if (IsKeyPressed(KEY_UP) && selectedR > 0) selectedR--;
        if (IsKeyPressed(KEY_DOWN) && selectedR < GRID_SIZE - 1) selectedR++;

        if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON)) {
            Vector2 mousePos = GetMousePosition();
            int c = (mousePos.x - 50) / CELL_SIZE;
            int r = (mousePos.y - 80) / CELL_SIZE;
            if (r >= 0 && r < GRID_SIZE && c >= 0 && c < GRID_SIZE) {
                selectedR = r;
                selectedC = c;
            }
        }

        int key = GetCharPressed();
        if ((key >= 32) && (key <= 125)) {
            grid[selectedR][selectedC].letter = (char)toupper(key);
            grid[selectedR][selectedC].isActive = true;
        }

        if (IsKeyPressed(KEY_BACKSPACE) || IsKeyPressed(KEY_DELETE)) {
            grid[selectedR][selectedC].letter = ' ';
            grid[selectedR][selectedC].isActive = false;
        }

        if (IsKeyPressed(KEY_S)) {
            SaveToJson(grid);
            statusMsg = "Saved to crossword.json!";
        }

        BeginDrawing();
            ClearBackground(RAYWHITE);
            DrawText("CROSSWORD CREATOR MODE", 20, 20, 20, MAROON);
            DrawText(statusMsg.c_str(), 20, 45, 15, DARKGRAY);

            for (int r = 0; r < GRID_SIZE; r++) {
                for (int c = 0; c < GRID_SIZE; c++) {
                    int x = c * CELL_SIZE + 50;
                    int y = r * CELL_SIZE + 80;

                    Color boxColor = grid[r][c].isActive ? WHITE : BLACK;
                    if (r == selectedR && c == selectedC) boxColor = YELLOW;

                    DrawRectangle(x, y, CELL_SIZE, CELL_SIZE, boxColor);
                    DrawRectangleLines(x, y, CELL_SIZE, CELL_SIZE, GRAY);

                    if (grid[r][c].isActive) {
                        char txt[2] = {grid[r][c].letter, '\0'};
                        DrawText(txt, x + 15, y + 10, 25, BLACK);
                    }
                }
            }
            
            DrawText("Arrows/Click to Navigate", 20, 560, 15, DARKGRAY);
        EndDrawing();
    }

    CloseWindow();
    return 0;
}