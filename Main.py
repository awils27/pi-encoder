import Button
#import Encoder

Button_GPIO = 16
EncoderA = 20
EncoderB = 21
PulsesPerRev = 400

def button_pressed_callback(channel):
    print("Button pressed!")

Button.SetupButton(Button_GPIO, button_pressed_callback)
#Encoder.SetupEncoders(EncoderA, EncoderB)