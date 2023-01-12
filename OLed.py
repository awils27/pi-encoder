from luma.core.interface.serial import gpio_cs_spi
from luma.core.render import canvas
from luma.oled.device import sh1106
from luma.core import cmdline

# rev.1 users set port=0
# substitute spi(device=0, port=0) below if using that interface
# substitute bitbang_6800(RS=7, E=8, PINS=[25,24,23,27]) below if using that interface
serial = gpio_cs_spi(device=0, port=0, gpio_CS=5, gpio_DC=6, gpio_RS=4)

# substitute ssd1331(...) or sh1106(...) below if using that device
device = sh1106(serial)

with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((30, 40), "Hello World", fill="white")
