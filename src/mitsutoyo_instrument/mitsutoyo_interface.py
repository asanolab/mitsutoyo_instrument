#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from device_control.serial_interface import SerialInterface


class MitsutoyoInterface(SerialInterface):
    def __init__(self):
        super().__init__(baudrate=2400, timeout=1)
        self.open()
        time.sleep(1)  # wait
        # from manual
        # - データは, 1回/秒程度のスピードでの取り込み必要.早いとデータエラーが生じる.
        # - データの取り込み開始前に,一定時間の蓄電が必要.


    def extract_value_from_data(self, data):
        value = None
        # format:
        # 表示 0.1234 -> データ 01A+000.1234
        if(data[0:3] == '01A'):
            value = float(data[3:])
        elif(data[0:2] == '91'):
            print('Known error. see manual')
        else:
            print('Unknown error')

        return value


    def get_value_by_cmd(self):
        input("Waiting for Enter...")

        self.write_str('\n')
        data = self.readline_str()
        value = self.extract_value_from_data(data)

        return value


    def get_value_by_button(self):
        print('Waiting for button input...')
        value = 0

        try:
            while True:
                data = self.readline_str()
                if(data != ''):
                    value = self.extract_value_from_data(data)
                    break
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("Stop reading")

        return value
