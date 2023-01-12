import time
from OledSetup import get_device
from luma.core.render import canvas
import Encoder
import Main

arguments = ['--display', 'sh1106', '--interface', 'gpio_cs_spi', '--gpio-data-command', '24', '--gpio-chip-select', '8', '--gpio-reset', '25', '--rotate', '2']

device = get_device(arguments)

print("Testing screen updates...")
while True:
    for x in range(40):
        if x < 20:
            text = Main.UDP_IP + ":" + str(Main.UDP_PORT)
        else:
            text = "60hz Genlock"

        with canvas(device) as draw:
            draw.text((5, 2), "Lens Encoder V15.04", fill="white")
            draw.text((5, 15), "Zoom  " + str(abs(Encoder.counter)), fill="white")
            draw.text((5, 30), "Focus  1000", fill="white")
            draw.text((5, 45), text, fill="white")
            time.sleep(0.1)