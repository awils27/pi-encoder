import time
from OledSetup import get_device
from luma.core.render import canvas


arguments = ['--display', 'sh1106', '--interface', 'gpio_cs_spi', '--gpio-data-command', '24', '--gpio-chip-select', '8', '--gpio-reset', '25', '--rotate', '2']

device = get_device(arguments)

print("Testing screen updates...")
while True:
    with canvas(device) as draw:
        draw.text((3, 2), "Lens Encoder   V15.04", fill="white")
        draw.text((3, 10), "Lens Encoder   V15.04", fill="white")
        draw.text((3, 20), "Lens Encoder   V15.04", fill="white")
        draw.text((3, 30), "Lens Encoder   V15.04", fill="white")
        time.sleep(0.1)