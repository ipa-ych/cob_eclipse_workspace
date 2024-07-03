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
    get_package_share_directory('cob_navi_robot'),
    'config',
    'twist_mux.yaml'
  )
  teleop_twist_joy_node_config = os.path.join(
    get_package_share_directory('cob_navi_robot'),
    'config',
    'teleop_twist_joy_node.yaml'
  )
  slam_toolbox_config = os.path.join(
    get_package_share_directory('cob_navi_robot'),
    'config',
    'slam_toolbox.yaml'
  )

  # *** ROS 2 nodes ***
  joy_node = Node(
    package="joy",
    executable="joy_node",
    prefix = 'xterm -e',
    output='screen',
    name="joy_node",
    remappings=[
      ("joy", "joy_pub")]
    ,
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
      ("cmd_vel", "cmd_vel"),
      ("cmd_vel_out", "/base/twist_controller/command")]
    ,
    parameters = [twist_mux_config]
  )
  teleop_twist_joy_node = Node(
    package="teleop_twist_joy",
    executable="teleop_node",
    prefix = 'xterm -e',
    output='screen',
    name="teleop_twist_joy_node",
    remappings=[
      ("joy", "joy_pub"),
      ("cmd_vel", "cmd_vel")]
    ,
    parameters = [teleop_twist_joy_node_config]
  )
  slam_toolbox = Node(
    package="slam_toolbox",
    executable="async_slam_toolbox_node",
    prefix = 'xterm -e',
    output='screen',
    name="slam_toolbox",
    remappings=[
      ("scan", "scan_unified"),
      ("map", "map"),
      ("map", "map"),
      ("tf", "tf")]
    ,
    parameters = [slam_toolbox_config]
  )

  # *** ROS 2 subsystems (include launch files)***
  include_launch_visual= IncludeLaunchDescription(
    PythonLaunchDescriptionSource([get_package_share_directory('cob_slam') + '/launch/display_robot_0509.launch.py'])
  )
  include_cob_nav2= IncludeLaunchDescription(
    PythonLaunchDescriptionSource([get_package_share_directory('cob_slam') + '/launch/nav2_only.launch.py'])
  )

  # *** Add actions ***
  ld.add_action(joy_node)
  ld.add_action(twist_mux)
  ld.add_action(teleop_twist_joy_node)
  ld.add_action(slam_toolbox)
  ld.add_action(include_launch_visual)
  ld.add_action(include_cob_nav2)

  return ld
