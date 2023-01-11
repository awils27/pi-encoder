from threading import Thread
import Button
import Encoder

Button_GPIO = 16
EncoderA = 20
EncoderB = 21
PulsesPerRev = 400

def button_pressed_callback(channel):
    Encoder.counter = 0
    print("Lens Value Reset")




Encoder.SetupEncoders(EncoderA, EncoderB)

ThreadEncoders = Thread(target = Encoder.ReadEncoderValues, args = (EncoderA, EncoderB))

ThreadEncoders.start()
ThreadEncoders.join()

Button.SetupButton(Button_GPIO, button_pressed_callback)
