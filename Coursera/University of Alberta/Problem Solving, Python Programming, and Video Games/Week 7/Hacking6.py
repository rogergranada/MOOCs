# Code for Hacking6.py

# Hacking Version 6
# This is a window-based password guessing game that displays a
# list of potential computer passwords. The player is allowed
# 4 attempts to guess the password. The game indicates that the
# player achieved success or failure to guess the password.
# It uses functions to remove duplicates of code.

from uagame import Window
from time import sleep

def main():
    location = [0, 0]
    attempts_left = 4
    password = 'HUNTING'
    window = create_window()
    display_header(window, location, attempts_left)
    display_password_list(window, location)
    guess = get_guesses(window, password, location, attempts_left)
    end_game(window, guess, password)


def create_window():
    # create window with aspect ration of 6:5, black screen 
    # and green letters, and small font-size
    window = Window('Hacking', 600, 500)
    window.set_font_name('couriernew')
    window.set_font_size(18)
    window.set_font_color('green')
    window.set_bg_color('black')
    return window


def display_header(window, location, attempts):
    # display header of the window
    # - window is the new Window to display in
    # - location is a tuple containing the int x and int y coords of where 
    #   the string should be displayed and it should be updated to one "line" 
    #   below the top left corner of the displayed string
    # - attempts is the number of tries the user can enter
    header_lines = ['DEBUG MODE', str(attempts)+' ATTEMPT(S) LEFT', '']
    for header_line in header_lines:
        display_line(window, header_line, location)


def display_password_list(window, location):
    # display password list
    # - window is the new Window to display in
    # - location is a tuple containing the int x and int y coords of where 
    #   the string should be displayed and it should be updated to one "line" 
    #   below the top left corner of the displayed string
    password_list = ['PROVIDE', 'SETTING', 'CANTINA', 'CUTTING', 
                     'HUNTERS', 'SURVIVE', 'HEARING', 'HUNTING', 
                     'REALIZE', 'NOTHING', 'OVERLAP', 'FINDING', 'PUTTING', '']
    for password in password_list:
        # diplay password line
        display_line(window, password, location)


def get_guesses(window, password, location, attempts_left):
    # get guesses from the user
    # - window is the new Window to display in
    # - password is a string with the correct password
    # - location is a tuple containing the int x and int y coords of where 
    #   the string should be displayed and it should be updated to one "line" 
    #   below the top left corner of the displayed string
    # - attempts_left represents the number of attempts the user has
    string_height = window.get_font_height()
    guess = prompt_user(window, 'ENTER PASSWORD >', location)
    attempts_left = attempts_left - 1

    while guess != password and attempts_left > 0:
        # display attempts left
        window.draw_string(str(attempts_left), 0, string_height)
        # check warning
        check_warning(window, attempts_left)
        # get guess
        guess = prompt_user(window, 'ENTER PASSWORD >', location)
        attempts_left = attempts_left - 1
    return guess


def end_game(window, guess, password):
    # generate the messages for the end of the game according to the
    # guess and correct password
    # - window is the new Window to display in
    # - guess is a string content the guess of the user
    # - password is a string with the correct password
    # clear window
    window.clear()
    # create outcome
    if guess == password:
        # create success
        outcome = [guess, '', 'EXITING DEBUG MODE', '', 'LOGIN SUCCESSFUL - WELCOME BACK', '']
        prompt = 'PRESS ENTER TO CONTINUE'
    else:
        # create failure
        outcome = [guess, '', 'LOGIN FAILURE - TERMINAL LOCKED', '', 'PLEASE CONTACT AN ADMINISTRATOR', '']
        prompt = 'PRESS ENTER TO EXIT'
    line_y = display_outcome(window, outcome)
    x_space = window.get_width() - window.get_string_width(prompt)
    line_x = x_space // 2
    prompt_user(window, prompt, [line_x, line_y])

    # close window
    window.close()


def display_line(window, string, location):
    # Display a string in the window in the window and update the location
    # - window is the new Window to display in
    # - string is the srt to display in
    # - location is a tuple containing the int x and int y coords of where 
    # the string should be displayed and it should be updated to one "line" 
    # below the top left corner of the displayed string
    pause_time = 0.3
    string_height = window.get_font_height()
    window.draw_string(string, location[0], location[1])
    window.update()
    sleep(pause_time)
    location[1] = location[1] + string_height

       
def prompt_user(window, prompt, location):
    # prompt the user for the guess or end of the game
    # - window is the new Window to display in
    # - prompt is the string to display information
    # - location is a tuple containing the int x and int y coords of where 
    # the string should be displayed and it should be updated to one "line" 
    # below the top left corner of the displayed string
    answer = window.input_string(prompt, location[0], location[1])
    string_height = window.get_font_height()
    location[1] = location[1] + string_height
    return answer


def check_warning(window, attempts_left):
    # check warning to display lockout
    # - window is the new Window to display in
    # - attempts_left represents the number of attempts the user has
    string_height = window.get_font_height()
    if attempts_left == 1:
        # display warning
        warning = '*** LOCKOUT WARNING ***'
        x_space = window.get_width() - window.get_string_width(warning)
        y_space = window.get_height() - string_height
        window.draw_string(warning, x_space, y_space)


def display_outcome(window, outcome):
    # display success or failure outcome
    # - window is the new Window to display in
    # - outcome is a list containing strings for success or failure
    string_height = window.get_font_height()
    outcome_height = 7 * string_height
    y_space = window.get_height() - outcome_height
    line_y = y_space // 2

    for line in outcome:
        # display outcome
        x_space = window.get_width() - window.get_string_width(line)
        line_x = x_space // 2
        display_line(window, line, [line_x, line_y])
        line_y = line_y + string_height
    return line_y

main()
