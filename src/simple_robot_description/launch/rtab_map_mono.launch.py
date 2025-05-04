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
                'subscribe_rgb': True,
                'subscribe_depth': False,
                'subscribe_rgbd': False,
                'approx_sync': True,
                'subscribe_odom_info': True,  # Добавить подписку на одометрию
            }],
            remappings=[
                ('/camera/image_raw', '/camera_sensor/image_raw'),
                ('/camera/camera_info', '/camera_sensor/camera_info'),
                ('/odom', '/odom')
            ]
        ),
        Node(
            package='rtabmap_ros',
            executable='rtabmapviz',
            name='rtabmapviz',
            output='screen',
            parameters=[{
                'frame_id': 'base_link'
            }]
        )
    ])
