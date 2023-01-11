from threading import Thread
from FreeD import FreeD, FreeDWrapper
import socket
import Button
import Encoder

Button_GPIO = 16
EncoderA = 20
EncoderB = 21

UDP_IP = "127.0.0.1"
UDP_PORT = 40000


struct = FreeDWrapper(0,0,0,0,0,0,0,0)
bits: 'bytes' = struct.createFreeD().encode()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

unit = 1000


sock.sendto(bits, (UDP_IP, UDP_PORT))



def button_pressed_callback(channel):
    Encoder.counter = 0
    print("Lens Value Reset")




Encoder.SetupEncoders(EncoderA, EncoderB)
T1Encoders = Thread(target = Encoder.EncoderThread.ReadEncoderValues, args = (EncoderA, EncoderB))
T1Encoders.start()


Button.SetupButton(Button_GPIO, button_pressed_callback)
