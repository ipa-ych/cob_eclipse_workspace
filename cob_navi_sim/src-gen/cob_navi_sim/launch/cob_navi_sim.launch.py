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
  teleop_twist_joy_node_config = os.path.join(
    get_package_share_directory('cob_navi_sim'),
    'config',
    'teleop_twist_joy_node.yaml'
  )
  twist_mux_config = os.path.join(
    get_package_share_directory('cob_navi_sim'),
    'config',
    'twist_mux.yaml'
  )
  ros2_laserscan_merger_config = os.path.join(
    get_package_share_directory('cob_navi_sim'),
    'config',
    'ros2_laserscan_merger.yaml'
  )
  pointcloud_to_laserscan_config = os.path.join(
    get_package_share_directory('cob_navi_sim'),
    'config',
    'pointcloud_to_laserscan.yaml'
  )
  slam_toolbox_config = os.path.join(
    get_package_share_directory('cob_navi_sim'),
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
  twist_mux = Node(
    package="twist_mux",
    executable="twist_mux",
    prefix = 'xterm -e',
    output='screen',
    name="twist_mux",
    remappings=[
      ("cmd_vel", "cmd_vel"),
      ("cmd_vel_out", "tricycle_controller/cmd_vel")]
    ,
    parameters = [twist_mux_config]
  )
  ros2_laserscan_merger = Node(
    package="ros2_laser_scan_merger",
    executable="ros2_laser_scan_merger_3",
    prefix = 'xterm -e',
    output='screen',
    name="ros2_laserscan_merger",
    remappings=[
      ("base_laser_left/scan_raw", "base_laser_left/scan_raw"),
      ("base_laser_right/scan_raw", "base_laser_right/scan_raw"),
      ("base_laser_front/scan_raw", "base_laser_front/scan_raw"),
      ("cloud_in", "cloud_in")]
    ,
    parameters = [ros2_laserscan_merger_config]
  )
  pointcloud_to_laserscan = Node(
    package="pointcloud_to_laserscan",
    executable="pointcloud_to_laserscan_node",
    prefix = 'xterm -e',
    output='screen',
    name="pointcloud_to_laserscan",
    remappings=[
      ("cloud_in", "cloud_in"),
      ("scan", "scan")]
    ,
    parameters = [pointcloud_to_laserscan_config]
  )
  slam_toolbox = Node(
    package="slam_toolbox",
    executable="async_slam_toolbox_node",
    prefix = 'xterm -e',
    output='screen',
    name="slam_toolbox",
    remappings=[
      ("scan", "scan"),
      ("map", "map"),
      ("map", "map"),
      ("tf", "tf")]
    ,
    parameters = [slam_toolbox_config]
  )
  rviz2 = Node(
    package="rviz2",
    executable="rviz2",
    prefix = 'xterm -e',
    output='screen',
    name="rviz2",
    remappings=[
      ("cloud_in", "cloud_in"),
      ("robot_description", "robot_description"),
      ("map", "map")]
  )

  # *** ROS 2 subsystems (include launch files)***
  include_cob_gazebo= IncludeLaunchDescription(
    PythonLaunchDescriptionSource([get_package_share_directory('cob_sim') + '/launch/cob_gazebo_slam_base.launch.py'])
  )
  include_cob_nav2= IncludeLaunchDescription(
    PythonLaunchDescriptionSource([get_package_share_directory('cob_sim') + '/launch/cob_navi.launch.py'])
  )

  # *** Add actions ***
  ld.add_action(joy_node)
  ld.add_action(teleop_twist_joy_node)
  ld.add_action(twist_mux)
  ld.add_action(ros2_laserscan_merger)
  ld.add_action(pointcloud_to_laserscan)
  ld.add_action(slam_toolbox)
  ld.add_action(rviz2)
  ld.add_action(include_cob_gazebo)
  ld.add_action(include_cob_nav2)

  return ld
