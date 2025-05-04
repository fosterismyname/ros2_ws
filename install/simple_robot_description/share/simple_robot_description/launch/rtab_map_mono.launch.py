from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rtabmap_ros',
            executable='rtabmap',
            name='rtabmap',
            output='screen',
            parameters=[{
                'frame_id': 'base_link',
                'subscribe_depth': False,
                'subscribe_rgb': True,
                'subscribe_scan': False,
                'subscribe_stereo': False,
                'subscribe_rgbd': False,
                'approx_sync': True
            }],
            remappings=[
                ('rgb/image', '/camera_sensor/image_raw'),
                ('rgb/camera_info', '/camera_sensor/camera_info'),
                ('odom', '/odom')
            ]
        )
    ])
