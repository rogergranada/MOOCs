# Code for Hacking4.py

# Hacking Version 4
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
header = ['DEBUG MODE', '1 ATTEMPT(S) LEFT', '']

for header_line in header:
    window.draw_string(header_line, 0, line_y)
    window.update()
    sleep(0.3)
    line_y = line_y + string_height

# display password list
password_list = ['PROVIDE', 'SETTING', 'CANTINA', 'CUTTING', 'HUNTERS', 'SURVIVE', 'HEARING', 'HUNTING', 'REALIZE', 'NOTHING', 'OVERLAP', 'FINDING', 'PUTTING', '']

for password in password_list:
    # diplay password line
    window.draw_string(password, 0, line_y)
    window.update()
    sleep(0.3)
    line_y = line_y + string_height

# prompt for guess
guess = window.input_string('ENTER PASSWORD >', 0, line_y)

# end game

# clear window
window.clear()

# create outcome
#   check guess equals password
if guess == 'HUNTING':
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

for outcome_line in outcome_list:
    # display outcome
    x_space = window.get_width() - window.get_string_width(outcome_line)
    line_x = x_space // 2
    window.draw_string(outcome_line, line_x, line_y)
    window.update()
    sleep(0.3)
    line_y = line_y + string_height

x_space = window.get_width() - window.get_string_width(outcome_line4)
line_x = x_space // 2
window.input_string(outcome_line4, line_x, line_y)

# close window
window.close()
