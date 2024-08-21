from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression, PathJoinSubstitution, TextSubstitution

def generate_launch_description():
  ld = LaunchDescription()
  
  # *** PARAMETERS ***

  # *** ROS 2 nodes ***
  teleop_key = Node(
    package="teleop_twist_keyboard",
    executable="teleop_twist_keyboard",
    prefix = 'xterm -e',
    output='screen',
    name="teleop_key",
    remappings=[
      ("cmd_vel", "cmd_vel_pub")]
  )

  # *** ROS 2 subsystems (include launch files)***
  include_turtlebot_gazebo= IncludeLaunchDescription(
    PythonLaunchDescriptionSource([get_package_share_directory('turtlebot3_gazebo') + '/launch/turtlebot3_world.launch.py'])
  )

  # *** Add actions ***
  ld.add_action(teleop_key)
  ld.add_action(include_turtlebot_gazebo)

  return ld
