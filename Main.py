import Button
import Encoder

Button_GPIO = 16
EncoderA = 20
EncoderB = 21
PulsesPerRev = 400



Button.SetupButton(Button_GPIO)
Encoder.SetupEncoders(EncoderA, EncoderB)