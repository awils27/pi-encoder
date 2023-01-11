from RPi import GPIO
from time import sleep
import signal
import sys


counter = 0

def SetupEncoders(EncoderA, EncoderB):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(EncoderA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(EncoderB, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def ReadEncoderVlaues(EncoderA, EncoderB):
    LastState = GPIO.input(EncoderA)
    global counter
    try:
        while True:
            AState = GPIO.input(EncoderA)
            BState = GPIO.input(EncoderB)

            if AState != LastState:
                if BState !=AState:
                    counter += 1

                else:
                    counter -= 1

                print ((360/400)*counter)

            LastState = AState
            sleep(0.001)

    finally:
        GPIO.cleanup()
