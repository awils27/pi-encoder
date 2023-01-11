import Encoder
from FreeD import FreeD, FreeDWrapper
import socket
from time import sleep
from threading import Thread

UDP_IP = "192.168.1.68"
UDP_PORT = 4000

class SendData(Thread):
    
    def SendFreeDData():
        while True:

            struct = FreeDWrapper(0,0,0,0,0,0,0,0)
            bits: 'bytes' = struct.createFreeD().encode()
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            struct.focus = Encoder.counter
            bits = struct.createFreeD().encode()


            sock.sendto(bits, (UDP_IP, UDP_PORT))

            sleep(1/60)