import usb_hid
import time
import random

from abstract_classes import AbstractConfiguration, AbstractMacro
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)



## CONFIGURATIONS ##


class Terminal(AbstractConfiguration):
	def getName():
		return 'Terminal'
	def getColor():
		return (0, 255, 0)

	def appName():
		return 'Terminal.app'

	def shouldLaunch():
		return True

	def getMacros():
		return [
			Ls, 
			Pwd,
			Home,
		]

class Logic(AbstractConfiguration):
	def getName():
		return 'Logic'
	def getColor():
		return (114, 75, 171)
	def appName():
		return 'Logic Pro.app'
	def shouldLaunch():
		return True		
	def getMacros():
		return [
			SelectForward,
			CreateMarker
		]

class GoogleMeet(AbstractConfiguration):
	def getName():
		return 'Google Meet'
	def getColor():
		return (255, 128, 0)
	def getMacros():
		return [
			ToggleMicrophone, 
			ToggleWebcam
		]

class Git(AbstractConfiguration):
	def getName():
		return 'GIT'
	def getColor():
		return (247, 78, 39)
	def getMacros():
		return [
			MergeDevelop,
			MergeMaster,
			GitPush
		]

## COMMANDS ##	

# Logic Pro
class SelectForward(AbstractMacro):
	def getMacroName():
		return 'Select Forward'
	def getMacro():
		keyboard.send(Keycode.SHIFT, Keycode.F)

class CreateMarker(AbstractMacro):
	def getMacroName():
		return 'Create Marker'
	def getMacro():
		keyboard.send(Keycode.OPTION, Keycode.QUOTE)		

class OneWeekEsteem(AbstractMacro):
	def getMacroName():
		return '< 1 week'
	def getMacro():
		layout.write(str(random.randint(1, 5)))
		keyboard.send(Keycode.ENTER)

class Ls(AbstractMacro):
	def getMacroName():
		return 'ls -al'
	def getMacro():
		layout.write("ls ")
		keyboard.send(Keycode.KEYPAD_MINUS)
		layout.write("al")
		keyboard.send(Keycode.ENTER)

class Pwd(AbstractMacro):
	def getMacroName():
		return 'pwd'
	def getMacro():
		layout.write("pwd")
		keyboard.send(Keycode.ENTER)

class Home(AbstractMacro):
	def getMacroName():
		return 'Home'
	def getMacro():
		layout.write("cd ")
		keyboard.send(Keycode.ENTER)

# Google Meet
class ToggleMicrophone(AbstractMacro):
	def getMacroName():
		return 'Toggle Microphone'
	def getMacro():
		keyboard.send(Keycode.COMMAND, Keycode.D)

class ToggleWebcam(AbstractMacro):
	def getMacroName():
		return 'Toggle Webcam'
	def getMacro():
		keyboard.send(Keycode.COMMAND, Keycode.E)

# Git
class MergeDevelop(AbstractMacro):
	def getMacroName():
		return "Merge develop into master"
	def getMacro():
		layout.write("git checkout master")
		keyboard.send(Keycode.ENTER)
		time.sleep(0.5)
		layout.write("git merge develop")
		keyboard.send(Keycode.ENTER)

class MergeMaster(AbstractMacro):
	def getMacroName():
		return "Merge master into develop"
	def getMacro():
		layout.write("git checkout develop")
		keyboard.send(Keycode.ENTER)
		time.sleep(0.5)
		layout.write("git merge master")
		keyboard.send(Keycode.ENTER)

class GitPush(AbstractMacro):
	def getMacroName():
		return "Push"
	def getMacro():
		layout.write("git push")
		keyboard.send(Keycode.ENTER)
		

# Map your configurations inside this array
#configurations_map = [Terminal, GoogleMeet, Obsidian, RandomEstimation, PhpStorm, Git, Logic ]	
configurations_map = [Terminal, Logic ]	
