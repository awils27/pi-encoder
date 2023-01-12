from luma.core.interface.serial import gpio_cs_spi
from luma.core.render import canvas
from luma.oled.device import sh1106


import sys
import logging

from luma.core import cmdline, error


def get_device(actual_args=None):
    """
    Create device from command-line arguments and return it.
    """
    if actual_args is None:
        actual_args = sys.argv[1:]
    parser = cmdline.create_parser(description='luma.examples arguments')
    args = parser.parse_args(actual_args)

    if args.config:
        # load config from file
        config = cmdline.load_config(args.config)
        args = parser.parse_args(config + actual_args)

    # create device
    try:
        device = cmdline.create_device(args)
        return device

    except error.Error as e:
        parser.error(e)
        return None

device = get_device(display=sh1106, interface=gpio_cs_spi, gpio_DC=6, gpio_CS=5, gpio_RST=4, rotate=2)


with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((30, 40), "Hello World", fill="white")
