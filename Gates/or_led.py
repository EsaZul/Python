#################################################
#					   	#
#	Name: Eduardo Saul Ruiz		   	#
#	Date: 10/27/2017		   	#
#	Title: or_led.py		   	#
#	Function: Implement an OR gate in 	#
#		  HW and SW to switch LED  	#
#					   	#
#################################################

#####  Import Libraries  #####
import RPi.GPIO as GPIO
import time

#   Warnings Off
GPIO.setwarnings(0)

#####  Initialize GPIO   #####
#   GPIO5 = output to LED
#   GPIO3 = input from switch
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(7, GPIO.OUT) 

#####  Runtime Variables  #####
printed = 0	      #Chill out w/the rick and morty broh


#####   Main function   #####
#
# Implement your logic function in SW here:
#
try:
	while True:
		if not  GPIO.input(3) or not GPIO.input(5):
			GPIO.output(7,1)

			if not printed: #don't touch these lines
				print "Look Morty! We turned the light on with science!"
			printed = 1
		else:
			GPIO.output(7,0) #turn LED off
			printed = 0

# ^C exit 
except KeyboardInterrupt:
	print "\n"
	print "Exiting program!"
	#clean up program
	GPIO.cleanup()

#error exit
except:
	print "Oops! You have another error/exception."
	GPIO.cleanup()

#all else
finally:
	GPIO.cleanup()


