#################################################
#					   	#
#	Name: Eduardo Saul Ruiz		   	#
#	Date: 11/02/2017		   	#
#	Title: two_to_four_decoder.py	   	#
#	Function: Take two inputs and output 	#
#		  to four LEDs as a decoder  	#
#					   	#	
#################################################

#####  Import Libraries  #####
import RPi.GPIO as GPIO
import time

#   Warnings Off
GPIO.setwarnings(0)

#####  Initialize GPIO   #####
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

#####  Runtime Variables  #####
last = 1	      #Chill out w/the rick and morty broh
dec_out0 = [0,0,0,1]
dec_out1 = [0,0,1,0]
dec_out2 = [0,1,0,0]
dec_out3 = [1,0,0,0]
my_array = dec_out0

#####   Main function   #####
#
# Implement your decoder in SW here:
#
try:
	while True:
                if not GPIO.input(3) and not GPIO.input(5):
                        GPIO.output(7,0)
                        GPIO.output(11,0)
                        GPIO.output(13,0)
                        GPIO.output(15,1)

                        my_array = dec_out0
                        time.sleep(.2)       #debounce time
                        if last != 0:
                                print "Decoder output: [{}, {}, {}, {}]" .format(*my_array)
                                last = 0
		elif not GPIO.input(3) and GPIO.input(5):
                        GPIO.output(7,0)
                        GPIO.output(11,0)
                        GPIO.output(13,1)
                        GPIO.output(15,0)

                        my_array = dec_out1
                        time.sleep(.2)       #debounce time
                        if last != 1:
				print "Decoder output: [{}, {}, {}, {}]" .format(*my_array)
                                last = 1
                elif GPIO.input(3) and not GPIO.input(5):
                        GPIO.output(7,0)
                        GPIO.output(11,1)
                        GPIO.output(13,0)
                        GPIO.output(15,0)

                        my_array = dec_out2
                        time.sleep(.2)       #debounce time
                        if last != 2:
                                print "Decoder output: [{}, {}, {}, {}]" .format(*my_array)
                                last = 2
		elif GPIO.input(3) and GPIO.input(5):
                        GPIO.output(7,1)
                        GPIO.output(11,0)
                        GPIO.output(13,0)
                        GPIO.output(15,0)

                        my_array = dec_out3
                        time.sleep(.2)       #debounce time
                        if last != 3:
                                print "Decoder output: [{}, {}, {}, {}]" .format(*my_array)
                                last = 3
                else:
                        print "You made it to else statement. Oops!\n"

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

