# mitsutoyo_ros

## Setup
マイクロメータの接続後, デバイスの読み書き権限とuser設定をする.
```
sudo chmod a+rw /dev/ttyUSB0
sudo usermod -a -G dialout $USER
```

## Usage
## デバイス単体
```
cd scripts
./get_value_by_button.py  #　then, press push button

or
.get_value_by_cmd.py  # then, press enter
```

## ROS node
```
rosrun mitsutoyo_ros mitsutoyo_ros_manager_node.py
```
