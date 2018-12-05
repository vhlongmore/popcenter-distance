# -*- coding: future_fstrings -*-

from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

import math
from decimal import Decimal


class LatLongCoordinate:
    radians_conversion_factor = Decimal(math.pi / 180)

    def __init__(self, lat, long):
        self.latitude = Decimal(lat)
        self.longitude = Decimal(long)

    def convert_to_radians(self):
        """
        Convert the current coordinates from lat/long to rad.
        """
        return (self.latitude * self.radians_conversion_factor,
                self.longitude * self.radians_conversion_factor)

    def __repr__(self):
        return 'LatLongCoordinate' + self.__str__()

    def __str__(self):
        return f'({self.latitude}, {self.longitude})'
