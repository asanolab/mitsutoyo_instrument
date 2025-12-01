# mitsutoyo_instrument

## Install
```
cd mitsutoyo_instrument
python3 -m pip install -e .
```

## Build for ROS interface
```
cd ros1
catkin build
```

## Setup for hardware instrument
マイクロメータの接続後, デバイスの読み書き権限とuser設定をする.
```
sudo chmod a+rw /dev/ttyUSB0
sudo usermod -a -G dialout $USER
```

## Usage
## デバイス単体
```
cd nitsutoyo_instrument
./get_value_by_button.py  # then, press push button

or
.get_value_by_cmd.py  # then, press enter
```

## ROS node
```
roslaunch mitsutoyo_ros mitsutoyo_micrometer.launch
```
