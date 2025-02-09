# Copyright (c) Contributors to the Open 3D Engine Project.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import pathlib

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([str(pathlib.Path(
                get_package_share_directory('slam_toolbox')).joinpath('launch', 'online_async_launch.py'))]),
            launch_arguments = {
                'slam_params_file': str(pathlib.Path(__file__).parent.absolute().joinpath('config', 'slam_params.yaml'))
            }.items()
        ),
        Node(
            package='pointcloud_to_laserscan',
            executable='pointcloud_to_laserscan_node',
            name='pc_to_laserscan',
            parameters=[{
                'min_height': 0.0,
                'max_height': 0.4,
                'range_min': 0.05
            }],
            remappings=[
                ('/cloud_in', '/pc'),
            ]
        )
    ])
