import pygame as pg

from typing import List, Tuple

import gamerules as gr

pg.init()

try:
    FIELD_IMG = pg.image.load(r"img\field.png")
    FIELD_IMG = pg.transform.scale(FIELD_IMG, gr.DISPLAY_SIZE)
except FileNotFoundError:
    FIELD_IMG = None


class Pixel:
    def __init__(self, row: int, col: int, color: str):
        self.cords: Tuple[int, int] = (row, col)
        cords = self.get_cords()
        self.rect = pg.Rect((cords[0], cords[1], gr.PIXEL_SIZE - 1, gr.PIXEL_SIZE - 1))
        self.color = pg.Color(color)

    def get_cords(self) -> Tuple[int, int]:
        return (
            gr.PIXEL_SIZE * 2 + gr.PIXEL_SIZE * self.cords[0] + 1,
            gr.PIXEL_SIZE * 2 + gr.PIXEL_SIZE * self.cords[1] + 1,
        )

    def draw(self, screen: pg.Surface):
        pg.draw.rect(surface=screen, color=self.color, rect=self.rect)


class Field:
    def __init__(self):
        self.apples: List[Tuple[int, int]] = []  # Координаты яблок
        self._pixels: List[Pixel] = []

    def draw_grid(self, screen: pg.Surface):
        if FIELD_IMG:
            screen.blit(FIELD_IMG, (0, 0))
        else:
            if len(self._pixels) == 0:
                self.generate_pixels()
            for pixel in self._pixels:
                pixel.draw(screen)

    def generate_pixels(self):
        for i in range(-2, 37):
            for j in range(-2, 0):
                self._pixels.append(Pixel(i, j, "Gray"))
        for i in range(-2, 37):
            for j in range(35, 37):
                self._pixels.append(Pixel(i, j, "Gray"))
        for i in range(0, 35):
            for j in range(-2, 0):
                self._pixels.append(Pixel(j, i, "Gray"))
        for i in range(0, 35):
            for j in range(35, 37):
                self._pixels.append(Pixel(j, i, "Gray"))
