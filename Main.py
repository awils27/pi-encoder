from threading import Thread
import Button
import Encoder
import DataSending

Button_GPIO = 16
EncoderA = 20
EncoderB = 21
UDP_IP = "192.168.1.68"
UDP_PORT = 4000





def button_pressed_callback(channel):
    Encoder.counter = 0
    print("Lens Value Reset")




Encoder.SetupEncoders(EncoderA, EncoderB)
T1Encoders = Thread(target = Encoder.EncoderThread.ReadEncoderValues, args = (EncoderA, EncoderB))

T2Data = Thread(target = DataSending.SendData.SendFreeDData, args = (UDP_IP, UDP_PORT))


T1Encoders.start()
T2Data.start()

Button.SetupButton(Button_GPIO, button_pressed_callback)
