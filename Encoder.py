from RPi import GPIO
from time import sleep
import signal
import sys
from threading import Thread


counter = 0

def SetupEncoders(EncoderA, EncoderB):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(EncoderA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(EncoderB, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    print ("Encoders ready.")

    return

class EncoderThread(Thread):
    def ReadEncoderValues(EncoderA, EncoderB):
        print ("Reading Encoder")
        LastState = GPIO.input(EncoderA)
        global counter
        while True:
            AState = GPIO.input(EncoderA)
            BState = GPIO.input(EncoderB)

            if AState != LastState:
                if BState !=AState:
                    counter += 1

                else:
                    counter -= 1

            LastState = AState
