from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="use_prm_with_namespace",
                executable="use_prm_with_namespace",
                name="use_prm_with_namespace",
                output="screen",
                emulate_tty=True,
                parameters=[
                    {
                        "foo": "new_value_foo", # this works
                        "ns1.bar": "new_value_bar_ns1", # this does not work!
                        "ns2.bar": "new_value_bar_ns2", # this does not work!
                    }
                ],
            ),
        ]
    )