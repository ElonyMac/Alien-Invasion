import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


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
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Rozpoczecie petli glownej gry."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            # Odswiezanie ekranu w trakcie kazdej iteracji petli.

    def _check_events(self):
        """Reakcja na zdarzenia generowane przez klawiature i mysz"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Reakcja na nacisniecie klawisza."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Reakcja na zwolnienie klawisza."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_q:
            sys.exit()

    def _fire_bullet(self):
        """Utworzenie nowego pocisku i dodanie go do grupy pociskow."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Uaktualnienie polozenia pociskow i usun iecie tych niewidocznych na ekranie"""
        # Uaktualnieni polozenia pociskow.
        self.bullets.update()

        # Usuniecie pociskow, ktore znajduja sie poza ekranem.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

        # Usuniecie pociskow, ktore znajduja sie poza ekranem.


    def _update_screen(self):
        """Uaktualnienie obrazow na ekranie i przejscie do nowego ekranu"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()


        # Wyswietlanie ostatnio zmodyfikowanego ekranu.
        pygame.display.flip()


if __name__ == '__main__':
    # Utworzenie egzemplarza gry i jej uruchomienie.
    ai = AlienInvasion()
    ai.run_game()
