from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
    package='simple_robot_description',
    executable='l_shape_driver.py',
    arguments=['install/simple_robot_description/lib/simple_robot_description/l_shape_driver.py'],
    output='screen'
)
    ])
