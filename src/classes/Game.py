import pygame
import random
from . import Costants as K
from .Box import Box


class Game():
    def __init__(self) -> None:
        self.life = K.MAX_LIFE
        self.running = True
        self.playing = False
        self.number = random.randint(K.MIN_NUM, K.MAX_NUM)
        self.speach = "Benvenuto, premi \nNUOVA PARTITA \nper giocare!"
        self.new_game_box = Box(250, 70, 30, 50, 35, 55, "NUOVA PARTITA", "green",
                                "grey", "white", "black", True)
        self.stop_game_box = Box(250, 70, 30, 150, 35, 155, "INTERROMPI", "orange",
                                 "grey", "white", "black", False)
        self.exit_box = Box(250, 70, 30, 250, 35, 255, "ESCI", "red",
                            "grey", "white", "black", True)
        self.guess_text = pygame.font.Font(K.FONT, 20).render(
            "Inserisci il numero scelto: ", True, "white")
        self.input_box = Box(250, 60, 400, 90, 205, 95, "", "white",
                             "grey", "black", "black", True)
        self.image = None

    def is_running(self):
        return self.running

    def is_playing(self):
        return self.playing

    def start_game(self):
        self.life = K.MAX_LIFE
        self.number = random.randint(K.MIN_NUM, K.MAX_NUM)
        self.speach = f"Sto pensando ad\nun numero tra \n{K.MIN_NUM} e {K.MAX_NUM}"
        self.input_box.text = ""
        prompt = f"Scegli un numero da {K.MIN_NUM} a {K.MAX_NUM}"
        self.playing = True
        self.stop_game_box.active = True
        self.update_static_boxes()
        self.set_image(self.leo_start)

    def game_over(self):
        self.playing = False
        self.speach = "Peccato.. Hai perso! \nPremi NUOVA PARTITA \nper giocare!"
        prompt = "Hai Perso.."
        self.stop_game_box.active = False
        self.update_static_boxes()
        self.set_image(self.leo_sad)

    def game_win(self):
        self.speach = "Sono sorpreso!\nSei riuscito ad \nindovinare! BRAVO!"
        prompt = "COMPLIMENTI!"
        self.playing = False
        self.stop_game_box.active = False
        self.update_static_boxes()
        self.set_image(self.leo_wow)

    def check_answer(self, guess):
        if guess == "":
            guess = 0
        else:
            guess = int(guess)
        if guess == self.number:
            return 0
        elif guess > self.number:
            return 1
        else:
            return -1

    def eval_guess(self, guess):
        res = self.check_answer(guess)
        if res == 0:
            self.game_win()
        else:
            self.life = self.life - 1
            if self.life == 0:
                self.game_over()
            else:
                self.set_image(self.leo_mmm)
                if res < 0:
                    self.speach = f"Sbagliato: {self.get_input() or 0}\nè più PICCOLO\ndel mio numero!"
                else:
                    self.speach = f"Sbagliato: {self.get_input() or 0}\nè più GRANDE \ndel mio numero!"
        self.set_input("")

    def draw_texts(self, screen, color, x, y):
        lines = self.speach.splitlines()
        for i, l in enumerate(lines):
            screen.blit(pygame.font.Font(K.FONT, K.FONT_SIZE).render(
                l, 0, color), (x, y + K.FONT_SIZE*i))

    def load_images(self):
        w = pygame.display.get_window_size()[0]
        h = pygame.display.get_window_size()[1]
        print(w, h)
        img_width = w *0.48
        img_height = h * 0.8

        bg_image = pygame.image.load("./src/images/bg.jpg").convert()
        self.bg_image = pygame.transform.scale(bg_image, (w, h))
        leo_start = pygame.image.load(
            "./src/images/leo/leo.png").convert_alpha()
        self.leo_start = pygame.transform.scale(leo_start, (img_width, img_height))
        leo_wow = pygame.image.load(
            "./src/images/leo/leo_wow.png").convert_alpha()
        self.leo_wow = pygame.transform.scale(leo_wow, (img_width, img_height))
        leo_mmm = pygame.image.load(
            "./src/images/leo/leo_mmm.png").convert_alpha()
        self.leo_mmm = pygame.transform.scale(leo_mmm, (img_width, img_height))
        leo_sad = pygame.image.load(
            "./src/images/leo/leo_noo.png").convert_alpha()
        self.leo_sad = pygame.transform.scale(leo_sad, (img_width, img_height))
        bubble = pygame.image.load(
            "./src/images/bubble.png").convert_alpha()
        self.bubble = pygame.transform.scale(bubble, (img_width/2, img_height/2))
        if not self.is_playing(): self.set_image(self.leo_start)

    def get_static_boxes(self):
        return [self.new_game_box, self.stop_game_box, self.exit_box]

    def update_static_boxes(self):
        self.new_game_box.set_bg_color()
        self.stop_game_box.set_bg_color()
        self.exit_box.set_bg_color()

    def update_input(self, screen):
            screen.blit(self.guess_text, (400, 70))
            self.input_box.draw(screen)
    def get_input(self):
        return self.input_box.text

    def set_input(self, input):
        if input == "":
            self.input_box.text = ""
        self.input_box.text = input

    def set_image(self, image):
        self.image = image

    def render_window(self, screen):
        screen.blit(self.bg_image, (0, 0))
        w = pygame.display.get_window_size()[0]
        h = pygame.display.get_window_size()[1]
        # Rendering del gioco
        screen.blit(self.image, (700 * w / K.WIDTH, 200 * h / K.HEIGHT))
        screen.blit(self.bubble, (700* w / K.WIDTH, 00 * h / K.HEIGHT))
        self.draw_texts(screen, "black", 755* w / K.WIDTH, 85* w / K.WIDTH)

        if self.is_playing():
            self.update_input(screen)

        # Rendering delle box statiche
        for box in self.get_static_boxes():
            box.draw(screen)

        pygame.display.flip()
        
    def button_hovered(self, pos):
        arr = self.get_static_boxes()
        for box in arr:
            if box.check_clicked(pos) and box.active:
                return True
        return False
