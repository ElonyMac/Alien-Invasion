import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Ogolna klasa przeznaczona do zarzadzania zasobami i sposobem
    dzialania gry."""

    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobow."""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Rozpoczecie petli glownej gry."""
        while True:
            self._check_events()
            self._update_screen()
            # Odswiezanie ekranu w trakcie kazdej iteracji petli.

    def _check_events(self):
        """Reakcja na zdarzenia generowane przez klawiature i mysz"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Uaktualnienie obrazow na ekranie i przejscie do nowego ekranu"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Wyswietlanie ostatnio zmodyfikowanego ekranu.
        pygame.display.flip()


if __name__ == '__main__':
    # Utworzenie egzemplarza gry i jej uruchomienie.
    ai = AlienInvasion()
    ai.run_game()
