# this code is a hunk of crap but should be ok for testing if the thing works lol
# circuitpython required!

import board
import busio
import time
from adafruit_matrixkeypad import Matrix_Keypad
import digitalio
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image, ImageDraw, ImageFont

# super awesome display setup
i2c = busio.I2C(board.GP18, board.GP19)  # SDA, SCL
WIDTH = 128
HEIGHT = 64
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# clear display
oled.fill(0)
oled.show()

image = Image.new("1", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

uart = busio.UART(board.GP17, board.GP16, baudrate=31250)

def midi_note_on(note, velocity=127, channel=1):
    uart.write(bytes([0x90 | channel, note, velocity]))

def midi_note_off(note, velocity=0, channel=1):
    uart.write(bytes([0x80 | channel, note, velocity]))

rows = [board.GP0, board.GP1]
cols = [board.GP2, board.GP3, board.GP4, board.GP5,
        board.GP6, board.GP7, board.GP8, board.GP9]

keypad = Matrix_Keypad(rows, cols)

notes = [
    60, 61, 62, 63, 64, 65, 66, 67,  # row 0
    68, 69, 70, 71, 72, 73, 74, 75   # row 1
]

key_states = [False] * 16

def update_display(key_idx=None):
    draw.rectangle((0, 0, WIDTH, HEIGHT), outline=0, fill=0)  # clear screen
    if key_idx is not None:
        draw.text((0, 0), f"key: {key_idx}", font=font, fill=255)
        draw.text((0, 16), f"note: {notes[key_idx]}", font=font, fill=255)
    else:
        draw.text((0, 0), "no key pressed", font=font, fill=255)
    oled.image(image)
    oled.show()

while True:
    keys = keypad.pressed_keys  # list of (row, col) tuples
    any_key_pressed = False

    for r in range(len(rows)):
        for c in range(len(cols)):
            key_idx = r * len(cols) + c
            pressed = (r, c) in keys
            if pressed and not key_states[key_idx]:
                midi_note_on(notes[key_idx])
                key_states[key_idx] = True
                update_display(key_idx)
                any_key_pressed = True
            elif not pressed and key_states[key_idx]:
                midi_note_off(notes[key_idx])
                key_states[key_idx] = False

    if not any_key_pressed:
        update_display(None)

    time.sleep(0.01)  # small debounce
