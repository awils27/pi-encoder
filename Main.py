from threading import Thread
import Button
import Encoder

Button_GPIO = 16
EncoderA = 20
EncoderB = 21
PulsesPerRev = 400

def button_pressed_callback(channel):
    print (Encoder.counter)
    Encoder.counter = 0
    print("Lens Value Reset")



ThreadButtonSetup = Thread(target = Button.SetupButton, args = (Button_GPIO, button_pressed_callback))

ThreadButtonSetup.start()
ThreadButtonSetup.join()


Encoder.SetupEncoders(EncoderA, EncoderB)

Encoder.ReadEncoderValues(EncoderA, EncoderB)
