#################################################
#                                               #
#       Name: Eduardo Saul Ruiz                 #
#       Date: 12/5/2017                         #
#       Title: dac.py                           #
#       Function: Take 4 input values           #
#                 and output to 4 channels      #
#                 to form a 4-bit resistor-     #
#                 string DAC                    #
#                                               #
#################################################

################# PART A INSTRUCTIONS ######################
#  1. Your job is to complete this python code             #
#     such that it implements the same functionality       #
#     as the source code in lab 9.1.                       #
#  2. You have been provided 5 functions and a barebones   #
#     main function. 2 of the functions are incomplete -   #
#     getInput() and dacOut(). You must complete those     #
#     2 functions and the main function.                   #
#  3. In dacOut, you must develop all of the code such     #
#     that your binary-weighted DAC reads the proper       #
#     voltage. In all other functions, you will be         #
#     replacing 3 #'s (###) with a variable name.          #
#  4. In some cases, there are predetermined variable      #
#     names that you must use. In other cases, you may     #
#     choose the variable name and will likely use it      #
#     elsewhere in your code.                              #
#  5. You have been provided hints wherever you must       #
#     complete the code. Your first hint is this: complete #
#     the functions BEFORE attempting to complete the main #
#     function. Good luck!                                 #
############################################################

################# PART B INSTRUCTIONS ######################
#  1. AFTER verifying that your DAC functions properly,    #
#     output each of the sound waveforms (sinewave,        #
#     bassoon, guitar) using your dacOut() function        #
#  2. UNCOMMENT each line that has ### part b ### in it.   #
#     You will need these variables/functions for this     #
#     portion of the lab.                                  #
#  3. Use software to run each of the waveforms            #
#     individually.                                        #
#  4. Use an oscilloscope to capture ONE OF EACH waveform. #
#     You will have to use it for debugging, after all.    #
#     These captured waveforms will be submitted with your #
#     report.                                              #
############################################################


#####  Import Libraries  #####
from __future__ import print_function
import RPi.GPIO as GPIO
import time

#   Warnings Off
GPIO.setwarnings(0)

#####  Initialize GPIO   #####
#   GPIO[3,5,11,13] = input switches
#   GPIO3[8,10,16,18] = 4-bit output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

#####  Runtime Variables  #####
last = 1

#####  Function Definitions #####
def getInput(inp0, inp1, inp2, inp3):

        # HINT1: the variables on the left will be used TWICE
        # HINT2: the round(sum()) functions will be used on the function inputs
        
        inp3 = round(sum(inp3)/4.0)
        inp2 = round(sum(inp2)/4.0)
        inp1 = round(sum(inp1)/4.0)
        inp0 = round(sum(inp0)/4.0)
        dacOut = [inp3, inp2, inp1, inp0]
        return dacOut

def dacOut(inp3, inp2, inp1, inp0):
        #Implement dacOut using 4 inputs (inp3, inp2, inp1, inp0)
        if inp0:
            GPIO.output(8,1)
        elif not inp0:
            GPIO.output(8,0)
        if inp1:
            GPIO.output(10,1)
        elif not inp1:
            GPIO.output(10,0)
        if inp2:
            GPIO.output(16,1)
        elif not inp2:
            GPIO.output(16,0)
        if inp3:
            GPIO.output(18,1)
        elif not inp3:
            GPIO.output(18,0)
        
        return

def arrayToInt(my_list = [], *args):
        sum = 0
        for i in my_list:
                sum = sum + i
        return sum

def sound(period, duration, my_wave):
#        print(my_wave)
        last = 0
        for n in range(duration):
                for t in range(32):
                        
                        data = my_wave[t]
                        bin_array = int2bin(data)
                        inp3 = bin_array[3]
                        inp2 = bin_array[2]
                        inp1 = bin_array[1]
                        inp0 = bin_array[0]
                        dacOut(inp3, inp2, inp1, inp0)

#                        if last == 0:
#                               print("dacOut = [{}, {}, {}, {}]" .format(*bin_array))
#                               last == 1
                                
                        time.sleep(period)

# takes an integer value and returns the 4-bit binary representation [LSB,b1,b2,MSB]
def int2bin(val):
        return [int(x) for x in bin(val)[2:].rjust(4,'0')][::-1]
  

#################   Main   ################# 
try:
        # initialize input arrays
        my_array = [0,0,0,0]   #HINT: this array will be used multiple times in your code
        inp0 = [0,0,0,0]
        inp1 = [0,0,0,0]
        inp2 = [0,0,0,0]
        inp3 = [0,0,0,0]
        sinewave = [8,9,11,12,13,14,14,15,15,15,14,14,13,12,11,9,8,7,5,4,3,2,2,1,1,1,2,2,3,4,5,7]
        bassoon = [8,8,8,8,7,7,9,15,10,1,1,4,8,11,10,6,3,2,6,10,8,5,5,5,6,7,7,9,8,8,8,7]
        guitar = [5,5,4,1,1,3,8,11,11,9,4,2,5,11,15,13,9,7,5,5,6,8,8,7,4,3,3,3,3,4,5,5]
	period_midA = 1/(440*32)
	period_midC = 1/(261*32)
	period_hiA = 1/(1661*32)
	period_hiC = 1/(1046*32)

        while True:

                    #### Part A Implementation ####
		
                # Store input values into input arrays
                inp0 = inp0[1:] + [GPIO.input(7)]
                inp1 = inp1[1:] + [GPIO.input(15)]
                inp2 = inp2[1:] + [GPIO.input(11)]
                inp3 = inp3[1:] + [GPIO.input(13)]

                # Store values to ###
                # HINT: this is the same array you declared in initialization
                my_array = getInput(inp0, inp1, inp2, inp3)

                # Determine decimal value of input
                # HINT: this is the same array you declared in initialization
                inp = arrayToInt(my_array)
                dacOut(my_array[0], my_array[1], my_array[2], my_array[3])
        
                # If new value, print input
                # HINT: this is the same array you declared in initialization
                if last != inp:
                        print("Your input = [{}, {}, {}, {}]" .format(*my_array))
                        last = inp
                
                time.sleep(.05)

									#### Part B Implementation ####
                #
				# You will need to comment out much of the code used in part A.                                                                      
                # Here you will make calls to sound(). Here is an example:
                # sound(freq_midA, 1000, sinewave) will output a sinewave at the frequency
				# of middle A 1000 times in a row. You may call sound multiple times 
				# in succession to capture multiple waves in a row. Good luck!
                #
		sound(period_hiA, 1000, guitar)
		sound(period_midA, 1000, sinewave)
		sound(period_midC, 1000, bassoon)
# ^C exit 
except KeyboardInterrupt:
        print("\n")
        print("Exiting program!")

#error exit
except e:
        print("Oops! You have another exception.\n", e)
        
        
#finally
finally:
        GPIO.cleanup()
