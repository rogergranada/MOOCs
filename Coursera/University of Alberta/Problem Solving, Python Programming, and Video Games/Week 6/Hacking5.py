# Code for Hacking5.py

# Hacking Version 5
# This is a window-based password guessing game that displays a
# list of potential computer passwords. The player is allowed
# 1 attempt to guess the password. The game indicates that the
# player achieved success or failure to guess the password.
# It uses a for loop to iterate on passwords

from uagame import Window
from time import sleep

# create window
window = Window('Hacking', 600, 500)
window.set_font_name('couriernew')
window.set_font_size(18)
window.set_font_color('green')
window.set_bg_color('black')

# display header
line_y = 0
string_height = window.get_font_height()
attempts_left = 4
header_lines = ['DEBUG MODE', str(attempts_left)+' ATTEMPT(S) LEFT', '']

for header in header_lines:
    window.draw_string(header, 0, line_y)
    window.update()
    sleep(0.3)
    line_y = line_y + string_height

# display password list
password_list = ['PROVIDE', 'SETTING', 'CANTINA', 'CUTTING', 
                 'HUNTERS', 'SURVIVE', 'HEARING', 'HUNTING', 
                 'REALIZE', 'NOTHING', 'OVERLAP', 'FINDING', 'PUTTING', '']

for password in password_list:
    # diplay password line
    window.draw_string(password, 0, line_y)
    window.update()
    sleep(0.3)
    line_y = line_y + string_height

guess = window.input_string('ENTER PASSWORD >', 0, line_y)
line_y = line_y + string_height
attempts_left = attempts_left - 1

while guess != password_list[7] and attempts_left > 0:
    # display attempts left
    window.draw_string(str(attempts_left), 0, string_height)

    # check warning
    if attempts_left == 1:
        # display warning
        warning = '*** LOCKOUT WARNING ***'
        x_space = window.get_width() - window.get_string_width(warning)
        y_space = window.get_height() - string_height
        window.draw_string(warning, x_space, y_space)

    # get guess
    guess = window.input_string('ENTER PASSWORD >', 0, line_y)
    line_y = line_y + string_height
    attempts_left = attempts_left - 1

# end game

# clear window
window.clear()

# create outcome
#   check guess equals password
if guess == password_list[7]:
    # create success
    outcome_line2 = 'EXITING DEBUG MODE'
    outcome_line3 = 'LOGIN SUCCESSFUL - WELCOME BACK'
    outcome_line4 = 'PRESS ENTER TO CONTINUE'
else:
    # create failure
    outcome_line2 = 'LOGIN FAILURE - TERMINAL LOCKED'
    outcome_line3 = 'PLEASE CONTACT AN ADMINISTRATOR'
    outcome_line4 = 'PRESS ENTER TO EXIT'


# display outcome
# compute initial y coordinate
outcome_height = 7 * string_height
y_space = window.get_height() - outcome_height
line_y = y_space // 2

outcome_list = [guess, '', outcome_line2, '', outcome_line3, '']

for outcome in outcome_list:
    # display outcome
    x_space = window.get_width() - window.get_string_width(outcome)
    line_x = x_space // 2
    window.draw_string(outcome, line_x, line_y)
    window.update()
    sleep(0.3)
    line_y = line_y + string_height

x_space = window.get_width() - window.get_string_width(outcome_line4)
line_x = x_space // 2
window.input_string(outcome_line4, line_x, line_y)

# close window
window.close()
