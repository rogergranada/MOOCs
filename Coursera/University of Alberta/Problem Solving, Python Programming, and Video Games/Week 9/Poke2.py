# Poke the Dots version 2
# This is a graphical game where two dots move on
# the screen, bouncing off the edges.

from uagame import Window
from pygame.time import Clock
from pygame.event import get as get_events
from pygame import QUIT, Color
from pygame.draw import circle as draw_circle

def main():
    # Create game
    window = create_window()
    game = create_game(window)
    play_game(game)
    window.close()

def create_window():
    # Create a window for the game, open it, and return it
    window = Window('Poke the Dots', 500, 400)
    window.set_bg_color('black')
    return window 

def create_game(window):
    # Create a Game object for Poke the Dots 
    # - window is the Window we draw in
    game = Game()
    game.window = window
    game.clock = Clock()
    game.frame_rate = 90
    game.close_selected = False
    game.small_dot = create_dot(window, 'red', 20, [200, 100], [1, 2])
    game.big_dot = create_dot(window, 'blue', 40, [200, 100], [2, 1])
    return game

def create_dot(window, color, radius, center, velocity):
    # create a Dot using specific information
    # - color is a str representing the color of the dot
    # radius is an int representing the radius of the dot
    # center is a list representing the X and Y positions of the center of the dot
    # velocity is a list representing the velocity in X and Y of the dot
    dot = Dot()
    dot.window = window
    dot.color = color
    dot.radius = radius
    dot.center = center
    dot.velocity = velocity
    return dot

def play_game(game):
    # run the game while the player do not select to close the window
    # - game is the Game to play
    while not game.close_selected:
        handle_events(game)
        draw_game(game)
        update_game(game)

def handle_events(game):
    # handle the exit game event when the player clicks [X]
    # - game is the Game whose events should be handled
    event_list = get_events()
    for event in event_list:
        if event.type == QUIT:
            game.close_selected = True

def draw_game(game):
    # draw small and big dots on the screen and update the window
    # - game is the Game where the dot should be drawn
    game.window.clear()
    draw_dot(game.big_dot)
    draw_dot(game.small_dot)
    game.window.update()

def draw_dot(dot):
    # draw the dot on the screen
    # - game is the Game where the dot should be drawn
    # - dot is the Dot containing information to be drawn 
    surface = dot.window.get_surface()
    color = Color(dot.color)
    draw_circle(surface, color, dot.center, dot.radius)

def update_game(game):
    # control the frame rate and update the movement of the dots
    # - game is the Game to be updated
    move_dot(game.big_dot)
    move_dot(game.small_dot)
    game.clock.tick(game.frame_rate)

def move_dot(dot):
    # update the movement of the dot in each axis X and Y
    # - game is the Game containing the screen
    # - dot is the Dot to be moved
    size = [dot.window.get_width(), dot.window.get_height()]
    for index in range(0, 2):
        # 0 horizontal, 1 vertical
        dot.center[index] = dot.center[index] + dot.velocity[index]
        if dot.center[index] + dot.radius >= size[index] or dot.center[index] - dot.radius <= 0:
            dot.velocity[index] = - dot.velocity[index]

class Game:
    # An object in this class represents a complete game
    # - window
    # - frame_rate
    # - close_selected
    # - clock
    # - small_dot
    # - big_dot
    pass

class Dot:
    # window is the Window to display in
    # - color is the string representing the color of the small dot
    # - center is a list representing the X and Y positions of the center of the small dot
    # - radius is an int representing the radius of the small dot
    # - velocity is a list representing the velocity in X and Y of the small dot
    # - clock is the Clock object representing time
    pass

main()
