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
            if game.new_game_box.check_clicked(event.pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h),
                                             pygame.RESIZABLE)
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
    screen.blit(game.bg_image, (0, 0))

    # Rendering del gioco
    screen.blit(game.image, (700, 200))
    screen.blit(game.bubble, (700, 00))
    game.draw_texts(screen, "black", 755, 85)

    if game.is_playing():
        screen.blit(game.guess_text, (400, 70))
        game.input_box.draw(screen)

    # Rendering delle box statiche
    for box in static_boxes:
        box.draw(screen)

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
