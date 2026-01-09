#include <SDL2/SDL.h>
#include <iostream>
#include <fstream> // For file operations
#include <string>

#undef main  

const int WIDTH = 800;
const int HEIGHT = 600;
const std::string SAVE_PATH = ".\\system_files\\pong_scoreboard.bin";

struct ScoreData {
    int p1 = 0;
    int p2 = 0;
};

// Function to save scores to a binary file
void saveScores(const ScoreData& data) {
    std::ofstream outFile(SAVE_PATH, std::ios::binary);
    if (outFile.is_open()) {
        outFile.write(reinterpret_cast<const char*>(&data), sizeof(ScoreData));
        outFile.close();
    }
}

// Function to load scores from a binary file
ScoreData loadScores() {
    ScoreData data;
    std::ifstream inFile(SAVE_PATH, std::ios::binary);
    if (inFile.is_open()) {
        inFile.read(reinterpret_cast<char*>(&data), sizeof(ScoreData));
        inFile.close();
    }
    return data;
}

void updateConsoleScore(int s1, int s2) {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif

    std::cout << "============================" << std::endl;
    std::cout << "      PONG LEADERBOARD      " << std::endl;
    std::cout << " (Scores Saved to System)   " << std::endl;
    std::cout << "============================" << std::endl;
    std::cout << "  Player 1: " << s1 << " | Player 2: " << s2 << std::endl;
    std::cout << "============================" << std::endl;
}

int main() {
    SDL_Init(SDL_INIT_VIDEO);

    SDL_Window* window = SDL_CreateWindow("Pong - Persistent Leaderboard",
        SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
        WIDTH, HEIGHT, SDL_WINDOW_SHOWN);

    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, 0);

    SDL_Rect p1 = { 50, HEIGHT/2 - 50, 20, 100 };
    SDL_Rect p2 = { WIDTH - 70, HEIGHT/2 - 50, 20, 100 };
    SDL_Rect ball = { WIDTH/2 - 10, HEIGHT/2 - 10, 20, 20 };

    // --- 1. LOAD SAVED DATA ---
    ScoreData scores = loadScores();
    
    // --- 2. LOWERED BALL SPEED ---
    int ballVelX = 2, ballVelY = 2;

    updateConsoleScore(scores.p1, scores.p2);

    bool running = true;
    while (running) {
        SDL_Event e;
        while (SDL_PollEvent(&e)) {
            if (e.type == SDL_QUIT) running = false;
        }

        const Uint8* keys = SDL_GetKeyboardState(NULL);
        if (keys[SDL_SCANCODE_W] && p1.y > 0) p1.y -= 5;
        if (keys[SDL_SCANCODE_S] && p1.y < HEIGHT - p1.h) p1.y += 5;
        if (keys[SDL_SCANCODE_UP] && p2.y > 0) p2.y -= 5;
        if (keys[SDL_SCANCODE_DOWN] && p2.y < HEIGHT - p2.h) p2.y += 5;

        ball.x += ballVelX;
        ball.y += ballVelY;

        if (ball.y <= 0 || ball.y >= HEIGHT - ball.h)
            ballVelY = -ballVelY;

        if (SDL_HasIntersection(&ball, &p1) || SDL_HasIntersection(&ball, &p2))
            ballVelX = -ballVelX;

        // --- 3. SCORING & SAVING ---
        if (ball.x < 0) {
            scores.p2++;
            saveScores(scores); // Save to .bin file
            updateConsoleScore(scores.p1, scores.p2);
            ball = { WIDTH/2 - 10, HEIGHT/2 - 10, 20, 20 };
            ballVelX = 2; 
        }
        if (ball.x > WIDTH) {
            scores.p1++;
            saveScores(scores); // Save to .bin file
            updateConsoleScore(scores.p1, scores.p2);
            ball = { WIDTH/2 - 10, HEIGHT/2 - 10, 20, 20 };
            ballVelX = -2;
        }

        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderClear(renderer);
        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
        SDL_RenderFillRect(renderer, &p1);
        SDL_RenderFillRect(renderer, &p2);
        SDL_RenderFillRect(renderer, &ball);
        SDL_RenderPresent(renderer);

        SDL_Delay(10); 
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}