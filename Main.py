from threading import Thread
import Button
import Encoder

Button_GPIO = 16
EncoderA = 21
EncoderB = 20

def button_pressed_callback(channel):
    Encoder.counter = 0
    print("Lens Value Reset")




Encoder.SetupEncoders(EncoderA, EncoderB)
T1Encoders = Thread(target = Encoder.EncoderThread.ReadEncoderValues, args = (EncoderA, EncoderB))
T1Encoders.start()


Button.SetupButton(Button_GPIO, button_pressed_callback)
