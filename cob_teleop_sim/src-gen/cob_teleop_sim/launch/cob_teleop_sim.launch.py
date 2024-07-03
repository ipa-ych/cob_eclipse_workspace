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
  twist_mux_config = os.path.join(
    get_package_share_directory('cob_teleop_sim'),
    'config',
    'twist_mux.yaml'
  )
  teleop_twist_joy_node_config = os.path.join(
    get_package_share_directory('cob_teleop_sim'),
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
    parameters=[{
    "autorepeat_rate": LaunchConfiguration("autorepeat_rate"),
    "deadzone": LaunchConfiguration("deadzone"),
    "joy_dev": LaunchConfiguration("joy_dev"),}]
  )
  twist_mux = Node(
    package="twist_mux",
    executable="twist_mux",
    prefix = 'xterm -e',
    output='screen',
    name="twist_mux",
    remappings=[
      ("cmd_vel", "cmd_vel_pub"),
      ("cmd_vel_out", "cmd_vel_out")]
    ,
    parameters = [twist_mux_config]
  )
  cmd_vel_bridge_node = Node(
    package="tricycle_sim",
    executable="cmd_vel_bridge_Twist_node",
    prefix = 'xterm -e',
    output='screen',
    name="cmd_vel_bridge_node"
  )
  teleop_twist_joy_node = Node(
    package="teleop_twist_joy",
    executable="teleop_node",
    prefix = 'xterm -e',
    output='screen',
    name="teleop_twist_joy_node",
    remappings=[
      ("cmd_vel", "cmd_vel_pub")]
    ,
    parameters = [teleop_twist_joy_node_config]
  )

  # *** ROS 2 subsystems (include launch files)***
  include_cob_gazebo= IncludeLaunchDescription(
    PythonLaunchDescriptionSource([get_package_share_directory('cob_sim') + '/launch/cob_gazebo_0429.launch.py'])
  )

  # *** Add actions ***
  ld.add_action(joy_node)
  ld.add_action(twist_mux)
  ld.add_action(cmd_vel_bridge_node)
  ld.add_action(teleop_twist_joy_node)
  ld.add_action(include_cob_gazebo)

  return ld
