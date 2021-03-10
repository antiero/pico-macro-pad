class AbstractConfiguration:
	# The name will be visible in the console
	def getName():
		return ""

	def appName():
		return ""

	def shouldLaunch():
		return False

	# The color will colorize the button of the configuration and it's macros
	def getColor():
		return (0, 0, 0)
	# Return an array of maximum 15 macros
	def getMacros():
		return []
	# Needed to do nothing when is selected a not-configured button
	def nothing():
		pass

class AbstractMacro:
	# The name will be visible in the console
	def getMacroName():
		return ""
	# Here you will implement the actions of your macro
	def getMacro():
		pass
	# The color will colorize the button of the configuration and it's macros
	def getColor():
		return (255, 255, 255)		