#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import UInt32
from std_msgs.msg import String
from mitsutoyo_instrument.mitsutoyo_interface import MitsutoyoInterface
from mitsutoyo_instrument_ros1.msg import MitsutoyoMicrometer


class MitsutoyoROSInterface():
    def __init__(self):
        print('Generate MitsutoyoROSInterface')
        self.mi = MitsutoyoInterface()
        self.sample_id = 0
        self.sample_name = 'sample_a'

        # sub
        self.sub_sample_id   = rospy.Subscriber('mitsutoyo_micrometer/write/sample_id', UInt32, self.sample_id_cb)
        self.sub_sample_name = rospy.Subscriber('mitsutoyo_micrometer/write/sample_name', String, self.sample_name_cb)

        # pub
        self.pub = rospy.Publisher('mitsutoyo_micrometer/read', MitsutoyoMicrometer, queue_size=1)


    def sample_id_cb(self, msg):
        self.sample_id = msg.data
        rospy.loginfo('sample_id updated to: %s', self.sample_id)


    def sample_name_cb(self, msg):
        self.sample_name = msg.data
        rospy.loginfo('sample_name updated to: %s', self.sample_name)


    def publisher(self):
        while not rospy.is_shutdown():
            micrometer_value = self.mi.get_value_by_button()  # can't stop by ctrl+c
            rospy.loginfo('id: %s, name: %s, value: %s', self.sample_id, self.sample_name, micrometer_value)
            self.pub.publish(self.sample_id, self.sample_name, micrometer_value)
