#    Title: led_on.py
#    Function: turn a single LED on via GPIo
#

# # #  Import Libraries  # # #
import RPi.GPIO as GPIO
import time

# # #  GPIO Initialization  # # #
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)	 # Use channel 7 to output to LED

# # #  Activate Channel 7 # # #

while 1:
	# You must complete this line of code by inputting the channel and boolean value
	GPIO.output(7,1)
	
# # #  Cleanup Program  # # #
GPIO.cleanup()

