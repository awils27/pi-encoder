#!/usr/bin/env python3          
                                
import signal                   
import sys
import RPi.GPIO as GPIO

ENCODER_A = 7
ENCODER_B = 8

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def button_callback(channel):
    if not GPIO.input(ENCODER_A):
        print("Button pressed!")
    else:
        print("Button released!")

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ENCODER_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    GPIO.add_event_detect(ENCODER_A, GPIO.BOTH, 
            callback=button_callback, bouncetime=50)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()