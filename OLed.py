import time
from OledSetup import get_device
from luma.core.render import canvas
import Encoder
from threading import Thread

#['--display', 'sh1106', '--interface', 'gpio_cs_spi', '--gpio-data-command', '24', '--gpio-chip-select', '8', '--gpio-reset', '25', '--rotate', '2']

def IntialiseDisplay(display, interface, DC, CS, RST, Rot):


    arguments = ['--display', display, '--interface', interface, '--gpio-data-command', DC, '--gpio-chip-select', CS, '--gpio-reset', RST, '--rotate', Rot]
    device = get_device(arguments)

    print("Starting Display")

    return device


class OLEDScreen(Thread):
    def StartOLEDDisplay(IpAddr, Port, Freq, device):
        while True:
            for x in range(40):
                if x < 20:
                    text = IpAddr + ":" + str(Port)
                else:
                    text = str(Freq) + "hz Genlock"

                with canvas(device) as draw:
                    draw.text((5, 2), "Lens Encoder V15.04", fill="white")
                    draw.text((5, 15), "Zoom  " + str(abs(Encoder.counter)), fill="white")
                    draw.text((5, 30), "Focus  1000", fill="white")
                    draw.text((5, 45), text, fill="white")
                    time.sleep(0.1)