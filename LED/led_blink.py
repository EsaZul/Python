#    Title: led_on.py
#    Function: turn a single LED on via GPIo
#

# # #  Import Libraries  # # #
import RPi.GPIO as GPIO
import time

# # #  GPIO Initialization  # # #
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)	 # Use channel 7 to output to LED

# # #  Flash LED at 1 Hz # # #

for i in range(50):
	#You must complete this for loop by inputting the channel and boolean values where needed
	GPIO.output(7, 1,)
	time.sleep(.5)
	GPIO.output(7, 0,)
	time.sleep(.5)

# # # Cleanup Program # # #
GPIO.cleanup()
