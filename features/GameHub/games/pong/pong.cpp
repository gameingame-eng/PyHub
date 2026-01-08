#include <SDL2/SDL.h>

const int WIDTH = 800;
const int HEIGHT = 600;

int main() {
    SDL_Init(SDL_INIT_VIDEO);

    SDL_Window* window = SDL_CreateWindow("Pong",
        SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
        WIDTH, HEIGHT, SDL_WINDOW_SHOWN);

    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, 0);

    SDL_Rect p1 = { 50, HEIGHT/2 - 50, 20, 100 };
    SDL_Rect p2 = { WIDTH - 70, HEIGHT/2 - 50, 20, 100 };
    SDL_Rect ball = { WIDTH/2 - 10, HEIGHT/2 - 10, 20, 20 };

    int ballVelX = 4, ballVelY = 4;
    bool running = true;

    while (running) {
        SDL_Event e;
        while (SDL_PollEvent(&e)) {
            if (e.type == SDL_QUIT)
                running = false;
        }

        const Uint8* keys = SDL_GetKeyboardState(NULL);

        // Player 1: W/S
        if (keys[SDL_SCANCODE_W] && p1.y > 0) p1.y -= 5;
        if (keys[SDL_SCANCODE_S] && p1.y < HEIGHT - p1.h) p1.y += 5;

        // Player 2: Up/Down
        if (keys[SDL_SCANCODE_UP] && p2.y > 0) p2.y -= 5;
        if (keys[SDL_SCANCODE_DOWN] && p2.y < HEIGHT - p2.h) p2.y += 5;

        // Ball movement
        ball.x += ballVelX;
        ball.y += ballVelY;

        // Bounce top/bottom
        if (ball.y <= 0 || ball.y >= HEIGHT - ball.h)
            ballVelY = -ballVelY;

        // Bounce paddles
        if (SDL_HasIntersection(&ball, &p1) || SDL_HasIntersection(&ball, &p2))
            ballVelX = -ballVelX;

        // Reset if out of bounds
        if (ball.x < 0 || ball.x > WIDTH)
            ball = { WIDTH/2 - 10, HEIGHT/2 - 10, 20, 20 };

        // Draw
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderClear(renderer);

        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
        SDL_RenderFillRect(renderer, &p1);
        SDL_RenderFillRect(renderer, &p2);
        SDL_RenderFillRect(renderer, &ball);

        SDL_RenderPresent(renderer);

        SDL_Delay(16);
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}
