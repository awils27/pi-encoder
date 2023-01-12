# -*- coding: utf-8 -*-
# Copyright (c) 2014-2022 Richard Hull and contributors
# See LICENSE.rst for details.

import sys
import logging

from luma.core import cmdline, error

def get_device(actual_args):
    """
    Create device from command-line arguments and return it.
    """
    parser = cmdline.create_parser(description='luma.examples arguments')
    args = parser.parse_args(actual_args)

    # create device
    try:
        device = cmdline.create_device(args)
        return device

    except error.Error as e:
        parser.error(e)
        return None