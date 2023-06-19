import pygame
from . import Costants as K


class Box():
    def __init__(self, w, h, x, y, text_x, text_y, text, bg_color_active, bg_color_non_active, text_color, border_color, is_active) -> None:
        self.x = x
        self.y = y
        self.width = w
        self.heigth = h
        self.text_x = text_x
        self.text_y = text_y
        self.active = is_active
        self.bg_color_active = bg_color_active
        self.bg_color_non_active = bg_color_non_active
        self.text_color = text_color
        self.text = text
        self.bg_color = self.bg_color_active if self.active else self.bg_color_non_active
        self.border_color = border_color
        self.box_item = pygame.Rect(self.x, self.y, self.width, self.heigth)

    def draw_box(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.box_item, 0, 10)

    def draw_text(self, screen):
        t = pygame.font.Font(K.FONT, K.FONT_SIZE).render(
            self.text, True, "black")
        t_rect = t.get_rect(center=self.box_item.center)
        screen.blit(t, t_rect)

    def draw(self, screen):
        self.draw_box(screen)
        self.draw_text(screen)

    def update_text(self, t):
        self.text = t

    def change_active(self):
        self.active = not self.active
        self.set_bg_color()

    def is_active(self):
        return self.active

    def remove_active(self):
        self.active = False
        self.set_bg_color()

    def set_bg_color(self):
        self.bg_color = self.bg_color_active if self.active else self.bg_color_non_active

    def check_clicked(self, pos):
        return self.box_item.collidepoint(pos)

    def is_hovered(self, pos):
        return self.box_item.collidepoint(pos)
