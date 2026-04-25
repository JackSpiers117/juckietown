cmake_minimum_required(VERSION 2.8.3)
project(open_loop_square)

find_package(catkin REQUIRED COMPONENTS
    rospy
)

catkin_package()

catkin_install_python(PROGRAMS
  src/open_loop_square.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
