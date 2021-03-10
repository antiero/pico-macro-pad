import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

def SpotlightLauncher(appName):
	print("Attempting Spotlight Launch of App: %s" % appName)
	keyboard.send(Keycode.COMMAND, Keycode.SPACE)
	layout.write(appName)
	keyboard.send(Keycode.RETURN)