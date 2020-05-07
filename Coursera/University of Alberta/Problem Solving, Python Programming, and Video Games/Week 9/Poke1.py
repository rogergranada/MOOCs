# Poke the Dots version 1
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
    clock = Clock()

    # - Create small dot
    small_color = 'red'
    small_radius = 20
    small_center = [200,100]
    small_velocity = [1, 2]
    # - Create big dot
    big_color = 'blue'
    big_radius = 40
    big_center = [200,100]
    big_velocity = [2, 1]

    play_game(window, big_color, big_center, big_radius, big_velocity, 
             small_color, small_center, small_radius, small_velocity, clock)
    window.close()

def create_window():
    # Create a window for the game, open it, and return it
    window = Window('Poke the Dots', 500, 400)
    window.set_bg_color('black')
    return window 

def play_game(window, big_color, big_center, big_radius, big_velocity, 
              small_color, small_center, small_radius, small_velocity, clock):
    # run the game while the player do not select to close the window
    #
    # window is the Window to display in
    # big_color is the string representing the color of the big dot
    # big_center is a list representing the X and Y positions of the center of the big dot
    # big_radius is an int representing the radius of the big dot
    # big_velocity is a list representing the velocity in X and Y of the big dot
    # small_color is the string representing the color of the small dot
    # small_center is a list representing the X and Y positions of the center of the small dot
    # small_radius is an int representing the radius of the small dot
    # small_velocity is a list representing the velocity in X and Y of the small dot
    # clock is the Clock object representing time
    close_selected = False
    while not close_selected:
        close_selected = handle_events()
        draw_game(window, big_color, big_center, big_radius, small_color, small_center, small_radius)
        update_game(window, big_center, big_radius, big_velocity, small_center, small_radius, small_velocity, clock)

def handle_events():
    # handle the exit game event when the player clicks [X]
    closed = False
    event_list = get_events()
    for event in event_list:
        if event.type == QUIT:
            closed = True
    return closed

def draw_game(window, big_color, big_center, big_radius,
              small_color, small_center, small_radius):
    # draw small and big dots on the screen and update the window
    #
    # window is the Window to display in
    # big_color is the string representing the color of the big dot
    # big_center is a list representing the X and Y positions of the center of the big dot
    # big_radius is an int representing the radius of the big dot
    # small_color is the string representing the color of the small dot
    # small_center is a list representing the X and Y positions of the center of the small dot
    # small_radius is an int representing the radius of the small dot
    window.clear()
    draw_dot(window, big_color, big_center, big_radius)
    draw_dot(window, small_color, small_center, small_radius)
    window.update()

def draw_dot(window, color_string, center, radius):
    # draw the dot on the screen
    #
    # window is the Window to display in
    # color_string is the string representing the color of the dot
    # center is a list representing the X and Y positions of the center of the dot
    # radius is an int representing the radius of the dot
    surface = window.get_surface()
    color = Color(color_string)
    draw_circle(surface, color, center, radius)

def update_game(window, big_center, big_radius, big_velocity, 
                small_center, small_radius, small_velocity, clock):
    # control the frame rate and update the movement of the dots
    #
    # window is the Window to display in
    # big_center is a list representing the X and Y positions of the center of the big dot
    # big_radius is an int representing the radius of the big dot
    # big_velocity is a list representing the velocity in X and Y of the big dot
    # small_center is a list representing the X and Y positions of the center of the small dot
    # small_radius is an int representing the radius of the small dot
    # small_velocity is a list representing the velocity in X and Y of the small dot
    # clock is the Clock object representing time
    frame_rate = 90
    move_dot(window, big_center, big_radius, big_velocity)
    move_dot(window, small_center, small_radius, small_velocity)
    clock.tick(frame_rate)

def move_dot(window, center, radius, velocity):
    # update the movement of the dot in each axis X and Y
    #
    # window is the Window to display in
    # center is a list representing the X and Y positions of the center of the dot
    # radius is an int representing the radius of the dot
    # velocity is a list representing the velocity in X and Y of the dot
    size = [window.get_width(), window.get_height()]
    for index in range(0, 2):
        # 0 horizontal, 1 vertical
        center[index] = center[index] + velocity[index]
        if center[index] + radius >= size[index] or center[index] - radius <= 0:
            velocity[index] = - velocity[index]

main()
