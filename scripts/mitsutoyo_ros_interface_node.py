#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from mitsutoyo_instrument.mitsutoyo_ros_interface import MitsutoyoROSInterface


def main():
    rospy.init_node('mitsutoyo_ros_interface_node')
    mrm = MitsutoyoROSInterface()
    mrm.publisher()  # start publisher


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
