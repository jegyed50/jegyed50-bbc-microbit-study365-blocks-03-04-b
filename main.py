def on_button_pressed_a():
    basic.show_string("w")
    basic.pause(2500)
    basic.show_string("R")
    basic.pause(500)
    basic.show_string("w")
    basic.pause(2500)
    basic.show_string("R")
    basic.pause(500)
    basic.show_string("w")
    basic.pause(2500)
    basic.show_string("w")
    basic.show_string("R")
    basic.pause(1500)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

# https://github.com/jegyed50/jegyed50-bbc-microbit-study365-blocks-03-04-a
# JEGYED50-BBC-MICROBIT-STUDY365-BLOCKS-03-04-B
# POMODORO TIMER
# Betűk W25R5W25R5W25R5W25R15 25p=2500ms, 5p =500ms, 15p=1500ms

def on_forever():
    pass
basic.forever(on_forever)
