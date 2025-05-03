cmake_minimum_required(VERSION 3.8)
project(simple_robot_description)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(xacro REQUIRED)
find_package(rclpy REQUIRED)
find_package(geometry_msgs REQUIRED)

install(DIRECTORY urdf
  DESTINATION share/${PROJECT_NAME}
)

install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

install(
  PROGRAMS
  scripts/l_shape_driver.py
  DESTINATION lib/${PROJECT_NAME}
)
# Install world files
install(
  DIRECTORY worlds
  DESTINATION share/${PROJECT_NAME}
)

ament_package()

