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
    get_package_share_directory('cob_combi_robot_rostooling'),
    'config',
    'twist_mux.yaml'
  )
  teleop_twist_joy_node_config = os.path.join(
    get_package_share_directory('cob_combi_robot_rostooling'),
    'config',
    'teleop_twist_joy_node.yaml'
  )
  slam_toolbox_config = os.path.join(
    get_package_share_directory('cob_combi_robot_rostooling'),
    'config',
    'slam_toolbox.yaml'
  )
  rate_hz_arg = DeclareLaunchArgument(
    "rate_hz", default_value=TextSubstitution(text="0.5")
  )
  ld.add_action(rate_hz_arg)
  num_republish_arg = DeclareLaunchArgument(
    "num_republish", default_value=TextSubstitution(text="10")
  )
  ld.add_action(num_republish_arg)
  ping_starter_arg = DeclareLaunchArgument(
    "ping_starter", default_value=TextSubstitution(text="true")
  )
  ld.add_action(ping_starter_arg)
  behaviortree_file_arg = DeclareLaunchArgument(
    "behaviortree_file", default_value=TextSubstitution(text="/home/nhg-yc/bt_ws/src/ros2_behavior_tree_example/behavior_trees/cob_sim/combi_test_with_Navi_sim.xml")
  )
  ld.add_action(behaviortree_file_arg)

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
  bt_lifecycle_node = Node(
    package="ros2_behavior_tree_example",
    executable="behavior_tree_example",
    prefix = 'xterm -e',
    output='screen',
    name="bt_lifecycle_node",
    remappings=[
      ("setLightGreen", "setLightGreen_ss"),
      ("setLightRed", "setLightRed_ss"),
      ("setLightCyan", "setLightCyan_ss"),
      ("setLightCyanBreath", "setLightCyanBreath_ss"),
      ("setLightCyanSweep", "setLightCyanSweep_ss"),
      ("setMimicAsking", "setMimicAsking_ss"),
      ("setMimicBusy", "setMimicBusy_ss"),
      ("setMimicBlinking", "setMimicBlinking_ss"),
      ("sound_play", "/sound/play_ss")]
    ,
    parameters=[{
    "rate_hz": LaunchConfiguration("rate_hz"),
    "num_republish": LaunchConfiguration("num_republish"),
    "ping_starter": LaunchConfiguration("ping_starter"),
    "behaviortree_file": LaunchConfiguration("behaviortree_file"),}]
  )
  image_decompress = Node(
    package="image_transport",
    executable="republish",
    prefix = 'xterm -e',
    output='screen',
    name="image_decompress",
    remappings=[
      ("/torso_cam3d_left_upright/rgb/image_raw/compressed", "/image_raw/compressed"),
      ("cam_left/decompressed", "cam_left/decompressed")]
  )
  yolov8_node = Node(
    package="yolobot_recognition",
    executable="yolov8_ros2_pt",
    prefix = 'xterm -e',
    output='screen',
    name="yolov8_node",
    remappings=[
      ("Yolov8_Inference", "Yolov8_Inference"),
      ("inference_result", "inference_result"),
      ("yolo_image_input", "image_raw")]
  )

  # *** ROS 2 subsystems (include launch files)***
  include_launch_visual= IncludeLaunchDescription(
    PythonLaunchDescriptionSource([get_package_share_directory('cob_slam') + '/launch/display_robot_0509.launch.py'])
  )
  include_cob_nav2= IncludeLaunchDescription(
    PythonLaunchDescriptionSource([get_package_share_directory('cob_sim_trad') + '/launch/cob_navi_only.launch.py'])
  )

  # *** Add actions ***
  ld.add_action(joy_node)
  ld.add_action(twist_mux)
  ld.add_action(teleop_twist_joy_node)
  ld.add_action(slam_toolbox)
  ld.add_action(bt_lifecycle_node)
  ld.add_action(image_decompress)
  ld.add_action(yolov8_node)
  ld.add_action(include_launch_visual)
  ld.add_action(include_cob_nav2)

  return ld
