import pygame

from game.snake_game import SnakeGame

if __name__ == '__main__':
    pygame.init()

    font = pygame.font.Font('arial.ttf', 25)

    game = SnakeGame()

    # game loop
    while True:
        game_over, score = game.play_step(font)

        if game_over == True:
            break

    print('Final Score', score)

    pygame.quit()