from threading import Thread
import Button
import Encoder
import DataSending
import atexit
import Oled
from RPi import GPIO


Button_GPIO = 16
EncoderA = 21
EncoderB = 20
UDP_IP = "192.168.1.68"
UDP_PORT = 4000
Display = "sh1106"
Interface = "gpio_cs_spi"
DC_Pin = "24"
CS_Pin = "8"
RST_Pin = "25"
ScreenRot = "2"
Encoder_Frq = 60



def ExitHandler():
    GPIO.cleanup()

def button_pressed_callback(channel):
    Encoder.counter = 0
    print("Lens Value Reset")


atexit.register(ExitHandler)

Encoder.SetupEncoders(EncoderA, EncoderB)

Display = Oled.IntialiseDisplay(Display, Interface, DC_Pin, CS_Pin, RST_Pin, ScreenRot)



T1Encoders = Thread(target = Encoder.EncoderThread.ReadEncoderValues, args = (EncoderA, EncoderB))

T2Data = Thread(target = DataSending.SendData.SendFreeDData, args = (UDP_IP, UDP_PORT))

T3Screen = Thread(target = Oled.OLEDScreen.StartOLEDDisplay, args = (UDP_IP, UDP_PORT, Encoder_Frq, Display))

T1Encoders.start()
T2Data.start()

Button.SetupButton(Button_GPIO, button_pressed_callback)


