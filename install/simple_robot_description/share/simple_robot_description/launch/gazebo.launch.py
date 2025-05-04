from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import Command
import os

def generate_launch_description():
    pkg_share = get_package_share_directory('simple_robot_description')
    xacro_path = os.path.join(pkg_share, 'urdf', 'simple_robot.xacro')
    world_path = os.path.join(pkg_share, 'worlds', 'room_with_obstacles.world')

    return LaunchDescription([
        # Запускаем Gazebo с нужным миром
        ExecuteProcess(
            cmd=['gazebo', '--verbose', world_path, '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),

        # Публикуем состояние робота
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{'robot_description': Command(['xacro ', xacro_path])}],
            output='screen'
        ),

        # Спауним робота в мир
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'simple_robot', '-topic', 'robot_description'],
            output='screen'
        ),

    ])
