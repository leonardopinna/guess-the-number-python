import pygame
import classes.Costants as K
from classes.Game import Game
from classes.Box import Box

# Initializzo PYGAME
pygame.init()
screen = pygame.display.set_mode((K.WIDTH, K.HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()

# Inizializzo gioco
game = Game()
game.load_images()

static_boxes = game.get_static_boxes()

while game.is_running():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            if game.button_hovered(event.pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h),
                                             pygame.RESIZABLE)
            game.load_images()
        if event.type == pygame.QUIT:
            game.running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game.exit_box.check_clicked(event.pos):
                game.running = False
            if not game.is_playing():
                if game.new_game_box.check_clicked(event.pos):
                    game.start_game()
            elif game.is_playing():
                if game.new_game_box.check_clicked(event.pos):
                    game.start_game()
                if game.stop_game_box.check_clicked(event.pos):
                    game.game_over()

        if event.type == pygame.KEYDOWN:
            if game.input_box.is_active() and game.is_playing():
                if event.key == pygame.K_RETURN:
                    game.eval_guess(game.get_input())
                elif event.key == pygame.K_BACKSPACE:
                    game.set_input(game.get_input()[:-1])
                elif event.unicode.isdigit():
                    game.set_input(
                        game.get_input()+event.unicode)

    # RENDERING
    game.render_window(screen)
    
    pygame.display.flip()

    clock.tick(15) 

pygame.quit()
