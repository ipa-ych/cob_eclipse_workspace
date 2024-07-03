from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression, PathJoinSubstitution, TextSubstitution

def generate_launch_description():
  ld = LaunchDescription()
  
  # *** PARAMETERS ***

  # *** ROS 2 nodes ***
  node1a = Node(
    package="my_awesome_pkg",
    executable="awesome",
    prefix = 'xterm -e',
    output='screen',
    name="node1a",
    remappings=[
      ("awesome_pub", "other_publisher")]
  )
  node2a = Node(
    package="my_awesome_pkg",
    executable="awesome",
    prefix = 'xterm -e',
    output='screen',
    name="node2a",
    remappings=[
      ("awesome_sub", "other_publisher")]
  )

  # *** ROS 2 subsystems (include launch files)***

  # *** Add actions ***
  ld.add_action(node1a)
  ld.add_action(node2a)

  return ld
