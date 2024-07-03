import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression, PathJoinSubstitution, TextSubstitution

def generate_launch_description():
  ld = LaunchDescription()
  
  # *** PARAMETERS ***
  node2_config = os.path.join(
    get_package_share_directory('my_awesome_system'),
    'config',
    'node2.yaml'
  )

  # *** ROS 2 nodes ***
  node1 = Node(
    package="my_awesome_pkg",
    namespace="/awesome_ns1",
    executable="awesome",
    prefix = 'xterm -e',
    output='screen',
    name="node1",
    remappings=[
      ("awesome_pub", "my_publisher"),
      ("awesome_action", "my_act_server"),
      ("awesome_server", "my_server")]
  )
  node2 = Node(
    package="my_awesome_pkg",
    namespace="/awesome_ns2",
    executable="awesome",
    prefix = 'xterm -e',
    output='screen',
    name="node2",
    remappings=[
      ("awesome_sub", "my_publisher"),
      ("awesome_action_client", "my_act_server"),
      ("awesome_client", "my_server")]
    ,
    parameters = [node2_config]
  )

  # *** ROS 2 subsystems (include launch files)***
  include_my_subsystem= IncludeLaunchDescription(
    PythonLaunchDescriptionSource([ get_package_share_directory('my_subsystem') + '/launch/my_subsystem.launch.py'])
  )

  # *** Add actions ***
  ld.add_action(node1)
  ld.add_action(node2)
  ld.add_action(include_my_subsystem)

  return ld
