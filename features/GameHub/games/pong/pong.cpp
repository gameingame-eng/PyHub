#include <SDL2/SDL.h>
#include <iostream>
#include <fstream>
#include <string>

#undef main  

const int WIDTH = 800;
const int HEIGHT = 600;
const std::string SAVE_PATH = ".\\system_files\\pong_scoreboard.bin";

struct ScoreData {
    int p1 = 0;
    int p2 = 0;
};

// --- UPDATED: APPENDS TO FILE INSTEAD OF OVERWRITING ---
void saveScores(const ScoreData& data) {
    // std::ios::app ensures every save is a new entry at the end of the file
    std::ofstream outFile(SAVE_PATH, std::ios::binary | std::ios::app); 
    if (outFile.is_open()) {
        outFile.write(reinterpret_cast<const char*>(&data), sizeof(ScoreData));
        outFile.close();
    }
}

void updateConsoleScore(int s1, int s2) {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif

    std::cout << "============================" << std::endl;
    std::cout << "      PONG SESSION LIVE     " << std::endl;
    std::cout << " (Appending to System Log)  " << std::endl;
    std::cout << "============================" << std::endl;
    std::cout << "  Player 1: " << s1 << " | Player 2: " << s2 << std::endl;
    std::cout << "============================" << std::endl;
}

int main() {
    if (SDL_Init(SDL_INIT_VIDEO) < 0) return -1;

    SDL_Window* window = SDL_CreateWindow("Pong - Multi-Entry Leaderboard",
        SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
        WIDTH, HEIGHT, SDL_WINDOW_SHOWN);

    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);

    SDL_Rect p1 = { 50, HEIGHT/2 - 50, 20, 100 };
    SDL_Rect p2 = { WIDTH - 70, HEIGHT/2 - 50, 20, 100 };
    SDL_Rect ball = { WIDTH/2 - 10, HEIGHT/2 - 10, 20, 20 };

    // Start with a fresh score for this specific session
    ScoreData sessionScores = {0, 0};
    
    // --- DECREASED BALL SPEED ---
    int ballVelX = 2, ballVelY = 2;

    updateConsoleScore(sessionScores.p1, sessionScores.p2);

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

        // Wall Collision
        if (ball.y <= 0 || ball.y >= HEIGHT - ball.h)
            ballVelY = -ballVelY;

        // Paddle Collision
        if (SDL_HasIntersection(&ball, &p1) || SDL_HasIntersection(&ball, &p2))
            ballVelX = -ballVelX;

        // Scoring Logic
        if (ball.x < 0) {
            sessionScores.p2++;
            saveScores(sessionScores); // Writes a new 8-byte entry to the file
            updateConsoleScore(sessionScores.p1, sessionScores.p2);
            ball = { WIDTH/2 - 10, HEIGHT/2 - 10, 20, 20 };
            ballVelX = 2; 
        }
        if (ball.x > WIDTH) {
            sessionScores.p1++;
            saveScores(sessionScores); // Writes a new 8-byte entry to the file
            updateConsoleScore(sessionScores.p1, sessionScores.p2);
            ball = { WIDTH/2 - 10, HEIGHT/2 - 10, 20, 20 };
            ballVelX = -2;
        }

        // Render
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