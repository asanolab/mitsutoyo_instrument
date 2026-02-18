cmake_minimum_required(VERSION 2.8.0)
project(mitsutoyo_instrument)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
)

catkin_python_setup()

add_service_files(
  FILES
  GetMicrometerValue.srv
  )

add_message_files(
  FILES
  MitsutoyoMicrometer.msg
  )

generate_messages(
  DEPENDENCIES
  std_msgs
  )

catkin_package(
  CATKIN_DEPENDS rospy std_msgs message_runtime
  )

# install
catkin_install_python(
  PROGRAMS
  scripts/mitsutoyo_ros_interface_node.py
  scripts/micrometer_data_manager_node.py
  DESTINATION
    ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(
  DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/
  )
