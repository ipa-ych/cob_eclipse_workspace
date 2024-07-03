import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression, PathJoinSubstitution, TextSubstitution

def generate_launch_description():
  ld = LaunchDescription()
  
  # *** PARAMETERS ***
  autorepeat_rate_arg = DeclareLaunchArgument(
    "autorepeat_rate", default_value=TextSubstitution(text="20.0")
  )
  ld.add_action(autorepeat_rate_arg)
  deadzone_arg = DeclareLaunchArgument(
    "deadzone", default_value=TextSubstitution(text="0.3")
  )
  ld.add_action(deadzone_arg)
  joy_dev_arg = DeclareLaunchArgument(
    "joy_dev", default_value=TextSubstitution(text="/dev/input/js0")
  )
  ld.add_action(joy_dev_arg)
  teleop_twist_joy_node_config = os.path.join(
    get_package_share_directory('minimum_teleop'),
    'config',
    'teleop_twist_joy_node.yaml'
  )

  # *** ROS 2 nodes ***
  joy_node = Node(
    package="joy",
    executable="joy_node",
    prefix = 'xterm -e',
    output='screen',
    name="joy_node",
    remappings=[
      ("joy", "joy"),
      ("joy/set_feedback", "joy/set_feedback")]
    ,
    parameters=[{
    "autorepeat_rate": LaunchConfiguration("autorepeat_rate"),
    "deadzone": LaunchConfiguration("deadzone"),
    "joy_dev": LaunchConfiguration("joy_dev"),}]
  )
  teleop_twist_joy_node = Node(
    package="teleop_twist_joy",
    executable="teleop_node",
    prefix = 'xterm -e',
    output='screen',
    name="teleop_twist_joy_node",
    parameters = [teleop_twist_joy_node_config]
  )

  # *** ROS 2 subsystems (include launch files)***

  # *** Add actions ***
  ld.add_action(joy_node)
  ld.add_action(teleop_twist_joy_node)

  return ld
