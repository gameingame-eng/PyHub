import pygame
import random
import os
import sys

pygame.init()

# Window + grid settings
WIDTH, HEIGHT = 600, 600
CELL = 20
GRID_WIDTH = WIDTH // CELL
GRID_HEIGHT = HEIGHT // CELL

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

# Colors
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Load and scale apple image
APPLE_PATH = os.path.join(
    "features", "GameHub", "games", "snake", "img", "apple.png"
)

apple_img = pygame.image.load(APPLE_PATH).convert_alpha()
apple_img = pygame.transform.scale(apple_img, (CELL, CELL))  # auto-fit 255→20px


def draw_rect(color, pos):
    pygame.draw.rect(screen, color, (pos[0] * CELL, pos[1] * CELL, CELL, CELL))


def snake_game():
    snake = [(10, 10), (9, 10), (8, 10)]
    direction = (1, 0)
    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)

        # Move snake
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        # Wall collision
        if not (0 <= new_head[0] < GRID_WIDTH and 0 <= new_head[1] < GRID_HEIGHT):
            return score

        # Self collision
        if new_head in snake:
            return score

        snake.insert(0, new_head)

        # Food collision
        if new_head == food:
            score += 1
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        else:
            snake.pop()

        # Draw everything
        screen.fill(BLACK)

        # Draw snake
        for segment in snake:
            draw_rect(GREEN, segment)

        # Draw apple image
        screen.blit(apple_img, (food[0] * CELL, food[1] * CELL))

        pygame.display.flip()
        clock.tick(10)  # speed


print("Score:", snake_game())
