from RPi import GPIO
from time import sleep
import signal
import sys


def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)



def SetupButton(BUTTON_PIN, Callback):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, 
            callback=Callback, bouncetime=100)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
    
    return