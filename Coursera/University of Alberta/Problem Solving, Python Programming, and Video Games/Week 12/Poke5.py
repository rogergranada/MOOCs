# Poke the Dots version 5
# This is a graphical game where two dots move on
# the screen, bouncing off the edges.

from uagame import Window
from pygame import time
from pygame.time import Clock
from pygame.event import get as get_events
from pygame import QUIT, Color, MOUSEBUTTONUP
from pygame.draw import circle as draw_circle
import random
from math import sqrt

def main():
    # Create game
    game = Game()
    game.play()

class Game:
    # An object in this class represents a complete game
    # - window
    # - frame_rate
    # - close_selected
    # - clock
    # - small_dot
    # - big_dot
    def __init__(self):
        self._window = Window('Poke the Dots', 500, 400)
        self._clock = Clock()
        self._frame_rate = 90
        self._close_selected = False
        self._small_dot = Dot('red', [200, 100], 20, [1, 2], self._window)
        self._small_dot.randomize()
        self._big_dot = Dot('blue', [200, 100], 40, [2, 1], self._window)
        self._big_dot.randomize()
        self._score = 0
        self._continue = True
        self._adjust_window()
    
    def _adjust_window(self):
        # set parameters to the window
        self._window.set_font_name('ariel')
        self._window.set_font_size(64)
        self._window.set_font_color('white')
        self._window.set_bg_color('black')

    def _draw(self):
        # draw small and big dots on the screen and update the window
        self._window.clear()
        self._draw_score()
        self._small_dot.draw()
        self._big_dot.draw()
        if not self._continue:
            self._draw_game_over()
        self._window.update()

    def _draw_score(self):
        # draw the score on the screen
        self._window.draw_string('Score: '+str(self._score), 0, 0)

    def _draw_game_over(self):
        # draw GAME OVER when the balls collide
        small_color = self._small_dot.get_color()
        big_color = self._big_dot.get_color()
        font_color = self._window.get_font_color()
        bg_color = self._window.get_bg_color()
        self._window.set_font_color(small_color)
        self._window.set_bg_color(big_color)
        height = self._window.get_height() - self._window.get_font_height()
        self._window.draw_string('GAME OVER', 0, height)
        self._window.set_font_color(font_color)
        self._window.set_bg_color(bg_color)

    def _handle_events(self):
        # handle the exit game event when the player clicks [X]
        event_list = get_events()
        for event in event_list:
            if event.type == QUIT:
                self._close_selected = True
            elif event.type == MOUSEBUTTONUP and self._continue:
                self._small_dot.randomize()
                self._big_dot.randomize()

    def play(self):
        # run the game while the player do not select to close the window
        while not self._close_selected:
            self._handle_events()
            self._draw()
            self._update()
        self._window.close()

    def _update(self):
        # control the frame rate and update the movement of the dots
        if self._continue:
            self._small_dot.move()
            self._big_dot.move()
            self._score = time.get_ticks() // 1000
        self._clock.tick(self._frame_rate)
        if self._small_dot.intersects(self._big_dot):
            self._continue = False
            

class Dot:
    # window is the Window to display in
    # - color is the string representing the color of the small dot
    # - center is a list representing the X and Y positions of the center of the small dot
    # - radius is an int representing the radius of the small dot
    # - velocity is a list representing the velocity in X and Y of the small dot
    # - clock is the Clock object representing time
    def __init__(self, color, center, radius, velocity, window):
        self._color = color
        self._center = center
        self._radius = radius
        self._velocity = velocity
        self._window = window

    def get_color(self):
        # return the color of the font
        return self._color

    def get_center(self):
        # return the center of the dot
        return self._center

    def get_radius(self):
        # return the radius of the dot
        return self._radius

    def draw(self):
        # draw the dot on the screen
        surface = self._window.get_surface()
        color = Color(self._color)
        draw_circle(surface, color, self._center, self._radius)

    def move(self):
        # update the movement of the dot in each axis X and Y
        size = [self._window.get_width(), self._window.get_height()]
        for index in range(0, 2):
            # 0 horizontal, 1 vertical
            self._center[index] = self._center[index] + self._velocity[index]
            if self._center[index] + self._radius >= size[index] or self._center[index] - self._radius <= 0:
                self._velocity[index] = - self._velocity[index]

    def randomize(self):
        # randomize the position of Dot
        size = [self._window.get_width(), self._window.get_height()]
        for index in range(0, 2):
            self._center[index] = random.randint(0+self._radius, size[index])

    def intersects(self, dot):
        # check whether two dots intersect
        distance = 0
        for index in range(0, 2):
            distance += (self._center[index] - dot.get_center()[index])**2
        sum_radius = self._radius + dot.get_radius()
        if sqrt(distance) <= sum_radius:
            return True
        return False

main()
