#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import pandas as pd
from datetime import datetime
from mitsutoyo_ros.msg import MitsutoyoMicrometer
from mitsutoyo_ros.srv import GetMicrometerValue, GetMicrometerValueResponse


class MicrometerDataManager():
    def __init__(self):
        print('Generate MicrometerDataManager')
        self.df = pd.DataFrame(columns=['time', 'sample_id', 'sample_name', 'value'])
        # subscriber
        rospy.Subscriber('/mitsutoyo_micrometer/read', MitsutoyoMicrometer, self.micrometer_cb)  # micrometer value
        rospy.loginfo("Subscriber started, waiting for micrometer value ...")

        # service
        service = rospy.Service('/get_micrometer_value', GetMicrometerValue, self.handle_get_micrometer_value)
        rospy.loginfo("Service /get_micrometer_value is ready.")

        # destructor
        rospy.on_shutdown(self.save_data)


    def micrometer_cb(self, msg):
        '''store micrometer value when button pushed'''
        new_row = {
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],
            'sample_id': msg.sample_id,
            'sample_name': msg.sample_name,
            'value': msg.value
        }

        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
        rospy.loginfo("Measured value=%s | Measured times=%s", msg.value, len(self.df))


    def handle_get_micrometer_value(self, req):
        '''service: return measured value of specified sample_id'''
        rospy.loginfo(f"Service called with sample_id={req.sample_id}")

        if self.df.empty:
            return GetMicrometerValueResponse(value=0.0, success=False, message="No data received yet.")

        # extract value of specified sample_id
        rows = self.df[self.df['sample_id'] == req.sample_id]
        if not rows.empty:
            latest_row = rows.iloc[-1]
            return GetMicrometerValueResponse(
                value=float(latest_row['value']),
                success=True,
                message=f"Found sample_id={req.sample_id}"
            )
        else:
            return GetMicrometerValueResponse(
                value=0.0,
                success=False,
                message=f"sample_id {req.sample_id} not found"
            )


    def save_data(self, csv_save_path='/tmp/micrometer.csv'):
        rospy.loginfo("Interrupted, saving to CSV...")
        self.df.to_csv(csv_save_path, index=False)
        rospy.loginfo(f"Saved data to {csv_save_path}")
