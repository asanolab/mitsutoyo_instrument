#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from mitsutoyo_ros.mitsutoyo_ros_manager import MitsutoyoROSManager


def main():
    rospy.init_node('mitsutoyo_ros_manager_node')
    mrm = MitsutoyoROSManager()
    mrm.publisher()  # publisherを起動


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
