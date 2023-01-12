#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-18 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Rotating 3D box wireframe & color dithering.
Adapted from:
http://codentronix.com/2011/05/12/rotating-3d-cube-using-python-and-pygame/
"""

from OledSetup import get_device
from luma.core.render import canvas
from luma.core.sprite_system import framerate_regulator


arguments = ['--display', 'sh1106', '--interface', 'gpio_cs_spi', '--gpio-data-command', '24', '--gpio-chip-select', '8', '--gpio-reset', '25', '--rotate', '2']
device = get_device(arguments)


with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((30, 40), "Hello World", fill="white")