from RPi import GPIO
from time import sleep
import signal
import sys




def SetupEncoders(EncoderA, EncoderB):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(EncoderA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(EncoderB, GPIO.IN, pull_up_down=GPIO.PUD_UP)

counter = 0
LastState = GPIO.input(EncoderA)

try:
    while True:
        AState = GPIO.input(EncoderA)
        BState = GPIO.input(EncoderB)

        if AState != LastState:
            if BState !=AState:
                counter += 1

            else:
                counter -= 1

            degrees = (360/PulsesPerRev)*counter

            print (str(degrees) + " degrees")

        LastState = AState
        sleep(0.001)

finally:
    GPIO.cleanup()
