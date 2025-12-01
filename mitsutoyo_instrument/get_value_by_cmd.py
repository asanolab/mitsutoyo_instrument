#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mitsutoyo_ros.mitsutoyo_interface import MitsutoyoInterface


if __name__ ==  "__main__":
    mi = MitsutoyoInterface()
    value = mi.get_value_by_cmd()

    print(value)
