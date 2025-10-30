#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from mitsutoyo_ros.micrometer_data_manager import MicrometerDataManager


def main():
    rospy.init_node('micrometer_data_manager')
    mdm = MicrometerDataManager()
    rospy.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
