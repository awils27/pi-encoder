import Encoder
from FreeD import FreeD, FreeDWrapper
import socket
from time import sleep
from threading import Thread



class SendData(Thread):

    def SendFreeDData(IP, Port):
        struct = FreeDWrapper(0,0,0,0,0,0,0,0)
        bits: 'bytes' = struct.createFreeD().encode()
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        while True:

            struct.focus = Encoder.counter
            bits = struct.createFreeD().encode()


            sock.sendto(bits, (IP, Port))

            sleep(1/60)