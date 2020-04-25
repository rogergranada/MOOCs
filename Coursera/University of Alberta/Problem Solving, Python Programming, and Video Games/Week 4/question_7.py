from uagame import Window
from time import sleep

# create window
window = Window('hello', 300, 200)
string_height = window.get_font_height()

# prompt user
input_string = window.input_string('Enter string >', 0, 0)

# set text in the right corner
x_space = window.get_width() - window.get_string_width(input_string)
y_space = window.get_height() - window.get_font_height()

# draw text
window.draw_string(input_string, x_space, y_space)
window.update()
sleep(2.0)

# close window
window.close()
